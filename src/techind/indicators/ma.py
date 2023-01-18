from typing import Any, Optional, Union


from techind.indicator import Indicator


class MA(Indicator):
    """
    Moving Average.

    Class `MA`:

    * MA()
    * MA(dataset[:])
    * MA(dataset[:], period=24, method=0, price=0, shift=0)
    * MA("EURUSD", timeframe=1)
    * MA("EURUSD", timeframe=1, period=24, method=0, price=0, shift=0)

    Instance `ma = MA()`:

    * ma
    * ma[42]
    * ma(period=24, method=0, price=0, shift=0)
    * ma(period=24, method=0, price=0, shift=0)[42]
    """

    name = "Moving Average"
    type = "MA"
    description = __doc__
    #dataset = []
    symbol = ""
    # timeframe = 1

    def __subclasscheck__(self, subclass: Any) -> None:
        print("__subclasscheck__:MA", subclass)

    def __init__(
            self,
            reader: Union[list[Any], str, None] = None,
            timeframe: int = 1,
            # *args: tuple[Union[Optional[list[Any]], str], Any],
            # dataset: Optional[list[Any]] = None,
            # symbol: str = "",
            # timeframe: int = 1,
            *,
            period: int = 14,
            method: int = 0,
            price: int = 0,
            shift: int = 0
    ) -> None:
        print("__init__:MA", reader)

        match reader:
            case list() as dataset:
                super().__init__(dataset)
                self.dataset = dataset
                print('dataset', dataset)
            case str() as symbol:
                self.symbol: str = symbol
                print('symbol', symbol)
        #     case int() as timeframe:
        #         self.timeframe: int = timeframe
        #         print('timeframe', timeframe)

        # self.dataset = dataset
        # self.symbol = symbol
        self.timeframe = timeframe

        # self.dataset = args[0]
        # self.symbol = args[0]
        # self.timeframe = args[1]

        self.period: int = period
        self.method: int = method
        self.price: int = price
        self.shift: int = shift


if __name__ == "__main__":
    # ma = MA(ind.EURUSD, ind.TIMEFRAME_M1)

    ma = MA()
    ma1 = MA([1, 2, 3])
    ma2 = MA([1, 2, 3], period=24, method=0, price=0, shift=0)
    print(ma2.dataset)
    ma3 = MA("EURUSD", 1)
    print(ma3.dataset)
    ma4 = MA("EURUSD", timeframe=1, period=24, method=0, price=0, shift=0)

    #print(ma(42))
