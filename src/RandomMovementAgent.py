import random
from src.DriveInterface import DriveInterface
from src.Constants import DriveMove


class RandomMovementAgent(DriveInterface):

    def get_next_move(self, sensor_data):
        move = random.randint(1,4)
        return DriveMove(move)
