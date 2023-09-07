from dataclasses import dataclass
from src.Constants import Heading, DriveMove


@dataclass
class DriveState:
    x: int
    y: int

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __hash__(self):
        return hash((self.x, self.y))

    def heading_to_string(self):
        return self.heading.name

    def to_tuple(self):
        return (self.x, self.y)

    def get_next_state_from_move(self, move):
        if move == DriveMove.UP:
            return self.x, self.y + 1
        elif move == DriveMove.DOWN:
            return self.x, self.y - 1
        elif move == DriveMove.RIGHT:
            return self.x + 1, self.y
        elif move == DriveMove.LEFT:
            return self.x - 1, self.y
        else: # NONE or POD operation
            return self.x, self.y

    def update_state_from_move(self, move):
        new_x, new_y = self.get_next_state_from_move(move)
        self.x = new_x
        self.y = new_y
