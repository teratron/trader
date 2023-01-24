from typing import Union


class Price:
    """Price.
    """

    slots: Union[list[str], str] = "_price"

    def __init__(self, price: int) -> None:
        self._price = price

    @property
    def price(self) -> int:
        return self._price

    @price.setter
    def price(self, value: int) -> None:
        if 0 < value < 1000:
            self._price = value
        else:
            raise ValueError("")
