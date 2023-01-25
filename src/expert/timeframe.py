class Timeframe:
    """Timeframe.

    Периоды графиков.
    """

    TICK = 0
    TIMEFRAME_M1 = M1 = 1
    TIMEFRAME_M5 = M5 = 2
    TIMEFRAME_M15 = M15 = 3
    TIMEFRAME_M30 = M30 = 4
    TIMEFRAME_H1 = H1 = 5
    TIMEFRAME_H4 = H4 = 6
    TIMEFRAME_D1 = D1 = 7
    TIMEFRAME_Y1 = Y1 = 8

    PERIOD_CURRENT = 0
    """Текущий период"""

    PERIOD_M1 = 1
    """1 минута"""

    PERIOD_M5 = 5
    """5 минут"""

    PERIOD_M15 = 15
    """15 минут"""

    PERIOD_M30 = 30
    """30 минут"""

    PERIOD_H1 = 60
    """1 час"""

    PERIOD_H4 = 240
    """4 часа"""

    PERIOD_D1 = 1440
    """1 день"""

    PERIOD_W1 = 10080
    """1 неделя"""

    PERIOD_MN1 = 43200
    """1 месяц"""

    # Нестандартные таймфреймы:

    PERIOD_M2 = 2
    """2 минуты"""

    PERIOD_M3 = 3
    """3 минуты"""

    PERIOD_M4 = 4
    """4 минуты"""

    PERIOD_M6 = 6
    """6 минут"""

    PERIOD_M10 = 10
    """10 минут"""

    PERIOD_M12 = 12
    """12 минут"""

    PERIOD_M20 = 20
    """20 минут"""

    PERIOD_H2 = 120
    """2 часа"""

    PERIOD_H3 = 180
    """3 часа"""

    PERIOD_H6 = 360
    """6 часа"""

    PERIOD_H8 = 480
    """8 часа"""

    PERIOD_H12 = 720
    """12 часов"""

    slots: str = "_timeframe"

    def __init__(self, timeframe: int) -> None:
        self._timeframe = timeframe

    @property
    def timeframe(self) -> int:
        return self._timeframe

    @timeframe.setter
    def timeframe(self, value: int) -> None:
        self._timeframe = value
