from abc import ABC, abstractmethod
from enum import IntEnum
from typing import Any

from techind.types import DataSeriesType, BufferType, ResultType, KeyType, PriceDataType


class State(IntEnum):
    DATA = 0
    INIT = 1


class Indicator(ABC):
    """Indicator.
    """

    data_series: DataSeriesType = None
    data_buffer: BufferType = None
    price_buffer: PriceDataType = None
    len_dataset: int = 0
    is_ready: bool = False

    def __init__(self, dataset: DataSeriesType) -> None:

        if isinstance(dataset, list):  # TODO: validation data_series
            self.data_series = dataset
            self.len_dataset = len(self.data_series)

            if self.len_dataset > 0:

                # if self.len_dataset == len(self.data_buffer):
                if self.calculate() is None:
                    self.is_ready = True
        else:
            raise TypeError(f"{__name__}: ")  # TODO:

    def __get__(self, instance, owner) -> float:
        print("__get__, instance", instance, "owner", owner)
        return 0.1

    def __call__(self, *, bar: KeyType = None, **kwargs: Any) -> ResultType:
        self.set_properties(**kwargs)
        return self.__getitem__(bar)

    def __getitem__(self, key: KeyType) -> ResultType:
        if self.is_ready and isinstance(self.data_buffer, list):
            match key:
                case None:
                    return None
                case int() if 0 <= key < self.len_dataset:
                    return self.data_buffer[key]
                case slice():
                    start: int = key.start if key.start is not None else 0
                    stop: int = key.stop if key.stop is not None else self.len_dataset

                    if 0 <= start < stop <= self.len_dataset:
                        return self.data_buffer[start:stop]
                case _:
                    raise IndexError(f"{__name__}: неверный индекс: {key}")

    def __setitem__(self, key: KeyType, value: ResultType) -> None:
        if not isinstance(key, int | slice) or not isinstance(value, float):
            raise TypeError(f"{__name__}: неверный тип индекса")

        print(f"{__name__}: нет возможности вносить изменения в данные")

    def __delitem__(self, key: KeyType) -> None:
        if not isinstance(key, int | slice):
            raise TypeError(f"{__name__}: неверный тип индекса")

        print(f"{__name__}: нет возможности удалить данные")

    def set_properties(self, **kwargs: Any) -> None:
        if kwargs != {}:
            for key in kwargs:
                if key in self.__dict__:
                    # print(f"{key = }")
                    self.__dict__[key] = kwargs[key]
                else:
                    _key = "_" + key
                    if _key in self.__dict__:
                        #print(f"{_key = }")
                        self.__dict__[_key] = kwargs[key]

    def get_indicator(self) -> None:  # TODO:
        ...

    @abstractmethod
    def calculate(self, *args: Any, **kwargs: Any) -> ResultType:
        ...
