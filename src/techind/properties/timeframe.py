class Timeframe:
    """Timeframe.
    """

    slots = "_timeframe"

    TICK = 0
    TIMEFRAME_M1 = M1 = 1
    TIMEFRAME_M5 = M5 = 2
    TIMEFRAME_M15 = M15 = 3
    TIMEFRAME_M30 = M30 = 4
    TIMEFRAME_H1 = H1 = 5
    TIMEFRAME_H4 = H4 = 6
    TIMEFRAME_D1 = D1 = 7
    TIMEFRAME_Y1 = Y1 = 8

    def __init__(self, timeframe: int) -> None:
        self._timeframe = timeframe

    @property
    def timeframe(self) -> int:
        return self._timeframe

    @timeframe.setter
    def timeframe(self, value: int) -> None:
        self._timeframe = value
