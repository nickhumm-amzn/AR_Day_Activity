from dataclasses import dataclass


@dataclass
class Pod:
    game_id: int
    contents = []
    is_goal_pod = False