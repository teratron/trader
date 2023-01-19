from typing import Any, Union, Sequence


# from techind.symbol import Symbol
# from techind.timeframe import Timeframe
# Result = Union[Optional[list[Any]], str, int]
# print(len(Symbol))
# print(len(Timeframe))


class Indicator:  # (Symbol, Timeframe):
    """
    Indicator.
    """

    dataset: list[Any] = []

    def __init_subclass__(cls, **kwargs: Any) -> None:
        print("__init_subclass__:Indicator")

    def __subclasscheck__(self, subclass: Any) -> None:
        print("__subclasscheck__:Indicator", subclass)

    def __init__(self, *args: Any) -> None:
        print("__init__:Indicator", args)
        self.dataset = args[0]

    def __call__(self, *args: Any, **kwargs: Any) -> Any:
        print("__call__:Indicator", *args)
        return args[0]


def moving_average(
        data: Sequence[Union[float, int]],
        /,
        period: int = 1,
        *,
        inverse: bool = False
) -> Union[list[float], float, None]:
    _len = len(data)
    if period > _len:
        print(f"Период {period} превышает длину массива {len(data)}")
        return None
    elif period == _len:
        return sum(data) / float(period)

    if data is not list:
        data = list(data)

    _avg: list[float] = []
    for i in range(_len - period + 1):
        _sum = 0.0
        for item in data[i:period + i]:
            print(item)
            _sum += item

        _avg.append(_sum / float(period))
        print(_avg, end="\n")

    return _avg


if __name__ == "__main__":
    print(moving_average([1, 2, 3, 4, 5], 3))
