from typing import Any, Optional, Union


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
