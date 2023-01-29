from enum import IntEnum
from typing import NamedTuple

PriceType = float


class OHLCType(NamedTuple):
    open_price: float
    high_price: float
    low_price: float
    close_price: float


class PriceMode(IntEnum):
    """PriceMode.

    Ценовые константы:

    * CLOSE -- Цена закрытия (0).
    * OPEN -- Цена открытия (1).
    * HIGH -- Максимальная за период цена (2).
    * LOW -- Минимальная за период цена (3).
    * MEDIAN -- Медианная цена, `(high+low)/2` (4).
    * TYPICAL -- Типичная цена, `(high+low+close)/3` (5).
    * WEIGHTED -- Взвешенная цена закрытия, `(high+low+close+close)/4` (6).
    """

    CLOSE = 0
    """Цена закрытия."""

    OPEN = 1
    """Цена открытия."""

    HIGH = 2
    """Максимальная за период цена."""

    LOW = 3
    """Минимальная за период цена."""

    MEDIAN = 4
    """Медианная цена, `(high+low)/2`."""

    TYPICAL = 5
    """Типичная цена, `(high+low+close)/3`."""

    WEIGHTED = 6
    """Взвешенная цена закрытия, `(high+low+close+close)/4`."""


class Price:
    """Price.
    """

    slots: str = "_price"

    def __init__(self, price: PriceMode) -> None:
        # super().__init__(0.123)
        self._price = Price._check(price)

    @property
    def price(self) -> PriceMode:
        return self._price

    @price.setter
    def price(self, value: PriceMode) -> None:
        self._price = self._check(value)

    @staticmethod
    def _check(value: PriceMode) -> PriceMode:
        if PriceMode.CLOSE <= value <= PriceMode.WEIGHTED:
            return value
        else:
            raise ValueError("")  # TODO: add text exception

    def get_price(
            self,
            /,
            bar: OHLCType
    ) -> PriceType:
        # return get_price(open_price, high_price, low_price, close_price, self._price)
        return get_price(*bar, mode=self._price)


def get_price(
        open_price: PriceType,
        high_price: PriceType,
        low_price: PriceType,
        close_price: PriceType,
        *,
        mode: PriceMode = PriceMode.CLOSE
) -> PriceType:
    print("mode", mode)
    match mode:
        case PriceMode.CLOSE:
            return close_price
        case PriceMode.OPEN:
            return open_price
        case PriceMode.HIGH:
            return high_price
        case PriceMode.LOW:
            return low_price
        case PriceMode.MEDIAN:
            return _get_median(high_price, low_price)
        case PriceMode.TYPICAL:
            return _get_typical(high_price, low_price, close_price)
        case PriceMode.WEIGHTED:
            return _get_weighted(high_price, low_price, close_price)


def _get_median(high_price: float, low_price: float) -> PriceType:
    return (high_price + low_price) / 2


def _get_typical(high_price: float, low_price: float, close_price: float) -> PriceType:
    return (high_price + low_price + close_price) / 3


def _get_weighted(high_price: float, low_price: float, close_price: float) -> PriceType:
    return (high_price + low_price + close_price * 2) / 4
