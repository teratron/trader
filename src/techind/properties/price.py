# from typing import Union, NamedTuple
#
# BarPriceType = Union[
#     float,
#     list[float]
# ]
#
#
# class OHLCType(NamedTuple):
#     open_price: float
#     high_price: float
#     low_price: float
#     close_price: float
#
#
# class BidAskType(NamedTuple):
#     bid_price: float
#     ask_price: float


class Price:
    """Price - тип цены.

    Ценовые константы:

    * CLOSE -- Цена закрытия (0).
    * OPEN -- Цена открытия (1).
    * HIGH -- Максимальная за период цена (2).
    * LOW -- Минимальная за период цена (3).
    * MEDIAN -- Медианная цена (4).
    * TYPICAL -- Типичная цена (5).
    * WEIGHTED -- Взвешенная цена закрытия (6).
    """

    CLOSE: int = 0
    """Цена закрытия."""

    OPEN: int = 1
    """Цена открытия."""

    HIGH: int = 2
    """Максимальная за период цена."""

    LOW: int = 3
    """Минимальная за период цена."""

    MEDIAN: int = 4
    """Медианная цена."""

    TYPICAL: int = 5
    """Типичная цена."""

    WEIGHTED: int = 6
    """Взвешенная цена закрытия."""

    BID: int = 7
    """Цена покупки."""

    ASK: int = 8
    """Цена продажи."""

    def __init__(self, price: int) -> None:
        self._price: int = Price.check(price)

    @property
    def price(self) -> int:
        print("get price")
        return self._price

    @price.setter
    def price(self, value: int) -> None:
        print("set price")
        self._price = Price.check(value)

    @classmethod
    def check(cls, value: int) -> int:
        if cls.CLOSE <= value <= cls.WEIGHTED:
            return value
        raise ValueError(f"{__name__}: константа цены не соответствует существующим значениям")

    def get_price(self, *prices: float) -> float:
        print(prices)
        return get_price(self._price, *prices)


def get_price(
        price_mode: int,
        open_price: float,
        high_price: float,
        low_price: float,
        close_price: float
) -> float:
    """Формирование цены."""
    match price_mode:
        case Price.OPEN:
            return open_price
        case Price.HIGH:
            return high_price
        case Price.LOW:
            return low_price
        case Price.MEDIAN:
            return get_median(high_price, low_price)
        case Price.TYPICAL:
            return get_typical(high_price, low_price, close_price)
        case Price.WEIGHTED:
            return get_weighted(high_price, low_price, close_price)
        case Price.CLOSE | _:
            return close_price


def get_price_tick(
        price_mode: int,
        bid_price: float,
        ask_price: float
) -> float:
    """Формирование цены для тика."""
    match price_mode:
        case Price.ASK:
            return ask_price
        case Price.MEDIAN:
            return get_median(bid_price, ask_price)
        case Price.BID | _:
            return bid_price


def get_median(high_price: float, low_price: float) -> float:
    """Медианная цена.

    `MEDIAN = (high + low) / 2`
    """
    return (high_price + low_price) / 2


def get_typical(high_price: float, low_price: float, close_price: float) -> float:
    """Типичная цена.

    `TYPICAL = (high + low + close) / 3`
    """
    return (high_price + low_price + close_price) / 3


def get_weighted(high_price: float, low_price: float, close_price: float) -> float:
    """Взвешенная цена закрытия.

    `WEIGHTED = (high + low + close + close) / 4`
    """
    return (high_price + low_price + close_price * 2) / 4
