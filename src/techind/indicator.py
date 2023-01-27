from abc import ABC, abstractmethod
from typing import Any, Union, Sequence

from techind.properties.method import Method

DatasetType = Union[
    # list[
    #     Union[
    #         tuple[Optional[Any]],
    #         Optional[float]
    #     ]
    # ],
    list[tuple[int, float, float, float, float, int, int, int]],  # OHLC Data
    list[tuple[int, float, float, float, int, int, int, float]],  # Tick Data
    list[float],
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
    list[float],
    tuple[float, ...],
    float,
    None
]

BarType = Union[int, slice, None]
DataType = Sequence[Union[float, int]]


# class Data:
#     """Data.
#     """
#
#     buffer: BufferType = None
#
#     def __init__(self, dataset: DatasetType = None) -> None:
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
    properties = None
    dataset = None
    buffer = None

    def __init_subclass__(cls, **kwargs: Any):
        props = list(filter(lambda x: x.__name__ == "Properties", cls.__bases__))
        if props:
            Indicator.properties = props[0]

    def __init__(self, /, dataset: DatasetType, **kwargs: Any) -> None:
        self.dataset = dataset
        # self.buffer: BufferType = None
        self.len_dataset: int = 0

        if self.dataset is not None:
            self.len_dataset = len(self.dataset)

        print(self.len_dataset)
        print(self.dataset)
        # match self.dataset:
        #     case Type(self.dataset) as a:
        #         print("++++++")

    def __call__(self, *, bar: BarType = None, **kwargs: Any) -> ResultType:
        if kwargs != {} and Indicator.properties is not None:
            Indicator.__dict__["properties"].__init__(self, **kwargs)

        if bar is not None:
            return self.__getitem__(bar)

        return None

    def __getitem__(self, key: BarType) -> ResultType:
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
    def calculate(self, *args: Any, **kwargs: Any) -> ResultType:
        ...


def moving_average(data: DataType, period: int, method: int = Method.SMA) -> ResultType:
    """Скользящая средняя."""
    length = len(data)
    if period > length:
        print(f"Период `{period=}` превышает длину массива `{length=}`")
        return None
    elif period == length:
        return sum(data) / float(period)

    if not isinstance(data, list):
        data = list(data)

    match method:
        case Method.SMA:  # SMA(i) = SUM(CLOSE(i), N) / N
            return [
                sum(data[i:period + i]) / float(period)
                for i in range(length - period + 1)
            ]
        case Method.EMA:  # EMA(i) = (CLOSE(i) * P) + (EMA(i - 1) * (100 - P))
            pass
        case Method.SMMA:  # SMMA(0) = SUM(CLOSE(i), N) / N; SMMA(i) = (SUM(CLOSE(i), N) - SMMA(i - 1) + CLOSE(i)) / N
            pass
        case Method.LWMA:  # LWMA(i) = SUM(CLOSE(i) * i, N) / SUM(i, N)
            pass

    return None
