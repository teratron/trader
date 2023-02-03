class Symbol:
    """Symbol.
    """

    EURUSD = "EURUSD"
    GBPUSD = "GBPUSD"
    CHFUSD = "CHFUSD"

    slots: str = "_symbol"

    def __init__(self, symbol: str) -> None:
        self._symbol = symbol

    @property
    def symbol(self) -> str:
        return self._symbol

    @symbol.setter
    def symbol(self, value: str) -> None:
        if not isinstance(value, str):
            raise TypeError(f"{__name__}: ")

        self._symbol = value
