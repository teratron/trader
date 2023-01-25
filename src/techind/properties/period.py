class Period:
    """Period.
    """

    slots: str = "_period"

    def __init__(self, period: int) -> None:
        self._period = self.check(period)

    @property
    def period(self) -> int:
        return self._period

    @period.setter
    def period(self, value: int) -> None:
        self._period = self.check(value)

    @staticmethod
    def check(value: int) -> int:
        if 0 < value <= 10000:
            return value
        else:
            raise ValueError("")  # TODO: add text exception
