from dataclasses import dataclass


@dataclass
class GameLevel:
    name: str
    num_ai_drives: int
    num_pods: int
    is_target_pod_required: bool
    sensor_range: int