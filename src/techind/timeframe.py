from enum import IntEnum


class Timeframe(IntEnum):
    TICK = 0
    TIMEFRAME_M1 = 1
    TIMEFRAME_M5 = 2
    TIMEFRAME_M15 = 3
    TIMEFRAME_M30 = 4
    TIMEFRAME_H1 = 5
    TIMEFRAME_H4 = 6
    TIMEFRAME_D1 = 7
    TIMEFRAME_Y1 = 8
