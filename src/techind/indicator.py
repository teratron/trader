from abc import ABC, abstractmethod

from typing import Any

from techind.types import DataSeriesType, BufferType, ResultType, KeyType


class Indicator(ABC):
    """Indicator.
    """

    dataset: DataSeriesType = None
    buffer: BufferType = None
    len_dataset: int = 0

    def __init__(self, /, dataset: DataSeriesType, **kwargs: Any) -> None:
        self.dataset = dataset

        if isinstance(self.dataset, list):
            self.len_dataset = len(self.dataset)

    def __call__(self, *, bar: KeyType = None, **kwargs: Any) -> ResultType:
        self.set_properties(**kwargs)
        return self.__getitem__(bar)

    def __getitem__(self, key: KeyType) -> ResultType:
        valid: bool = False
        match key:
            case None:
                return None
            case int():
                valid = 0 <= key < self.len_dataset
            case slice():
                start: int = key.start if key.start is not None else 0
                stop: int = key.stop if key.stop is not None else self.len_dataset
                valid = 0 <= start < stop <= self.len_dataset

        if valid:
            return self.calculate(bar=key)

        raise IndexError("Неверный индекс")

    def __setitem__(self, key: KeyType, value: ResultType) -> None:
        if not isinstance(key, KeyType) or not isinstance(value, ResultType):
            raise TypeError("Неверный тип индекса")

        print("Нет возможности вносить изменения в данные")

    def __delitem__(self, key: KeyType) -> None:
        if not isinstance(key, KeyType):
            raise TypeError("Неверный тип индекса")

        print("Нет возможности удалять данные")

    def set_properties(self, **kwargs: Any) -> None:
        if kwargs != {}:
            for key in kwargs:
                if key in self.__dict__:
                    # print("****", _key, kwargs[key], self.__dict__)
                    self.__dict__[key] = kwargs[key]
                else:
                    _key = "_" + key
                    if _key in self.__dict__:
                        self.__dict__[_key] = kwargs[key]

        # def asf(_key):
        #     if _key in self.__dict__:
        #         self.__dict__[_key] = kwargs[key]

    @abstractmethod
    def calculate(self, *args: Any, **kwargs: Any) -> ResultType:
        ...
