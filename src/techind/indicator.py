from abc import ABC, abstractmethod

from typing import Any, Union, Optional, Sequence

from techind.symbol import Symbol
from techind.timeframe import Timeframe

Result = Union[list[float], float, None]


class Indicator(ABC, Symbol, Timeframe):
    """Indicator.
    """

    _slots_ = [
        Symbol._slots_,
        Timeframe._slots_
    ]

    dataset: Optional[list[Any]] = None

    def __init_subclass__(cls, **kwargs: Any) -> None:
        print("__init_subclass__:Indicator", cls, kwargs)
        # super().__init_subclass__(**kwargs)

    def __init__(
            self,
            /,
            symbol: Optional[str],
            timeframe: int,
            # *args: Any,
            **kwargs: Any
    ) -> None:
        Symbol.__init__(self, symbol)
        Timeframe.__init__(self, timeframe)
        # Symbol.__init__(self, args[0])
        # Timeframe.__init__(self, args[1])
        # print("__init__:Indicator", args)
        self.dataset = [0.0, 1.0, 2.0, 3.0, 4.0, 5.0]

    def __call__(self, *args: Any, **kwargs: Any) -> Any:
        print("__call__:Indicator", args)
        return args[0]

    def __getitem__(self, key: int) -> Result:
        if 0 <= key < len(self.dataset):
            return self.calculate(bar=key)
        else:
            raise IndexError("Неверный индекс")

    def __setitem__(self, key: int, value: float) -> None:
        if not isinstance(key, int) or key < 0:
            raise TypeError("Индекс должен быть целым неотрицательным числом")

        if key >= len(self.dataset):
            off = key + 1 - len(self.dataset)
            self.dataset.extend([None] * off)

        self.dataset[key] = value

    def __delitem__(self, key: int) -> None:
        if not isinstance(key, int):
            raise TypeError("Индекс должен быть целым числом")

        del self.dataset[key]

    def __enter__(self) -> None:
        print("__enter__:Indicator")

    @abstractmethod
    def calculate(self, *args: Any, **kwargs: Any) -> Result:
        pass


def moving_average(data: Sequence[Union[float, int]], /, period: int) -> Result:
    """Скользящая средняя."""
    length = len(data)
    if period > length:
        print(f"Период `{period=}` превышает длину массива `{length=}`")
        return None
    elif period == length:
        return sum(data) / float(period)

    if not isinstance(data, list):
        data = list(data)

    return [
        sum(data[i:period + i]) / float(period)
        for i in range(length - period + 1)
    ]

# if __name__ == "__main__":
#     print(moving_average([0, 1, 2, 3, 4, 5], 3))
#     print(Timeframe["H1"])
