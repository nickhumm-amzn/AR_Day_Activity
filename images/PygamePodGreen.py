import pygame
from images.Colors import BLACK, WHITE, RED, GREEN, BLUE, YELLOW, ORANGE, LIGHT_BLUE, DARK_YELLOW
from src.GameConfig import GRID_BLOCK_DIMENSIONS


n = None
g = GREEN
d = DARK_YELLOW

pod_green_img_pixel_array = [
    [n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n],
    [n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n],
    [n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n],
    [n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n],
    [n, n, n, n, g, g, d, d, d, d, d, g, g, d, d, d, d, d, d, g, g, d, d, d, d, d, g, g, n, n, n, n],
    [n, n, n, n, g, g, d, d, d, d, d, g, g, d, d, d, d, d, d, g, g, d, d, d, d, d, g, g, n, n, n, n],
    [n, n, n, n, g, g, d, d, d, d, d, g, g, d, d, d, d, d, d, g, g, d, d, d, d, d, g, g, n, n, n, n],
    [n, n, n, n, g, g, d, d, d, d, d, g, g, d, d, d, d, d, d, g, g, d, d, d, d, d, g, g, n, n, n, n],
    [n, n, n, n, g, g, d, d, d, d, d, g, g, d, d, d, d, d, d, g, g, d, d, d, d, d, g, g, n, n, n, n],
    [n, n, n, n, g, g, d, d, d, d, d, g, g, d, d, d, d, d, d, g, g, d, d, d, d, d, g, g, n, n, n, n],
    [n, n, n, n, g, g, g, g, g, g, g, g, g, g, g, g, g, g, g, g, g, g, g, g, g, g, g, g, n, n, n, n],
    [n, n, n, n, g, g, g, g, g, g, g, g, g, g, g, g, g, g, g, g, g, g, g, g, g, g, g, g, n, n, n, n],
    [n, n, n, n, d, d, d, d, d, d, g, g, g, g, g, g, g, g, g, g, g, g, d, d, d, d, d, d, n, n, n, n],
    [n, n, n, n, d, d, d, d, d, d, g, g, g, g, g, g, g, g, g, g, g, g, d, d, d, d, d, d, n, n, n, n],
    [n, n, n, n, d, d, d, d, d, d, g, g, g, g, g, g, g, g, g, g, g, g, d, d, d, d, d, d, n, n, n, n],
    [n, n, n, n, d, d, d, d, d, d, g, g, g, g, g, g, g, g, g, g, g, g, d, d, d, d, d, d, n, n, n, n],
    [n, n, n, n, d, d, d, d, d, d, g, g, g, g, g, g, g, g, g, g, g, g, d, d, d, d, d, d, n, n, n, n],
    [n, n, n, n, d, d, d, d, d, d, g, g, g, g, g, g, g, g, g, g, g, g, d, d, d, d, d, d, n, n, n, n],
    [n, n, n, n, d, d, d, d, d, d, g, g, g, g, g, g, g, g, g, g, g, g, d, d, d, d, d, d, n, n, n, n],
    [n, n, n, n, d, d, d, d, d, d, g, g, g, g, g, g, g, g, g, g, g, g, d, d, d, d, d, d, n, n, n, n],
    [n, n, n, n, g, g, g, g, g, g, g, g, g, g, g, g, g, g, g, g, g, g, g, g, g, g, g, g, n, n, n, n],
    [n, n, n, n, g, g, g, g, g, g, g, g, g, g, g, g, g, g, g, g, g, g, g, g, g, g, g, g, n, n, n, n],
    [n, n, n, n, g, g, d, d, d, d, d, g, g, d, d, d, d, d, d, g, g, d, d, d, d, d, g, g, n, n, n, n],
    [n, n, n, n, g, g, d, d, d, d, d, g, g, d, d, d, d, d, d, g, g, d, d, d, d, d, g, g, n, n, n, n],
    [n, n, n, n, g, g, d, d, d, d, d, g, g, d, d, d, d, d, d, g, g, d, d, d, d, d, g, g, n, n, n, n],
    [n, n, n, n, g, g, d, d, d, d, d, g, g, d, d, d, d, d, d, g, g, d, d, d, d, d, g, g, n, n, n, n],
    [n, n, n, n, g, g, d, d, d, d, d, g, g, d, d, d, d, d, d, g, g, d, d, d, d, d, g, g, n, n, n, n],
    [n, n, n, n, g, g, d, d, d, d, d, g, g, d, d, d, d, d, d, g, g, d, d, d, d, d, g, g, n, n, n, n],
    [n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n],
    [n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n],
    [n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n],
    [n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n]
]

pod_green_img = pygame.Surface((32, 32), pygame.SRCALPHA, 32)
for i in range(len(pod_green_img_pixel_array)):
    for j in range(len(pod_green_img_pixel_array[0])):
        if pod_green_img_pixel_array[i][j] != None:
            pod_green_img.set_at((j, i), pod_green_img_pixel_array[i][j])

pod_green_img = pygame.transform.scale(pod_green_img, (GRID_BLOCK_DIMENSIONS[0], GRID_BLOCK_DIMENSIONS[1]))

# Old full size image:
    # [n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n],
    # [n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n],
    # [n, n, g, g, d, d, d, d, d, d, d, g, g, d, d, d, d, d, d, d, g, g, d, d, d, d, d, d, g, g, n, n],
    # [n, n, g, g, d, d, d, d, d, d, d, g, g, d, d, d, d, d, d, d, g, g, d, d, d, d, d, d, g, g, n, n],
    # [n, n, g, g, d, d, d, d, d, d, d, g, g, d, d, d, d, d, d, d, g, g, d, d, d, d, d, d, g, g, n, n],
    # [n, n, g, g, d, d, d, d, d, d, d, g, g, d, d, d, d, d, d, d, g, g, d, d, d, d, d, d, g, g, n, n],
    # [n, n, g, g, d, d, d, d, d, d, d, g, g, d, d, d, d, d, d, d, g, g, d, d, d, d, d, d, g, g, n, n],
    # [n, n, g, g, d, d, d, d, d, d, d, g, g, d, d, d, d, d, d, d, g, g, d, d, d, d, d, d, g, g, n, n],
    # [n, n, g, g, d, d, d, d, d, d, d, g, g, d, d, d, d, d, d, d, g, g, d, d, d, d, d, d, g, g, n, n],
    # [n, n, g, g, d, d, d, d, d, d, d, g, g, d, d, d, d, d, d, d, g, g, d, d, d, d, d, d, g, g, n, n],
    # [n, n, g, g, g, g, g, g, g, g, g, g, g, g, g, g, g, g, g, g, g, g, g, g, g, g, g, g, g, g, n, n],
    # [n, n, g, g, g, g, g, g, g, g, g, g, g, g, g, g, g, g, g, g, g, g, g, g, g, g, g, g, g, g, n, n],
    # [n, n, d, d, d, d, d, d, d, d, g, g, g, g, g, g, g, g, g, g, g, g, d, d, d, d, d, d, d, d, n, n],
    # [n, n, d, d, d, d, d, d, d, d, g, g, g, g, g, g, g, g, g, g, g, g, d, d, d, d, d, d, d, d, n, n],
    # [n, n, d, d, d, d, d, d, d, d, g, g, g, g, g, g, g, g, g, g, g, g, d, d, d, d, d, d, d, d, n, n],
    # [n, n, d, d, d, d, d, d, d, d, g, g, g, g, g, g, g, g, g, g, g, g, d, d, d, d, d, d, d, d, n, n],
    # [n, n, d, d, d, d, d, d, d, d, g, g, g, g, g, g, g, g, g, g, g, g, d, d, d, d, d, d, d, d, n, n],
    # [n, n, d, d, d, d, d, d, d, d, g, g, g, g, g, g, g, g, g, g, g, g, d, d, d, d, d, d, d, d, n, n],
    # [n, n, d, d, d, d, d, d, d, d, g, g, g, g, g, g, g, g, g, g, g, g, d, d, d, d, d, d, d, d, n, n],
    # [n, n, d, d, d, d, d, d, d, d, g, g, g, g, g, g, g, g, g, g, g, g, d, d, d, d, d, d, d, d, n, n],
    # [n, n, g, g, g, g, g, g, g, g, g, g, g, g, g, g, g, g, g, g, g, g, g, g, g, g, g, g, g, g, n, n],
    # [n, n, g, g, g, g, g, g, g, g, g, g, g, g, g, g, g, g, g, g, g, g, g, g, g, g, g, g, g, g, n, n],
    # [n, n, g, g, d, d, d, d, d, d, d, g, g, d, d, d, d, d, d, d, g, g, d, d, d, d, d, d, g, g, n, n],
    # [n, n, g, g, d, d, d, d, d, d, d, g, g, d, d, d, d, d, d, d, g, g, d, d, d, d, d, d, g, g, n, n],
    # [n, n, g, g, d, d, d, d, d, d, d, g, g, d, d, d, d, d, d, d, g, g, d, d, d, d, d, d, g, g, n, n],
    # [n, n, g, g, d, d, d, d, d, d, d, g, g, d, d, d, d, d, d, d, g, g, d, d, d, d, d, d, g, g, n, n],
    # [n, n, g, g, d, d, d, d, d, d, d, g, g, d, d, d, d, d, d, d, g, g, d, d, d, d, d, d, g, g, n, n],
    # [n, n, g, g, d, d, d, d, d, d, d, g, g, d, d, d, d, d, d, d, g, g, d, d, d, d, d, d, g, g, n, n],
    # [n, n, g, g, d, d, d, d, d, d, d, g, g, d, d, d, d, d, d, d, g, g, d, d, d, d, d, d, g, g, n, n],
    # [n, n, g, g, d, d, d, d, d, d, d, g, g, d, d, d, d, d, d, d, g, g, d, d, d, d, d, d, g, g, n, n],
    # [n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n],
    # [n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n]