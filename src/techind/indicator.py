from typing import Any, Optional, Union

from techind.symbol import Symbol
from techind.timeframe import Timeframe

Result = Union[Optional[list[Any]], str, int]

print(len(Symbol))
print(len(Timeframe))


class Indicator:  # (Symbol, Timeframe):
    """
    Indicator.
    """

    def __init_subclass__(cls, **kwargs: Any) -> None:
        print("__init_subclass__:Indicator")

    def __subclasscheck__(self, subclass: Any) -> None:
        print("__subclasscheck__:Indicator", subclass)

    def __init__(self, *args: Any #Result

                 # dataset: Optional[list[Any]] = None,
                 # /,
                 # symbol: Optional[str] = None,
                 # timeframe: int = 0
                 ) -> None:
        print("__init__:Indicator", args)
        # self.dataset = dataset
        # self.symbol = symbol
        # self.timeframe = timeframe

    def __call__(self, *args: Any, **kwargs: Any) -> Any:
        print("__call__:Indicator", *args)
        return args
