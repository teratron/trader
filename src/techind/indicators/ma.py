from typing import Any, Optional, Union

from techind.indicator import Indicator as ind  # , Symbol, Timeframe


class MA:  # (ind)
    """
    Moving Average.

    Class `MA`:

    * MA()
    * MA(dataset[:])
    * MA(dataset[:], period=24, method=0, price=0, shift=0)
    * MA(symbol="EURUSD", timeframe=1)
    * MA(symbol="EURUSD", timeframe=1, period=24, method=0, price=0, shift=0)

    Instance `ma = MA()`:

    * ma
    * ma[42]
    * ma(period=24, method=0, price=0, shift=0)
    * ma(period=24, method=0, price=0, shift=0)[42]
    """

    name = "Moving Average"
    type = "MA"
    description = __doc__

    def __subclasscheck__(self, subclass: Any) -> None:
        print("__subclasscheck__:MA", subclass)

    def __init__(
            self,
            /,
            dataset: Union[list[Any], tuple[str, Any], None] = None,
            # symbol: str = "",
            # timeframe: int = 1,
            *,
            period: int = 24,
            method: int = 0,
            price: int = 0,
            shift: int = 0
    ) -> None:
        print("__init__:MA")
        #super().__init__(*dataset)

        # match dataset:
        #     case "":
        #         pass

        self.dataset = dataset
        # self.symbol = symbol
        # self.timeframe = timeframe

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
    ma4 = MA("EURUSD", 1)

    #print(ma(42))
