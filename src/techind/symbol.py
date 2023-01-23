class Symbol:  # (Enum):  # StrEnum
    """Symbol.
    """

    # _slots_ = "_symbol"

    EURUSD = "EURUSD"
    GBPUSD = "GBPUSD"
    CHFUSD = "CHFUSD"

    def __init__(self, symbol: str) -> None:
        self._symbol = symbol

    @property
    def symbol(self) -> str:
        print("@symbol.getter")
        return self._symbol

    @symbol.setter
    def symbol(self, value: str) -> None:
        print("@symbol.setter")
        if not isinstance(value, str):
            raise TypeError("dmdmdmdmdmd")

        self._symbol = value
