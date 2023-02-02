# @overload
# def __call__(self, *, bar: KeyType = ..., **kwargs: Any) -> ResultType:
#     ...
#
# @overload
# def __call__(self, *, period: int = ..., method: int = ..., price: int = ..., bar: KeyType = ...) -> ResultType:
#     ...


# class Properties(ABC):
#     """Properties.
#     """
#
#     @abstractmethod
#     def __init__(self, **kwargs: Any) -> None:
#         ...


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


# def __setitem__(self, key: KeyType, value: float) -> None:
#     if not isinstance(key, int):
#         raise TypeError("Индекс должен быть целым числом")
#
#     if key < 0:
#         raise IndexError("Индекс должен быть неотрицательным числом")
#
#     match self.dataset:
#         case list():
#             if key >= self.len_dataset:
#                 off = key + 1 - self.len_dataset
#                 self.dataset.extend([None] * off)
#
#             self.dataset[key] = value
#         case _:
#             raise TypeError("Буфер индикатора не соответствует необходимому типу данных")


# def __delitem__(self, key: KeyType) -> None:
#     if not isinstance(key, int):
#         raise TypeError("Индекс должен быть целым числом")
#     if isinstance(self.dataset, list):
#         del self.dataset[key]


# properties: tuple[type, ...] | None = None
# def __init_subclass__(cls, **kwargs: Any):
#     props = tuple(filter(lambda x: x.__name__ != Indicator.__name__, cls.__bases__))
#     if props:
#         Indicator.properties = props


# class Slot:
#     slots: Union[list[str], str] = "_period"
#     def __init_subclass__(cls, **kwargs: Any) -> None:
#         _slots = [Period.slots]
#         _slots.extend(cls.slots)
#         print("__init_subclass__:Period", cls, cls.slots, _slots, kwargs)


# print([i.__dict__ for i in MA.__bases__[MA.__bases__.index(MA.__base__) + 1:]])


# if kwargs != {}:
#     for key in kwargs:
#         if key in self.__dict__:
#             self.__dict__[key] = kwargs[key]
#         else:
#             _key = "_" + key
#             if _key in self.__dict__:
#                 self.__dict__[_key] = kwargs[key]


# Period
# def __init__(self, period: int) -> None:
#     # self._period: int = Period._check(period)
#     # self.period: int = Period._check(period)
#     self.__dict__["period"]: int = Period._check(period)
#     # self.__dict__.setdefault("period", 3)
#
# @property
# def period(self) -> int:
#     # return self._period
#     # return self.period
#     return self.__dict__["period"]
#
# @period.setter
# def period(self, value: int) -> None:
#     # self._period = Period._check(value)
#     # self.period = Period._check(value)
#     self.__dict__["period"] = Period._check(value)


# Method
# def __init__(self, /, method: int, period: int) -> None:
#     super().__init__(period)
#     # self._method: int = Method._check(method)
#     self.__dict__["method"]: int = Method._check(method)
#     self.__dict__.setdefault("method", Method.SMA)
#
# @property
# def method(self) -> int:
#     # return self._method
#     return self.__dict__["method"]
#
# @method.setter
# def method(self, value: int) -> None:
#     # self._method = Method._check(value)
#     self.__dict__["method"] = Method._check(value)


# Price
# def __init__(self, price: int) -> None:
#     # self._price: int = Price._check(price)
#     self.__dict__["price"]: int = Price._check(price)
#     self.__dict__.setdefault("price", Price.CLOSE)
#
# @property
# def price(self) -> int:
#     # return self._price
#     return self.__dict__["price"]
#
# @price.setter
# def price(self, value: int) -> None:
#     # self._price = Price._check(value)
#     self.__dict__["price"] = Price._check(value)
