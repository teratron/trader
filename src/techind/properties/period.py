class Period:
    """Period.
    """

    MIN_VALUE: int = 1
    MAX_VALUE: int = 10000

    def __init__(self, period: int) -> None:
        self._period: int = Period._check(period)

    @property
    def period(self) -> int:
        return self._period

    @period.setter
    def period(self, value: int) -> None:
        self._period = Period._check(value)

    @classmethod
    def _check(cls, value: int) -> int:
        if cls.MIN_VALUE <= value <= cls.MAX_VALUE:
            return value
        else:
            raise ValueError("Значение периода не соответствует заданному интервалу")
