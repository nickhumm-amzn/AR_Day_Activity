from src.DriveInterface import DriveInterface
from src.DriveState import DriveState
from src.Constants import DriveMove, SensorData


class DfsSolverAgent(DriveInterface):

    def __init__(self, game_id, is_advanced_mode):
        # Constructor for player
        # Player ID will always be 0
        self.game_id  = game_id
        self.path = []
        self.field_limits = []
        self.path_move_index = 0
        self.need_to_find_target_pod = is_advanced_mode

    def get_next_move(self, sensor_data) -> DriveMove:
        # Main function called by game orchestrator
        # Returns a DriveMove enum value
        if len(self.path) == 0:
            if self.need_to_find_target_pod:
                # Advanced mode - Need to find the target pod and bring it to the goal
                raise Exception('Advanced mode solver not implemented yet for DfsSolverAgent')
            else:
                self.dfs_solve_path_to_goal(sensor_data, sensor_data[SensorData.GOAL_LOCATION])

        next_move, next_state = self.get_move_for_next_state_in_path()
        if self.will_next_state_collide(next_state, sensor_data):
            self.path_move_index -= 1
            # print('Next move would have crashed player, waiting 1 move.')
            return DriveMove.NONE
        else:
            return next_move

    def will_next_state_collide(self, state, sensor_data):
        # Not implemented yet
        return False

    def get_move_for_next_state_in_path(self) -> DriveMove:
        # Function to find the move which will get the player to the next state in self.path
        current_state = self.path[self.path_move_index]
        self.path_move_index += 1
        next_state = self.path[self.path_move_index]

        for move in DriveMove:
            if current_state.get_next_state_from_move(move) == next_state.to_tuple():
                return move, next_state

        print('WARN next move could not be found')
        return DriveMove.NONE, next_state

    def dfs_solve_path_to_goal(self, sensor_data, goal):
        # Depth First Search solver to find a path between SensorData.PLAYER_LOCATION and the goal argument         
        start_state = sensor_data[SensorData.PLAYER_LOCATION]

        new_states = [DriveState(x=start_state[0], y=start_state[1])]
        visited_states = set([])
        paths = [[new_states[0]]]

        while len(paths) > 0:
            current_path = paths.pop(len(paths)-1)
            curr_state = current_path[-1]
            if curr_state.x == goal[0] and curr_state.y == goal[1]:
                self.path = current_path
                return

            visited_states.add(curr_state)
            
            for state in self.list_all_next_possible_states(curr_state):
                if state not in visited_states and self.is_state_in_bounds(state, sensor_data):
                    paths.append(current_path + [state])

        print('WARN Could not find solution from DFS solver')

    def list_all_next_possible_states(self, state) -> list[int]:
        # Returns a list of all reachable states from the argument state by iterating over all possible drive moves
        next_states = []
        for move in DriveMove:
            x, y = state.get_next_state_from_move(move)
            next_states.insert(0, DriveState(x=x, y=y))

        return next_states

    def is_state_in_bounds(self, state, sensor_data) -> bool:
        # Checks if state argument is not a field wall
        return [state.x, state.y] not in sensor_data[SensorData.FIELD_BOUNDARIES]

    def is_player_drive_carrying_a_pod(self, sensor_data) -> bool:
        # Checks if player game id is the first value in any of the entries in SensorData.DRIVE_LIFTED_POD_PAIRS
        return self.game_id in [drive_pod_pair[0] for drive_pod_pair in sensor_data[SensorData.DRIVE_LIFTED_POD_PAIRS]]
            