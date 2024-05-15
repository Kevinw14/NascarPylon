from enum import Enum


class FlagStatus(Enum):
    NONE = 0
    GREEN = 1
    CAUTION = 2
    RED = 3
    WHITE = 4
    UNKNOWN = 5
    WARMUP = 8
    CHECKERED = 9
