from typing import Union


class Period:
    """Period.
    """

    slots: Union[list[str], str] = "_period"

    def __init_subclass__(cls, **kwargs) -> None:
        Period.slots = [Period.slots]
        Period.slots.extend(cls.slots)
        print("__init_subclass__:Period", cls, cls.slots, Period.slots, kwargs)

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
