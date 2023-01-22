from typing import Any, Optional, overload


class Market:
    symbol: str = "EURUSD"
    timeframe: int = 1

    @overload
    def __init__(self, /, symbol: str, timeframe: int, **kwargs: Any) -> None:
        ...

    @overload
    def __init__(self, dataset: Optional[list[Any]], **kwargs: Any) -> None:
        ...

    def __init__(self, /, symbol: str, timeframe: int = 1, **kwargs: Any) -> None:
        super().__init__(**kwargs)
        self.symbol = symbol
        self.timeframe = timeframe

    # def __init__(self, dataset: Optional[list[Any]] = None, **kwargs: Any) -> None:
    #     super().__init__(**kwargs)
    #     self.dataset = dataset
