class Price:
    """Price.
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
        self._price = self.check(price)

    @property
    def price(self) -> int:
        return self._price

    @price.setter
    def price(self, value: int) -> None:
        self._price = self.check(value)

    def check(self, value: int) -> int:
        if self.CLOSE <= value <= self.WEIGHTED:
            return value
        else:
            raise ValueError("")  # TODO: add text exception
