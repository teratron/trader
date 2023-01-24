from typing import Union, Any

from techind.properties.period import Period


class Slot:
    slots: Union[list[str], str] = "_period"

    def __init_subclass__(cls, **kwargs: Any) -> None:
        _slots = [Period.slots]
        _slots.extend(cls.slots)
        print("__init_subclass__:Period", cls, cls.slots, _slots, kwargs)
