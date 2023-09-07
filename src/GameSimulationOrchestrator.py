import pygame
import time
import random
import math
import traceback
from src.AIDrive import AIDrive
from src.Constants import DriveMove
from src.Field import Field
from src.FieldRenderer import FieldRenderer
from src.GameConfig import WINDOW_DIMENSIONS, GRID_BLOCK_DIMENSIONS, SCORE_BANNER_HEIGHT, END_SCREEN_WAIT_TIME_SEC, FPS_LIMIT, MAX_MOVES_PER_ROUND
from src.GameIdProvider import GameIdProvider
from src.Pod import Pod

class GameSimulationOrchestrator:

    def __init__(self, drive_agent, level):

        # Initialise game window
        pygame.display.set_caption('AR Simulator Game')

        self.game_window = pygame.display.set_mode((WINDOW_DIMENSIONS[0], WINDOW_DIMENSIONS[1] + SCORE_BANNER_HEIGHT))

        # FPS (frames per second) controller
        self.game_clock = pygame.time.Clock()

        # Initialize game field
        field_grid_width = math.floor(WINDOW_DIMENSIONS[0]/GRID_BLOCK_DIMENSIONS[0])
        field_grid_height = math.floor(WINDOW_DIMENSIONS[1]/GRID_BLOCK_DIMENSIONS[1])
        self.field = Field(field_grid_width, field_grid_height, is_pod_required_to_win=level.is_target_pod_required)
        self.field.set_sensor_range(level.sensor_range)

        # Initialize game objects
        id_provider = GameIdProvider()
        self.field.spawn_goal()
        
        player_id = id_provider.get_new_id()
        self.player_drive = drive_agent(player_id, level.is_target_pod_required)
        self.field.spawn_player(self.player_drive, player_id)
        
        self.ai_drive_list = []
        for i in range(level.num_ai_drives):
            ai_drive = AIDrive(id_provider.get_new_id(), level.is_target_pod_required)
            self.field.spawn_new_ai_drive(ai_drive)
            self.ai_drive_list.append(ai_drive)

        self.pod_list = []
        pod_id_provider = GameIdProvider()
        if level.is_target_pod_required:
            pod = Pod(game_id=pod_id_provider.get_new_id())
            self.field.spawn_target_pod(pod)
            print('spawned target pod')
        for i in range(level.num_pods):
            pod = Pod(game_id=pod_id_provider.get_new_id())
            self.field.spawn_new_pod(pod)
            self.pod_list.append(pod)

        # Create game renderer
        self.renderer = FieldRenderer(self.field, self.game_window, drive_agent, level.name)

    def game_over_win(self, score):
        print(f'VICTORY, Score = {score}')
        self.renderer.show_victory_screen(score)
        time.sleep(END_SCREEN_WAIT_TIME_SEC)


    def game_over_loss(self, score):
        print(f'GAME OVER, Score = {score}')
        self.renderer.show_loss_screen(score)
        time.sleep(END_SCREEN_WAIT_TIME_SEC)

    def run_game(self):
        score = 0

        while True:
            # Get inputs from player (ignored for simulator)
            for event in pygame.event.get():
                pass

            # Update all game entities 

            # Start with the player entity first
            player_sensor_data = self.field.generate_sensor_data_for_drive(self.player_drive)
            try:
                player_move = self.player_drive.get_next_move(player_sensor_data)
            except Exception as e:
                print(f'Failed to get next move from player. Exception: {e}')
                print(traceback.format_exc())
                return -1
            if not isinstance(player_move, DriveMove):
                print('Received invalid move from player. Move must be an instance of Constants.DriveMove')
                return -1
            valid_move = self.field.process_move_for_drive(player_move, self.player_drive)

            if valid_move:
                score += 1 # counter increments once per turn

                # Next move all AI drives
                for ai_drive in self.ai_drive_list:
                    sensor_data = self.field.generate_sensor_data_for_drive(ai_drive)
                    ai_move = ai_drive.get_next_move(sensor_data)
                    self.field.process_move_for_drive(ai_move, ai_drive)

            # render new field
            self.renderer.update_game_window(score)

            # Refresh game screen
            pygame.display.update()

            # Check for win condition:
            if self.field.is_winning_condition():
                self.game_over_win(score)
                break

            # If the player move was invalid end the game (done after AI moves and UI update to visualize the failure)
            if not valid_move:
                print('Player colided with another drive or left the field! Game Over')
                self.game_over_loss(score)
                score = -1
                break
         
            # Wait remaining time such that fps does not exceed FPS_LIMIT
            self.game_clock.tick(FPS_LIMIT)

            # Check if max moves has been exceeded
            if score >= MAX_MOVES_PER_ROUND:
                print(f'Maximum moves reached: {MAX_MOVES_PER_ROUND}. Ending the round with a failing score')
                self.game_over_loss(score)
                return -1

        return score
