from abc import ABC, abstractmethod
from datetime import datetime
from typing import Any, Union, Sequence, NamedTuple, Callable


class OHLCType(NamedTuple):
    open_price: float
    high_price: float
    low_price: float
    close_price: float


class BarType(NamedTuple):
    time: int
    # ohlc_price: OHLCType
    open_price: float
    high_price: float
    low_price: float
    close_price: float
    tick_volume: int
    spread: int
    real_volume: int


bbb = BarType(1672165020, 1.06481, 1.06506, 1.06477, 1.06489, 111, 2, 0)


# aaa: OHLCType =OHLCType(high=1.06481, low=1.06506, close=1.06477)


class TickType(NamedTuple):
    time: datetime
    ask: float
    bid: float
    a: float
    tick_volume: int
    spread: int
    real_volume: int
    b: float


DataSeriesType = Union[
    Sequence[Union[BarType, TickType, float, None]],
    list[Union[BarType, TickType, float, None]],
    list[BarType],
    list[tuple[int, float, float, float, float, int, int, int]],  # OHLC Data
    # list[tuple[int, float, float, float, float, int, int, int]],  # OHLC Data
    # list[tuple[int, float, float, float, int, int, int, float]],  # Tick Data
    # list[float],

    None
]

BufferType = Union[
    # list[
    #     Union[
    #         list[Optional[float]],
    #         Optional[float]
    #     ]
    # ],
    list[list[float]],
    list[list[int | float]],
    list[tuple[int, float]],
    list[float],
    None
]

IndicatorType = BufferType

ResultType = Union[
    # list[
    #     Union[
    #         tuple[Optional[float]],
    #         Optional[float]
    #     ]
    # ],
    # tuple[Optional[float]],
    list[tuple[float, ...]],
    # list[float | None],
    list[Union[float | None]],
    tuple[float, ...],
    float,
    None
]

KeyType = Union[int, slice, None]
DataType = Sequence[Union[float, int]]


# class Data:
#     """Data.
#     """
#
#     buffer: BufferType = None
#
#     def __init__(self, dataset: DataSeriesType = None) -> None:
#         self.dataset = dataset
#
#         if self.dataset is not None:
#             self.len_dataset: int = len(self.dataset)


# class Properties(ABC):
#     """Properties.
#     """
#
#     @abstractmethod
#     def __init__(self, **kwargs: Any) -> None:
#         ...


class Indicator(ABC):
    """Indicator.
    """

    # slots: Union[list[str], str] = [
    #     Symbol.slots,
    #     Timeframe.slots
    # ]

    name = "indicator"
    type = "Indicator"
    description = __doc__
    # properties = None
    dataset: DataSeriesType = None
    buffer = None

    # def __init_subclass__(cls, **kwargs: Any):
    #     props = list(filter(lambda x: x.__name__ == "Properties", cls.__bases__))
    #     if props:
    #         Indicator.properties = props[0]

    def __init__(self, /, dataset: DataSeriesType, **kwargs: Any) -> None:
        self.dataset = dataset
        # self.buffer: BufferType = None
        self.len_dataset: int = 0

        if isinstance(self.dataset, Sequence):
            self.len_dataset = len(self.dataset)

        print(self.len_dataset)
        print(self.dataset)

        # match self.dataset:
        #     case list():
        #         print("++++++", len(self.dataset[0][1:5]))

        # pr = self.get(*self.dataset[0][1:5])
        # print(pr)
        # print(price_open, price_high, price_low, price_close)

    def __call__(self, *, bar: KeyType = None, **kwargs: Any) -> ResultType:
        # if kwargs != {} and Indicator.properties is not None:
        if kwargs != {}:
            # Indicator.__dict__["properties"].__init__(self, **kwargs)
            # print("************",kwargs)
            self.__class__.properties(self, **kwargs)

        if bar is not None:
            return self.__getitem__(bar)

        return None

    def __getitem__(self, key: KeyType) -> ResultType:
        valid: bool = False
        match key:
            case int():
                valid = 0 <= key < self.len_dataset
            case slice():
                start: int = key.start if key.start is not None else 0
                stop: int = key.stop if key.stop is not None else self.len_dataset
                valid = 0 <= start < stop <= self.len_dataset

        if valid:
            return self.calculate(bar=key)

        raise IndexError("Неверный индекс")

    def __setitem__(self, key: int, value: float) -> None:
        if not isinstance(key, int):
            raise TypeError("Индекс должен быть целым числом")

        if key < 0:
            raise IndexError("Индекс должен быть неотрицательным числом")

        match self.buffer:
            case list():
                if key >= self.len_dataset:
                    off = key + 1 - self.len_dataset
                    self.buffer.extend([None] * off)

                self.buffer[key] = value
            case _:
                raise TypeError("Буфер индикатора не соответствует необходимому типу данных")

    def __delitem__(self, key: int) -> None:
        if not isinstance(key, int):
            raise TypeError("Индекс должен быть целым числом")

        if isinstance(self.dataset, list):
            del self.dataset[key]

    @abstractmethod
    def properties(self, **kwargs: Any) -> None:
        ...

    @abstractmethod
    def calculate(self, *args: Any, **kwargs: Any) -> ResultType:
        ...


def _init(obj: type, class_name: str, call: Callable[[type], None]) -> None:
    props = list(filter(lambda x: x.__name__ == class_name, obj.__bases__))
    if props:
        call(props[0])
