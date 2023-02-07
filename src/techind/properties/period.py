class Period:
    """Period - период.
    """

    MIN_PERIOD: int = 1
    MAX_PERIOD: int = 10000

    def __init__(self, period: int) -> None:
        self._period: int = Period.check(period)

    @property
    def period(self) -> int:
        return self._period

    @period.setter
    def period(self, value: int) -> None:
        self._period = Period.check(value)

    @classmethod
    def check(cls, value: int) -> int:
        if cls.MIN_PERIOD <= value <= cls.MAX_PERIOD:
            return value
        raise ValueError(f"{__name__}: значение периода не соответствует заданному интервалу")
