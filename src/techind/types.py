from enum import IntEnum

from typing import Union, Sequence


class Mode(IntEnum):
    PriceType = 0
    MethodType = 1


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


OHLCType = tuple[float, float, float, float]
BarType = tuple[int, float, float, float, float, int, int, int]
TickType = tuple[int, float, float, float, int, int, int, float]

DataSeriesType = Union[
    # list[float],
    # list[tuple[float, float, float, float]],  # OHLC Data
    # list[tuple[int, float, float, float, float, int, int, int]],  # Bar Data
    # list[tuple[int, float, float, float, int, int, int, float]],  # Tick Data
    Sequence[Union[OHLCType, BarType, TickType, float]],
    None
]

BufferType = Union[
    list[float],
    list[list[float | int | bool]],
    list[tuple[int, float, ...]],  # (time, value, ...)
    None
]

ResultType = Union[
    float,
    list[float],
    list[tuple[float, ...]],
    list[tuple[int, float, ...]],  # (time, value, ...)
    tuple[float, ...],
    tuple[int, float, ...],  # (time, value, ...)
    None
]

DataType = Sequence[float | int]
KeyType = int | slice | None
