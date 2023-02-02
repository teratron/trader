from abc import ABC, abstractmethod

from typing import Any

from techind.properties.price import Price
from techind.types import DataSeriesType, BufferType, ResultType, KeyType


class Indicator(ABC, Price):
    """Indicator.
    """

    data_series: DataSeriesType = None
    data_buffer: BufferType = None
    len_dataset: int = 0
    is_ready: bool = False

    def __init__(self, /, dataset: DataSeriesType, price: int) -> None:
        Price.__init__(self, price)

        if isinstance(dataset, list):  # TODO: validation data_series
            self.data_series = dataset
            self.len_dataset = len(self.data_series)

            if self.len_dataset > 0:
                if self.data_buffer is None:
                    self.data_buffer = []
                    # self.data_buffer.clear()

                match self.data_series[0]:
                    case float():
                        self.data_buffer = self.data_series[:]
                    case tuple():
                        for row in self.data_series:
                            match row:
                                case tuple():
                                    self.data_buffer.append(self.get_price(*row[1:5]))  # TODO: OHLC
                                case _:
                                    raise ValueError("Данные не определены")
                    case _:
                        raise ValueError("Данные не определены")

                if self.len_dataset == len(self.data_buffer):
                    self.is_ready = self.calculate()

    def __call__(self, *, key: KeyType = None, **kwargs: Any) -> ResultType:
        self.set_properties(**kwargs)
        return self.__getitem__(key)

    def __getitem__(self, key: KeyType) -> ResultType:
        if self.is_ready:
            match key:
                case int() if 0 <= key < self.len_dataset:
                    return self.data_buffer[key]
                case slice():
                    start: int = key.start if key.start is not None else 0
                    stop: int = key.stop if key.stop is not None else self.len_dataset

                    if 0 <= start < stop <= self.len_dataset:
                        return self.data_buffer[start:stop]
                case _:
                    raise IndexError("Неверный индекс")

    def __setitem__(self, key: KeyType, value: ResultType) -> None:
        if not isinstance(key, int | slice) or not isinstance(value, float):
            raise TypeError("Неверный тип индекса")

        print("Нет возможности вносить изменения в данные")

    def __delitem__(self, key: KeyType) -> None:
        if not isinstance(key, int | slice):
            raise TypeError("Неверный тип индекса")

        print("Нет возможности удалять данные")

    def set_properties(self, **kwargs: Any) -> None:
        if kwargs != {}:
            for key in kwargs:
                if key in self.__dict__:
                    self.__dict__[key] = kwargs[key]

    @abstractmethod
    def calculate(self, *args: Any, **kwargs: Any) -> bool:
        ...
