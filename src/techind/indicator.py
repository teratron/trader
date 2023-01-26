from abc import ABC, abstractmethod

from typing import Any, Union, Optional, Sequence

DatasetType = Optional[
    list[
        Union[
            # list[Union[float, int, None]],
            # tuple[Union[float, int, None]],
            Sequence[Union[float, int, None]],
            Optional[float]
        ]
    ]
]

BufferType = Optional[
    list[
        Union[
            list[Optional[float]],
            Optional[float]
        ]
    ]
]

ResultType = Union[
    list[
        Union[
            tuple[Optional[float]],
            Optional[float]
        ]
    ],
    tuple[Optional[float]],
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
    props = None

    def __init_subclass__(cls, **kwargs):
        print("__init_subclass__", cls.__bases__[1].__name__)
        print("__init_subclass__", bool(filter(lambda x: x.__name__ == "Properties2", cls.__bases__)))
        Indicator.props = list(filter(lambda x: x.__name__ == "Properties", cls.__bases__))[0]

    def __init__(self, /, dataset: DatasetType, **kwargs: Any) -> None:
        # print("__init_subclass__", Indicator.props)
        # Data.__init__(self, dataset)
        self.dataset = dataset
        self.buffer: BufferType = None
        self.len_dataset: int = 0

        if self.dataset is not None:
            self.len_dataset = len(self.dataset)

        # print("__init__", self.__class__)
        # self.child = __class__
        # self.instance = self.__class__.instance
        # self.props = next(filter(lambda x: x.__name__ == "Properties", self.__class__.__bases__))
        # print(self.props)

    def __call__(self, *, bar: BarType = None, **kwargs: Any) -> ResultType:
        if kwargs != {}:
            self.properties(**kwargs)

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

        if self.buffer is list[Optional[float]]:
            if key >= self.len_dataset:
                off = key + 1 - self.len_dataset
                self.buffer.extend([None] * off)

            self.buffer[key] = value
        else:
            raise TypeError("Буфер индикатора не соответствует необходимому типу данных")

    def __delitem__(self, key: int) -> None:
        if not isinstance(key, int):
            raise TypeError("Индекс должен быть целым числом")

        if isinstance(self.dataset, list):
            del self.dataset[key]

    def properties(self, **kwargs: Any) -> None:
        # self.props.__init__(self.instance, **kwargs)
        Indicator.props.__init__(self, **kwargs)

    # @abstractmethod
    # def properties(self, **kwargs: Any) -> None:
    #     ...

    @abstractmethod
    def calculate(self, *args: Any, **kwargs: Any) -> ResultType:
        ...


def moving_average(data: DataType, period: int) -> ResultType:
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
