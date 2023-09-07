import pygame
from images.Colors import BLACK, WHITE, RED, GREEN, BLUE, YELLOW, ORANGE, LIGHT_BLUE
from src.GameConfig import GRID_BLOCK_DIMENSIONS


n = None
b = LIGHT_BLUE
w = WHITE

blue_drive_img_pixel_array = [
    [n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n],
    [n, n, n, n, n, n, n, n, n, n, n, n, n, w, w, w, w, w, w, n, n, n, n, n, n, n, n, n, n, n, n, n],
    [n, n, n, n, n, n, n, n, n, n, w, w, w, b, w, w, w, w, b, w, w, w, n, n, n, n, n, n, n, n, n, n],
    [n, n, n, n, n, n, n, n, n, w, b, b, b, b, w, w, w, w, b, b, b, b, w, n, n, n, n, n, n, n, n, n],
    [n, n, n, n, n, n, n, n, w, b, b, b, b, b, w, w, w, w, b, b, b, b, b, w, n, n, n, n, n, n, n, n],
    [n, n, n, n, n, n, n, w, b, b, b, b, b, b, b, w, w, b, b, b, b, b, b, b, w, n, n, n, n, n, n, n],
    [n, n, n, n, n, n, w, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, w, n, n, n, n, n, n],
    [n, n, n, n, n, n, w, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, w, n, n, n, n, n, n],
    [n, n, n, n, n, w, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, w, n, n, n, n, n],
    [n, n, n, n, n, w, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, w, n, n, n, n, n],
    [n, n, n, n, w, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, w, n, n, n, n],
    [n, n, n, n, w, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, w, n, n, n, n],
    [n, n, n, w, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, w, n, n, n],
    [n, n, n, w, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, w, n, n, n],
    [n, n, n, w, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, w, n, n, n],
    [n, n, n, w, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, w, n, n, n],
    [n, n, n, w, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, w, n, n, n],
    [n, n, n, w, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, w, n, n, n],
    [n, n, n, w, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, w, n, n, n],
    [n, n, n, w, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, w, n, n, n],
    [n, n, n, n, w, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, w, n, n, n, n],
    [n, n, n, n, w, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, w, n, n, n, n],
    [n, n, n, n, n, w, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, w, n, n, n, n, n],
    [n, n, n, n, n, w, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, w, n, n, n, n, n],
    [n, n, n, n, n, n, w, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, w, n, n, n, n, n, n],
    [n, n, n, n, n, n, w, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, w, n, n, n, n, n, n],
    [n, n, n, n, n, n, n, w, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, w, n, n, n, n, n, n, n],
    [n, n, n, n, n, n, n, n, w, b, b, b, b, b, b, b, b, b, b, b, b, b, b, w, n, n, n, n, n, n, n, n],
    [n, n, n, n, n, n, n, n, n, w, b, b, b, b, b, b, b, b, b, b, b, b, w, n, n, n, n, n, n, n, n, n],
    [n, n, n, n, n, n, n, n, n, n, w, w, w, b, b, b, b, b, b, w, w, w, n, n, n, n, n, n, n, n, n, n],
    [n, n, n, n, n, n, n, n, n, n, n, n, n, w, w, w, w, w, w, n, n, n, n, n, n, n, n, n, n, n, n, n],
    [n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n]
]

blue_drive_img = pygame.Surface((32, 32), pygame.SRCALPHA, 32)
for i in range(len(blue_drive_img_pixel_array)):
    for j in range(len(blue_drive_img_pixel_array[0])):
        if blue_drive_img_pixel_array[i][j] != None:
            blue_drive_img.set_at((j, i), blue_drive_img_pixel_array[i][j])

blue_drive_img = pygame.transform.scale(blue_drive_img, (GRID_BLOCK_DIMENSIONS[0], GRID_BLOCK_DIMENSIONS[1]))
