from src.GameLevel import GameLevel


WINDOW_DIMENSIONS = [1200,800]
GRID_BLOCK_DIMENSIONS = [100, 100]
SCORE_BANNER_HEIGHT = 40

FPS_LIMIT = 2

END_SCREEN_WAIT_TIME_SEC = 3

GAME_LEVELS = [
    GameLevel(name='Level 1, no AI', num_ai_drives=0, num_pods=10, is_target_pod_required=False, sensor_range=-1),
    GameLevel(name='Level 2, 1 AI', num_ai_drives=1, num_pods=20, is_target_pod_required=False, sensor_range=-1),
    GameLevel(name='Level 3, 5 AI', num_ai_drives=5, num_pods=30, is_target_pod_required=False, sensor_range=-1),
    GameLevel(name='Level 4, 20 AI', num_ai_drives=20, num_pods=30, is_target_pod_required=False, sensor_range=-1),
    GameLevel(name='Level 5, Advanced - 5 AI', num_ai_drives=5, num_pods=10, is_target_pod_required=True, sensor_range=-1)
]

MAX_MOVES_PER_ROUND = 1000

POD_PICKUP_PROBABILITY = 0.8
POD_DROP_PROBABILITY = 0.1

MIN_GOAL_DIST = 10
