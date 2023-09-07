import random
from src.DriveInterface import DriveInterface
from src.DriveState import DriveState
from src.GameConfig import POD_PICKUP_PROBABILITY, POD_DROP_PROBABILITY
from src.Constants import DriveMove


class AIDrive(DriveInterface):
    def __init__(self, game_id, is_advanced_mode):
        self.id = game_id
        self.is_advanced_mode = is_advanced_mode

    def get_next_move(self, sensor_data):
        # move
        move = random.randint(1,6)
        return DriveMove(move)
        