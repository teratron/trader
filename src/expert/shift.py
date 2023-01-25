class Shift:
    """Shift.
    """

    slots: str = "_shift"

    def __init__(self, shift: int) -> None:
        self._shift = shift

    @property
    def shift(self) -> int:
        return self._shift

    @shift.setter
    def shift(self, value: int) -> None:
        if 0 < value < 1000:
            self._shift = value
        else:
            raise ValueError("")
