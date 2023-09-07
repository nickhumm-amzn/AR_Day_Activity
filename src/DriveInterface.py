from abc import ABC, abstractmethod
from src.DriveState import DriveState


class DriveInterface(ABC):
    def __init__(self, game_id, is_advanced_mode):
        self.id = game_id
        self.is_advanced_mode = is_advanced_mode

    @abstractmethod
    def get_next_move(self, sensor_data):
        pass