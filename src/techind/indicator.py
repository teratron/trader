from abc import ABC, abstractmethod
from typing import Any

from techind.properties.price import Price
from techind.types import DataSeriesType, BufferType, ResultType, KeyType, ValueType


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
                match self.data_series[0]:
                    case float():
                        self.data_buffer = self.data_series[:]
                    case tuple() as ds if ds is ValueType:
                        # self.data_buffer: list[float]
                        for row in self.data_series:
                            match row:
                                case tuple():  # if row is OHLCType:
                                    # if row is tuple[float, ...]:
                                    self.data_buffer.append(self.get_price(*row[1:5]))  # TODO: OHLC
                                case _:
                                    raise ValueError(f"{__name__}: данные не определены")
                    case _:
                        raise ValueError(f"{__name__}: данные не определены")

                if self.len_dataset == len(self.data_buffer):
                    self.calculate()
                    self.is_ready = True
        else:
            raise TypeError(f"{__name__}: ")  # TODO:

    def __get__(self, instance, owner) -> None:
        print("instance", instance, "owner", owner)
        return None

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
                    self.__dict__[key] = kwargs[key]
                else:
                    _key = "_" + key
                    if _key in self.__dict__:
                        self.__dict__[_key] = kwargs[key]

    def get_indicator(self) -> None:  # TODO:
        ...

    @abstractmethod
    def calculate(self, *args: Any, **kwargs: Any) -> ResultType:
        ...
