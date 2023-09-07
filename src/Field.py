import random
from src.AIDrive import AIDrive
from src.Constants import DriveMove, Heading, SensorData, MOVE_TO_HEADING_MAP
from src.DriveState import DriveState
from src.GameConfig import POD_PICKUP_PROBABILITY, MIN_GOAL_DIST
from src.GameTile import GameTile
from src.Pod import Pod
from src.Utils import manhattan_dist_2D


SENSOR_DATA_FILTER_FIELDS = [
    SensorData.FIELD_BOUNDARIES,
    SensorData.DRIVE_LOCATIONS,
    SensorData.POD_LOCATIONS,
    SensorData.DRIVE_LIFTED_POD_PAIRS
]

class Field:
    def __init__(self, field_grid_width, field_grid_height, is_pod_required_to_win=False):
        # Initialize backing grid
        self.is_pod_required_to_win = is_pod_required_to_win
        self.field_grid = [[GameTile(drive=None, pod=None, is_goal=False) for row in range(field_grid_height)] for col in range(field_grid_width)]
        self.drive_pod_pairings_map = {} # key = drive object ID, val = Pod currently lifted by drive
        self.drive_states_map = {} # key = drive object ID, val = DriveState object for drive
        self.pod_locations_map = {} # key = pod object ID, val = [x, y] coords of pod
        self.drive_to_game_id_map = {} # key = drive object ID, val = assigned game id
        self.goal_coords = [-1, -1]
        self.player_id = ''
        self.target_pod_id = ''
        self.can_ai_lift_target_pod = False
        self.field_boundary_coords = self.build_list_of_field_boundaries()
        self.sensor_range = -1

    def set_sensor_range(self, sensor_range):
        self.sensor_range = sensor_range

    def spawn_goal(self):
        x = random.randint(0, len(self.field_grid) - 1)
        y = random.randint(0, len(self.field_grid[0]) - 1)
        self.field_grid[x][y].is_goal = True
        self.goal_coords = [x, y]

    def spawn_player(self, player, player_id):
        if self.goal_coords[0] == -1:
            raise Exception('Goal does not exist, cannot decide spawn location for player. Call Field.spawn_goalbefore Field.spawn_player')
        field_x = len(self.field_grid) - 1
        field_y = len(self.field_grid[0]) - 1
        x = random.randint(field_x // 4, 3 * field_x // 4)
        y = random.randint(field_y // 4, 3 * field_y // 4)
        while manhattan_dist_2D([x, y], self.goal_coords) < MIN_GOAL_DIST: 
            y = random.randint(0, len(self.field_grid[0])-1)
            x = random.randint(0, len(self.field_grid)-1)
        self.field_grid[x][y].drive = player
        self.drive_states_map[str(player)] = DriveState(x=x, y=y)
        self.player_id = str(player)
        self.drive_to_game_id_map[str(player)] = player_id

    def spawn_new_ai_drive(self, ai_drive):
        x = random.randint(0, len(self.field_grid) - 1)
        y = random.randint(0, len(self.field_grid[0]) - 1)
        while self.field_grid[x][y].drive != None: 
            y = random.randint(0, len(self.field_grid[0])-1)
            x = random.randint(0, len(self.field_grid)-1)
        self.field_grid[x][y].drive = ai_drive
        self.drive_states_map[str(ai_drive)] = DriveState(x=x, y=y)
        self.drive_to_game_id_map[str(ai_drive)] = ai_drive.id

    def spawn_target_pod(self, pod, can_other_drives_lift=False):
        field_x = len(self.field_grid) - 1
        field_y = len(self.field_grid[0]) - 1
        x = random.randint(field_x // 4, 3 * field_x // 4)
        y = random.randint(field_y // 4, 3 * field_y // 4)
        while manhattan_dist_2D([x, y], self.goal_coords) < MIN_GOAL_DIST: 
            y = random.randint(0, len(self.field_grid[0])-1)
            x = random.randint(0, len(self.field_grid)-1)

        self.field_grid[x][y].pod = pod
        self.pod_locations_map[str(pod)] = [x, y]
        self.target_pod_id = str(pod)

        if can_other_drives_lift == True:
            self.can_ai_lift_target_pod = True
            if self.field_grid[x][y].drive != None:
                if random.uniform(0, 1) < POD_PICKUP_PROBABILITY: # start with pod on drive
                    self.drive_pod_pairings_map[str(self.field_grid[x][y].drive)] = pod

    def spawn_new_pod(self, pod):
        x = random.randint(0, len(self.field_grid) - 1)
        y = random.randint(0, len(self.field_grid[0]) - 1)
        while self.field_grid[x][y].pod != None: 
            y = random.randint(0, len(self.field_grid[0])-1)
            x = random.randint(0, len(self.field_grid)-1)
        self.field_grid[x][y].pod = pod
        self.pod_locations_map[str(pod)] = [x, y]

        if self.field_grid[x][y].drive != None and str(self.field_grid[x][y].drive) != self.player_id:
            if random.uniform(0, 1) < POD_PICKUP_PROBABILITY: # start with pod on drive
                self.drive_pod_pairings_map[str(self.field_grid[x][y].drive)] = pod

    def is_drive_player(self, drive):
        return str(drive) == self.player_id

    def is_pod_target(self, pod):
        return str(pod) == self.target_pod_id

    def process_move_for_drive(self, move, drive):
        current_drive_state = self.drive_states_map[str(drive)]

        if self.will_next_move_crash(move, drive):
            if self.is_drive_player(drive):
                self.field_grid[current_drive_state.x][current_drive_state.y].drive = None
                self.field_grid[current_drive_state.x][current_drive_state.y].is_crash = True
                return False
            else:
                # Do not move AI drives into invalid states. Skip turn for AI instead
                return True
        else:
            # Process Pod operations before moves
            if move == DriveMove.LIFT_POD:
                if self.field_grid[current_drive_state.x][current_drive_state.y].pod != None:
                    if self.is_pod_target(self.field_grid[current_drive_state.x][current_drive_state.y].pod):
                        if self.is_drive_player(drive) or self.can_ai_lift_target_pod:
                            self.drive_pod_pairings_map[str(drive)] = self.field_grid[current_drive_state.x][current_drive_state.y].pod
                    else:
                        self.drive_pod_pairings_map[str(drive)] = self.field_grid[current_drive_state.x][current_drive_state.y].pod
                else:
                    if self.is_drive_player(drive):
                        print(f'Player drive {drive} tried picking up a pod, but no pod was present at current state')
            elif move == DriveMove.DROP_POD:
                if self.is_drive_carrying_a_pod(drive):
                    del self.drive_pod_pairings_map[str(drive)]
                else:
                    if self.is_drive_player(drive):
                        print(f'Player drive {drive} tried dropping a pod, but wasn\'t carrying one')
            else:
                # Move drive
                self.field_grid[current_drive_state.x][current_drive_state.y].drive = None
                if self.is_drive_carrying_a_pod(drive):
                    self.field_grid[current_drive_state.x][current_drive_state.y].pod = None

                current_drive_state.update_state_from_move(move)
                self.field_grid[current_drive_state.x][current_drive_state.y].drive = drive
                self.drive_states_map[str(drive)] = current_drive_state # redundant assignment
                if self.is_drive_carrying_a_pod(drive):
                    self.field_grid[current_drive_state.x][current_drive_state.y].pod = self.drive_pod_pairings_map[str(drive)]
                    self.pod_locations_map[str(self.field_grid[current_drive_state.x][current_drive_state.y].pod)] = [current_drive_state.x, current_drive_state.y]
                
                # Update drive heading for UI
                new_heading = MOVE_TO_HEADING_MAP[move]
                if new_heading != -1:
                    self.field_grid[current_drive_state.x][current_drive_state.y].drive_heading = new_heading

            return True

    def will_next_move_crash(self, move, drive):
        current_drive_state = self.drive_states_map[str(drive)]
        new_x, new_y = current_drive_state.get_next_state_from_move(move)

        if new_x < 0 or new_x >= len(self.field_grid) or new_y < 0 or new_y >= len(self.field_grid[0]):
            # Drive will exit the field
            return True
        elif (new_x, new_y) != current_drive_state.to_tuple():
            if self.field_grid[new_x][new_y].drive != None:
                # Drive will crash into another field
                return True
            elif self.field_grid[new_x][new_y].pod != None and self.is_drive_carrying_a_pod(drive):
                # Drive is carrying a pod and will crash into another pod
                return True
        else:
            return False

    def is_drive_carrying_a_pod(self, drive):
        return str(drive) in self.drive_pod_pairings_map.keys()

    def generate_sensor_data_for_drive(self, drive):
        sensor_data = {
            SensorData.FIELD_BOUNDARIES: self.field_boundary_coords,  
            SensorData.DRIVE_LOCATIONS: [], 
            SensorData.POD_LOCATIONS: [],
            SensorData.DRIVE_LIFTED_POD_PAIRS: self.build_drive_lifted_pod_pairs(),
            SensorData.PLAYER_LOCATION: [],
            SensorData.GOAL_LOCATION: self.goal_coords,
            SensorData.TARGET_POD_LOCATION: self.get_target_pod_info()
        }

        for d in self.drive_states_map.keys():
            x = self.drive_states_map[str(d)].x
            y = self.drive_states_map[str(d)].y
            if str(drive) == d:
                sensor_data[SensorData.PLAYER_LOCATION] = [x, y]
            else:
                sensor_data[SensorData.DRIVE_LOCATIONS].append([x, y])

        for p in self.pod_locations_map.keys():
            sensor_data[SensorData.POD_LOCATIONS].append(self.pod_locations_map[p])

        if self.sensor_range > 0:
            sensor_data = self.filter_sensor_data_for_sensor_range(sensor_data)

        return sensor_data

    def build_drive_lifted_pod_pairs(self):
        drive_lifted_pod_pair_list = []
        for drive_str in self.drive_states_map.keys():
            if drive_str in self.drive_pod_pairings_map.keys():
                drive_lifted_pod_pair_list.append([self.drive_to_game_id_map[drive_str], self.drive_pod_pairings_map[drive_str].game_id]) 

        return drive_lifted_pod_pair_list

    def get_target_pod_info(self):
        if self.target_pod_id != '':
            return self.pod_locations_map[self.target_pod_id]
        else:
            return []

    def filter_sensor_data_for_sensor_range(self, sensor_data):
        player_state = self.drive_states_map[self.player_id]
        player_location = [player_state.x, player_state.y]
        for data_field in SENSOR_DATA_FILTER_FIELDS:
            new_data = []
            for val in sensor_data[data_field]:
                if round(euclidean_dist_2D(player_location, val)) <= self.sensor_range:
                    new_data.append(val)
            sensor_data[data_field] = new_data


    def is_winning_condition(self):
        if self.is_pod_required_to_win and self.target_pod_id != '':
            target_pod_coords = self.pod_locations_map[self.target_pod_id]
            target_state = target_pod_coords
        else:
            player_state = self.drive_states_map[self.player_id]
            target_state = [player_state.x, player_state.y]

        if target_state[0] == self.goal_coords[0] and target_state[1] == self.goal_coords[1]:
            return True
        else:
            return False


    def build_list_of_field_boundaries(self):
        # Add top and bottom boundaries
        bottom_boundary = []
        top_boundary = []
        for i in range(len(self.field_grid) + 2):
            bottom_boundary.append([i-1, -1])
            top_boundary.append([i-1, len(self.field_grid[0])])

        # Add left and right boundaries
        left_boundary = []
        right_boundary = []
        for i in range(len(self.field_grid[0])):
            left_boundary.append([-1, i])
            right_boundary.append([len(self.field_grid), i])

        return bottom_boundary + left_boundary + top_boundary + right_boundary
    