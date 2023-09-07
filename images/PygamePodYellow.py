import pygame
from images.Colors import BLACK, WHITE, RED, GREEN, BLUE, YELLOW, ORANGE, LIGHT_BLUE, DARK_YELLOW
from src.GameConfig import GRID_BLOCK_DIMENSIONS


n = None
y = YELLOW
d = DARK_YELLOW

pod_yellow_img_pixel_array = [
    [n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n],
    [n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n],
    [n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n],
    [n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n],
    [n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n],
    [n, n, n, n, n, y, d, d, d, d, d, y, y, d, d, d, d, d, d, y, y, d, d, d, d, d, y, n, n, n, n, n],
    [n, n, n, n, n, y, d, d, d, d, d, y, y, d, d, d, d, d, d, y, y, d, d, d, d, d, y, n, n, n, n, n],
    [n, n, n, n, n, y, d, d, d, d, d, y, y, d, d, d, d, d, d, y, y, d, d, d, d, d, y, n, n, n, n, n],
    [n, n, n, n, n, y, d, d, d, d, d, y, y, d, d, d, d, d, d, y, y, d, d, d, d, d, y, n, n, n, n, n],
    [n, n, n, n, n, y, d, d, d, d, d, y, y, d, d, d, d, d, d, y, y, d, d, d, d, d, y, n, n, n, n, n],
    [n, n, n, n, n, y, y, y, y, y, y, y, y, y, y, y, y, y, y, y, y, y, y, y, y, y, y, n, n, n, n, n],
    [n, n, n, n, n, y, y, y, y, y, y, y, y, y, y, y, y, y, y, y, y, y, y, y, y, y, y, n, n, n, n, n],
    [n, n, n, n, n, d, d, d, d, d, y, y, y, y, y, y, y, y, y, y, y, y, d, d, d, d, d, n, n, n, n, n],
    [n, n, n, n, n, d, d, d, d, d, y, y, y, y, y, y, y, y, y, y, y, y, d, d, d, d, d, n, n, n, n, n],
    [n, n, n, n, n, d, d, d, d, d, y, y, y, y, y, y, y, y, y, y, y, y, d, d, d, d, d, n, n, n, n, n],
    [n, n, n, n, n, d, d, d, d, d, y, y, y, y, y, y, y, y, y, y, y, y, d, d, d, d, d, n, n, n, n, n],
    [n, n, n, n, n, d, d, d, d, d, y, y, y, y, y, y, y, y, y, y, y, y, d, d, d, d, d, n, n, n, n, n],
    [n, n, n, n, n, d, d, d, d, d, y, y, y, y, y, y, y, y, y, y, y, y, d, d, d, d, d, n, n, n, n, n],
    [n, n, n, n, n, d, d, d, d, d, y, y, y, y, y, y, y, y, y, y, y, y, d, d, d, d, d, n, n, n, n, n],
    [n, n, n, n, n, d, d, d, d, d, y, y, y, y, y, y, y, y, y, y, y, y, d, d, d, d, d, n, n, n, n, n],
    [n, n, n, n, n, y, y, y, y, y, y, y, y, y, y, y, y, y, y, y, y, y, y, y, y, y, y, n, n, n, n, n],
    [n, n, n, n, n, y, y, y, y, y, y, y, y, y, y, y, y, y, y, y, y, y, y, y, y, y, y, n, n, n, n, n],
    [n, n, n, n, n, y, d, d, d, d, d, y, y, d, d, d, d, d, d, y, y, d, d, d, d, d, y, n, n, n, n, n],
    [n, n, n, n, n, y, d, d, d, d, d, y, y, d, d, d, d, d, d, y, y, d, d, d, d, d, y, n, n, n, n, n],
    [n, n, n, n, n, y, d, d, d, d, d, y, y, d, d, d, d, d, d, y, y, d, d, d, d, d, y, n, n, n, n, n],
    [n, n, n, n, n, y, d, d, d, d, d, y, y, d, d, d, d, d, d, y, y, d, d, d, d, d, y, n, n, n, n, n],
    [n, n, n, n, n, y, d, d, d, d, d, y, y, d, d, d, d, d, d, y, y, d, d, d, d, d, y, n, n, n, n, n],
    [n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n],
    [n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n],
    [n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n],
    [n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n],
    [n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n]
]

pod_yellow_img = pygame.Surface((32, 32), pygame.SRCALPHA, 32)
for i in range(len(pod_yellow_img_pixel_array)):
    for j in range(len(pod_yellow_img_pixel_array[0])):
        if pod_yellow_img_pixel_array[i][j] != None:
            pod_yellow_img.set_at((j, i), pod_yellow_img_pixel_array[i][j])

pod_yellow_img = pygame.transform.scale(pod_yellow_img, (GRID_BLOCK_DIMENSIONS[0], GRID_BLOCK_DIMENSIONS[1]))
