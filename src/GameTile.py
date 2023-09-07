from dataclasses import dataclass
from src.Constants import Heading
from src.DriveInterface import DriveInterface
from src.Pod import Pod


@dataclass
class GameTile:
    drive: DriveInterface
    pod: Pod
    is_goal: bool
    is_crash = False
    drive_heading: Heading = Heading.NORTH