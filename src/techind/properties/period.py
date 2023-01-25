class Period:
    """Period.
    """

    slots: str = "_period"
    min_value: int = 1
    max_value: int = 10000

    def __init__(self, period: int) -> None:
        print("period:__init__")
        self._period = Period.check(period)

    @property
    def period(self) -> int:
        return self._period

    @period.setter
    def period(self, value: int) -> None:
        self._period = self.check(value)

    @classmethod
    def check(cls, value: int) -> int:
        print("period:check")
        if cls.min_value <= value <= cls.max_value:
            return value
        else:
            raise ValueError("")  # TODO: add text exception
