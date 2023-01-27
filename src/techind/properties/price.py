class Price:
    """Price.

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

    slots: str = "_price"

    def __init__(self, price: int) -> None:
        self._price = Price.check(price)

    @property
    def price(self) -> int:
        return self._price

    @price.setter
    def price(self, value: int) -> None:
        self._price = self.check(value)

    @classmethod
    def check(cls, value: int) -> int:
        if cls.CLOSE <= value <= cls.WEIGHTED:
            return value
        else:
            raise ValueError("")  # TODO: add text exception

    # def get_price(self, ohlc: tuple[float, float, float, float]) -> float:
    # def get_price(self, *ohlc: float) -> float:
    def get_price(self, /, price_open: float, price_high: float, price_low: float, price_close: float) -> float:
        # print(self._price, price_open, price_high, price_low, price_close)
        """
        ohlc:
        0     1     2    3
        open, high, low, close
        """
        match self._price:
            case Price.CLOSE:
                return price_close
            case Price.OPEN:
                return price_open
            case Price.HIGH:
                return price_high
            case Price.LOW:
                return price_low
            case Price.MEDIAN:
                return Price.get_median(price_high, price_low)
            case Price.TYPICAL:
                return Price.get_typical(price_high, price_low, price_close)
            case Price.WEIGHTED:
                return Price.get_weighted(price_high, price_low, price_close)

    @staticmethod
    def get_median(price_high: float, price_low: float) -> float:
        return (price_high + price_low) / 2

    @staticmethod
    def get_typical(price_high: float, price_low: float, price_close: float) -> float:
        return (price_high + price_low + price_close) / 3

    @staticmethod
    def get_weighted(price_high: float, price_low: float, price_close: float) -> float:
        return (price_high + price_low + price_close * 2) / 4
