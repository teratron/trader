class Symbol:
    """Symbol.
    """

    slots = "_symbol"

    EURUSD = "EURUSD"
    GBPUSD = "GBPUSD"
    CHFUSD = "CHFUSD"

    def __init__(self, symbol: str) -> None:
        self._symbol = symbol

    @property
    def symbol(self) -> str:
        return self._symbol

    @symbol.setter
    def symbol(self, value: str) -> None:
        if not isinstance(value, str):
            raise TypeError("")

        self._symbol = value
