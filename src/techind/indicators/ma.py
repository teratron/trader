from typing import Any, Optional, Union


#from techind.indicator import Indicator


#class MA(Indicator):
from techind.market import Market


class MA(Market):
    """
    Moving Average.

    Class `MA`:

    * MA()
    * MA(dataset[:])
    * MA(dataset[:], period=24, method=0, price=0, shift=0)
    * MA("EURUSD", timeframe=1)
    * MA("EURUSD", timeframe=1, period=24, method=0, price=0, shift=0)
    * MA(period=24, method=0, price=0, shift=0)

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
            reader: Union[list[Any], str, None] = None,
            timeframe: int = 1,
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
            case str() as symbol:
                self.symbol: str = symbol

        self.timeframe = timeframe
        self.period: int = period
        self.method: int = method
        self.price: int = price
        self.shift: int = shift


if __name__ == "__main__":
    # ma = MA(ind.EURUSD, ind.TIMEFRAME_M1)

    # ma = MA()
    # print(ma(42))

    ma1 = MA([1.32, 2.7, 3.92])
    print(ma1(43))
    print(ma1[2])
    ma1[2] = 9.61
    print(ma1[2])

    # ma2 = MA([1, 2, 3], period=24, method=0, price=0, shift=0)
    # print(ma2.dataset)
    #
    # ma3 = MA("EURUSD", 1)
    # print(ma3.dataset)
    #
    # ma4 = MA("EURUSD", timeframe=1, period=24, method=0, price=0, shift=0)
    #
    # ma5 = MA(period=24, method=0, price=0, shift=0)
