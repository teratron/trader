from abc import ABC, abstractmethod
from typing import Any, Union, Optional, Sequence


DatasetType = Union[
    Sequence[
        Union[
            list[Any],  # [[0.1, 2, 0.3, None], [0.1, 2, 0.3, None], ...]
            tuple[Any],  # [(0.1, 2, 0.3, None), (0.1, 2, 0.3, None), ...]
            Optional[float]  # [0.1, 0.2, 0.3, None]
        ]
    ],
    # list[
    #     Union[
    #         Any,
    #         list[Any],
    #         tuple[Any],
    #         float,
    #         None
    #     ]
    # ],
    # slice,
    None
]

IndicatorType = Union[
    list[Optional[float]],  # [0.1, 0.2, 0.3, None]
    Sequence[list[Optional[float]]],  # [[0.1, 0.2, 0.3, None], [0.1, 0.2, 0.3, None], ...]
    None
]

BufferType = Optional[list[Optional[float]]]
ResultType = Union[BufferType, float]
BarType = Union[int, slice, None]
DataType = Sequence[Union[float, int]]


class Data:
    """Data.
    """

    dataset: DatasetType = None
    buffer: Optional[list[Optional[float]]] = None

    def __init__(self) -> None:
        if self.dataset is not None:
            self.len_dataset: int = len(self.dataset)


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

    def __init__(self, /, dataset: DatasetType, **kwargs: Any) -> None:
        self.dataset = dataset

        if self.dataset is not None:
            self.len_dataset: int = len(self.dataset)

    # Call
    def __call__(self, *, bar: BarType = None, **kwargs: Any) -> ResultType:
        if kwargs != {}:
            self.properties(**kwargs)

        if bar is not None:
            return self.calculate(bar=bar)

        return None

    # Item
    def __getitem__(self, key: BarType) -> ResultType:
        match key:
            case None:
                return None
            case int() if not isinstance(self.dataset, float | None) and 0 <= key < len(self.dataset):
                data = self.dataset[key:key + self.period]
            case slice():
                data = self.dataset[key.start:key.stop + self.period - 1]
            case _:
                raise IndexError("Неверный индекс")

        if isinstance(self.dataset, list) and 0 <= key < len(self.dataset):
            return self.calculate(bar=key)
        else:
            raise IndexError("Неверный индекс")

    def __setitem__(self, key: int, value: float) -> None:
        if not isinstance(key, int) or key < 0:
            raise TypeError("Индекс должен быть целым неотрицательным числом")

        if isinstance(self.dataset, list):
            if key >= len(self.dataset):
                off = key + 1 - len(self.dataset)
                self.dataset.extend([None] * off)

            self.dataset[key] = value

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
