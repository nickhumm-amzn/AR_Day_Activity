import pygame
from src.Constants import Heading
from src.GameConfig import GRID_BLOCK_DIMENSIONS, WINDOW_DIMENSIONS
from src.PygameGraphicsUtils import BLACK, WHITE, RED, GREEN, SCORE_FONT, END_FONT
from images.PygameDriveOrange import orange_drive_img
from images.PygameDriveBlue import blue_drive_img
from images.PygamePlayerDriveOrange import player_orange_drive_img
from images.PygamePodYellow import pod_yellow_img
from images.PygamePodGreen import pod_green_img


class FieldRenderer:
    def __init__(self, field, game_window, agent_class, level_name):
        self.field = field
        self.game_window = game_window
        self.agent_class = agent_class
        self.level_name = level_name

    def update_game_window(self, score):
        # clear screen
        self.game_window.fill(BLACK)

        # draw grid
        self.draw_field_grid()

        # draw each tile in the field
        for x in range(len(self.field.field_grid)):
            for y in range(len(self.field.field_grid[0])):
                self.draw_game_tile_at_x_y(x, y)

        # update score banner
        self.update_score_banner(score)

        # flip screen over y axis to put origin in bottom left
        flip_surface = pygame.transform.flip(self.game_window, False, True)
        self.game_window.blit(flip_surface, (0, 0))

    def draw_game_tile_at_x_y(self, x, y):
        if self.field.field_grid[x][y].drive != None: # drive is present
            drive = self.field.field_grid[x][y].drive
            draw_pod_on_top = False
            if self.field.field_grid[x][y].pod != None:
                img = self.get_drive_image_for_drive(drive)
                draw_pod_on_top = True
            else:
                img = self.get_drive_image_for_drive(drive)
 
            heading = self.field.field_grid[x][y].drive_heading
            if heading == Heading.NORTH: 
                img = pygame.transform.rotate(img, 180)
            elif heading == Heading.EAST:
                img = pygame.transform.rotate(img, 270)
            elif heading == Heading.SOUTH:
                img = pygame.transform.rotate(img, 0)
            else: # Heading.WEST
                img = pygame.transform.rotate(img, 90)

            self.game_window.blit(img, (x*GRID_BLOCK_DIMENSIONS[0], y*GRID_BLOCK_DIMENSIONS[1]))
            if draw_pod_on_top:
                if self.field.is_drive_carrying_a_pod(drive):
                    self.game_window.blit(pod_green_img, (x*GRID_BLOCK_DIMENSIONS[0], y*GRID_BLOCK_DIMENSIONS[1]))
                else:
                    self.game_window.blit(pod_yellow_img, (x*GRID_BLOCK_DIMENSIONS[0], y*GRID_BLOCK_DIMENSIONS[1]))
        elif self.field.field_grid[x][y].pod != None: # pod without drive
            self.game_window.blit(pod_yellow_img, (x*GRID_BLOCK_DIMENSIONS[0], y*GRID_BLOCK_DIMENSIONS[1]))

        # highlight target pod
        if str(self.field.field_grid[x][y].pod) == self.field.target_pod_id:
            outline_surface = pygame.Surface((GRID_BLOCK_DIMENSIONS[0], GRID_BLOCK_DIMENSIONS[1]), pygame.SRCALPHA, 32)
            pygame.draw.rect(outline_surface, RED, pygame.Rect(0, 0, GRID_BLOCK_DIMENSIONS[0], GRID_BLOCK_DIMENSIONS[1]), 2)
            self.game_window.blit(outline_surface, (x*GRID_BLOCK_DIMENSIONS[0], y*GRID_BLOCK_DIMENSIONS[1]))

        # draw goal
        if self.field.field_grid[x][y].is_goal:
            pygame.draw.circle(self.game_window, GREEN, (x*GRID_BLOCK_DIMENSIONS[0]+GRID_BLOCK_DIMENSIONS[0]//2, y*GRID_BLOCK_DIMENSIONS[1]+GRID_BLOCK_DIMENSIONS[1]//2), GRID_BLOCK_DIMENSIONS[1]//4)

        if self.field.field_grid[x][y].is_crash:
            pygame.draw.circle(self.game_window, RED, (x*GRID_BLOCK_DIMENSIONS[0]+GRID_BLOCK_DIMENSIONS[0]//2, y*GRID_BLOCK_DIMENSIONS[1]+GRID_BLOCK_DIMENSIONS[1]//2), GRID_BLOCK_DIMENSIONS[1]//3)

    def get_drive_image_for_drive(self, drive):
        if str(drive) == self.field.player_id:
            return player_orange_drive_img
        else:
            return blue_drive_img

    def draw_field_grid(self):
        for x in range(0, WINDOW_DIMENSIONS[0], GRID_BLOCK_DIMENSIONS[0]):
            for y in range(0, WINDOW_DIMENSIONS[1], GRID_BLOCK_DIMENSIONS[1]):
                if x <= WINDOW_DIMENSIONS[0]-GRID_BLOCK_DIMENSIONS[0] and y <= WINDOW_DIMENSIONS[1]-GRID_BLOCK_DIMENSIONS[1]:
                    rect = pygame.Rect(x, y, GRID_BLOCK_DIMENSIONS[0], GRID_BLOCK_DIMENSIONS[1])
                    pygame.draw.rect(self.game_window, WHITE, rect, 1)

    def update_score_banner(self, score):
        text_surface = SCORE_FONT.render(f'Level: {self.level_name} | Using agent {str(self.agent_class.__name__)}  |  Running Cost = {score}', False, (255, 255, 255))
        text_surface = pygame.transform.flip(text_surface, False, True)
        self.game_window.blit(text_surface, (10, WINDOW_DIMENSIONS[1]+5))

    def show_victory_screen(self, score):
        text_surface = END_FONT.render(f'VICTORY! Total Cost = {score}', True, WHITE)
        temp_surface = pygame.Surface(text_surface.get_size())
        temp_surface.fill(BLACK)
        temp_surface.blit(text_surface, (0, 0))
        text_rect = text_surface.get_rect(center=(WINDOW_DIMENSIONS[0]//2, WINDOW_DIMENSIONS[1]//2))
        self.game_window.blit(temp_surface, text_rect)
        pygame.display.update()

    def show_loss_screen(self, score):
        text_surface = END_FONT.render('GAME OVER', True, WHITE)
        temp_surface = pygame.Surface(text_surface.get_size())
        temp_surface.fill(BLACK)
        temp_surface.blit(text_surface, (0, 0))
        text_rect = text_surface.get_rect(center=(WINDOW_DIMENSIONS[0]//2, WINDOW_DIMENSIONS[1]//2))
        self.game_window.blit(temp_surface, text_rect)
        pygame.display.update()
