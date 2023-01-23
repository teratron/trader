from typing import Optional


class Symbol:  # (Enum):  # StrEnum
    """Symbol.
    """

    _slots_ = "_symbol"

    EURUSD = "EURUSD"
    GBPUSD = "GBPUSD"
    CHFUSD = "CHFUSD"

    def __init__(self, symbol: Optional[str]) -> None:
        self._symbol = symbol

    @property
    def symbol(self) -> Optional[str]:
        return self._symbol

    @symbol.setter
    def symbol(self, value: str) -> None:
        self._symbol = value
