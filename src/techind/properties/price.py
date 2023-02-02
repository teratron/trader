from dataclasses import dataclass


@dataclass
class PriceMode:
    """Mode - тип цены.

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


class Price(PriceMode):
    """Price.
    """

    def __init__(self, price: int) -> None:
        self._price: int = Price._check(price)

    @property
    def price(self) -> int:
        return self._price

    @price.setter
    def price(self, value: int) -> None:
        self._price = Price._check(value)

    @classmethod
    def _check(cls, value: int) -> int:
        if cls.CLOSE <= value <= cls.WEIGHTED:
            return value
        else:
            raise ValueError("Константа цены не соответствует существующим значениям")

    def get_price(self, *bar: float) -> float:
        return get_price(*bar, price=self._price)


def get_price(
        open_price: float,
        high_price: float,
        low_price: float,
        close_price: float,
        *,
        price: int = Price.CLOSE
) -> float:
    """Формирование цены."""
    match price:
        case Price.OPEN:
            return open_price
        case Price.HIGH:
            return high_price
        case Price.LOW:
            return low_price
        case Price.MEDIAN:
            return _get_median(high_price, low_price)
        case Price.TYPICAL:
            return _get_typical(high_price, low_price, close_price)
        case Price.WEIGHTED:
            return _get_weighted(high_price, low_price, close_price)
        case Price.CLOSE | _:
            return close_price


def _get_median(high_price: float, low_price: float) -> float:
    """Медианная цена.

    `MEDIAN = (high + low) / 2`
    """
    return (high_price + low_price) / 2


def _get_typical(high_price: float, low_price: float, close_price: float) -> float:
    """Типичная цена.

    `TYPICAL = (high + low + close) / 3`
    """
    return (high_price + low_price + close_price) / 3


def _get_weighted(high_price: float, low_price: float, close_price: float) -> float:
    """Взвешенная цена закрытия.

    `WEIGHTED = (high + low + close + close) / 4`
    """
    return (high_price + low_price + close_price * 2) / 4
