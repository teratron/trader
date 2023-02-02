from typing import Union, Sequence, Any

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

# _BT = TypeVar("BT", int, float, float, float, float, int, int, int)
# print(BT, Type[BT])
# BT = NewType("BT", tuple[int, float, float, float, float, int, int, int])
# print(BT, Type[BT])

OHLCType = tuple[float, float, float, float]
BarType = tuple[int, float, float, float, float, int, int, int]
TickType = tuple[int, float, float, float, int, int, int, float]

DataSeriesType = Union[
    list[float],
    list[tuple[float, float, float, float]],  # OHLC Data
    list[tuple[int, float, float, float, float, int, int, int]],  # Bar Data
    list[tuple[int, float, float, float, int, int, int, float]],  # Tick Data
    # Sequence[Union[OHLCType, BarType, TickType, float]],
    None
]

BufferType = Union[
    list[float | None],
    # list[tuple[int, float]],
    list[tuple[Any, ...]],
    list[list[float | int | bool]],
    None
]

ResultType = Union[
    float,
    list[float | None],
    list[tuple[Any, ...]],
    tuple[Any, ...],
    None
]

DataType = Sequence[float | int]
KeyType = int | slice | None
