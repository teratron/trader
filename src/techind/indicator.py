from typing import Any, Union, Sequence

from techind.symbol import Symbol
from techind.timeframe import Timeframe


# Result = Union[Optional[list[Any]], str, int]
# print(len(Symbol))
# print(len(Timeframe))


class Indicator(Symbol, Timeframe):
    """
    Indicator.
    """

    dataset: list[Any] = []

    def __init_subclass__(cls, **kwargs: Any) -> None:
        print("__init_subclass__:Indicator")
        super().__init_subclass__(**kwargs)

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        print("__init__:Indicator", args)
        self.dataset = args[0]

    def __call__(self, *args: Any, **kwargs: Any) -> Any:
        print("__call__:Indicator", *args)
        return args[0]

    def __getitem__(self, item: int) -> Any:
        if 0 <= item < len(self.dataset):
            return self.dataset[item]
        else:
            raise IndexError("Неверный индекс")

    def __setitem__(self, key: int, value) -> None:
        if not isinstance(key, int) or key < 0:
            raise TypeError("Индекс должен быть целым неотрицательным числом")

        if key >= len(self.dataset):
            off = key + 1 - len(self.dataset)
            self.dataset.extend([None] * off)

        self.dataset[key] = value

    def __delitem__(self, key) -> None:
        if not isinstance(key, int):
            raise TypeError("Индекс должен быть целым числом")

        del self.dataset[key]


def moving_average(
        data: Sequence[Union[float, int]],
        /,
        period: int = 1
) -> Union[list[float], float, None]:
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


if __name__ == "__main__":
    print(moving_average([0, 1, 2, 3, 4, 5], 3))

    # print(Timeframe["H1"])
