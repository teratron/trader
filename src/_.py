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
#
#     if isinstance(self.dataset, list):
#         del self.dataset[key]


# properties: tuple[type, ...] | None = None
# def __init_subclass__(cls, **kwargs: Any):
#     props = tuple(filter(lambda x: x.__name__ != Indicator.__name__, cls.__bases__))
#     if props:
#         Indicator.properties = props


# class Slot:
#     slots: Union[list[str], str] = "_period"
#
#     def __init_subclass__(cls, **kwargs: Any) -> None:
#         _slots = [Period.slots]
#         _slots.extend(cls.slots)
#         print("__init_subclass__:Period", cls, cls.slots, _slots, kwargs)
