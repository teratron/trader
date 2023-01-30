class Period:
    """Period.
    """

    slots: str = "_period"
    min_value: int = 1
    max_value: int = 10000

    def __init__(self, period: int) -> None:
        self._period: int = _check(period)

    @property
    def period(self) -> int:
        return self._period

    @period.setter
    def period(self, value: int) -> None:
        self._period = _check(value)


def _check(value: int) -> int:
    if Period.min_value <= value <= Period.max_value:
        return value
    else:
        raise ValueError("")  # TODO: add text exception
