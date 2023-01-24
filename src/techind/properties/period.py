class Period:
    """Period.
    """

    slots: str = "_period"

    def __init__(self, period: int) -> None:
        self._period = period

    @property
    def period(self) -> int:
        return self._period

    @period.setter
    def period(self, value: int) -> None:
        if 0 < value < 1000:
            self._period = value
        else:
            raise ValueError("")
