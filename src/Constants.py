from enum import Enum


class DriveMove(Enum):
    NONE = 0
    UP = 1
    DOWN = 2
    RIGHT = 3
    LEFT = 4
    LIFT_POD = 5
    DROP_POD = 6

class Heading(Enum):
    NORTH = 0
    EAST = 1
    SOUTH = 2
    WEST = 3

class SensorData(Enum):
    FIELD_BOUNDARIES = 0
    DRIVE_LOCATIONS = 1
    POD_LOCATIONS = 2
    DRIVE_LIFTED_POD_PAIRS = 3
    PLAYER_LOCATION = 4
    GOAL_LOCATION = 5
    TARGET_POD_LOCATION = 6


MOVE_TO_HEADING_MAP = {
    DriveMove.NONE: -1,
    DriveMove.UP: Heading.NORTH,
    DriveMove.DOWN: Heading.SOUTH,
    DriveMove.RIGHT: Heading.EAST,
    DriveMove.LEFT: Heading.WEST
}
