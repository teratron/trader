from typing import Union, Sequence, TypeVar, Type, NewType

# class Mode(IntEnum):
#     PriceType = 0
#     MethodType = 1


# class OHLCType(NamedTuple):
#     open_price: float
#     high_price: float
#     low_price: float
#     close_price: float


# class BarType(NamedTuple):
#     time: int
#     open_price: float
#     high_price: float
#     low_price: float
#     close_price: float
#     tick_volume: int
#     spread: int
#     real_volume: int


# class TickType(NamedTuple):
#     time: int
#     ask: float
#     bid: float
#     a: float
#     tick_volume: int
#     spread: int
#     real_volume: int
#     b: float

_BT = TypeVar("BT", int, float, float, float, float, int, int, int)

# print(BT, Type[BT])

OHLCType = tuple[float, float, float, float]
BarType = tuple[int, float, float, float, float, int, int, int]
TickType = tuple[int, float, float, float, int, int, int, float]

BT = NewType("BT", tuple[int, float, float, float, float, int, int, int])
print(BT, Type[BT])

DataSeriesType = Union[
    # list[float],
    # list[tuple[float, float, float, float]],  # OHLC Data
    # list[tuple[int, float, float, float, float, int, int, int]],  # Bar Data
    # list[tuple[int, float, float, float, int, int, int, float]],  # Tick Data
    Sequence[Union[OHLCType, BarType, TickType, float]],
    None
]

BufferType = Union[
    list[float | None],
    list[tuple[int, float]],
    list[list[float | int | bool]],
    None
]

ResultType = Union[
    float,
    list[float],
    list[tuple[float, ...]],
    tuple[float, ...],
    None
]

DataType = Sequence[float | int]
KeyType = int | slice | None
