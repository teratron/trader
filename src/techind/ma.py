from typing import Any, Union

from techind.indicator import Indicator


# from techind.market import Market
# class MA(Market):


class MA(Indicator):
    """Moving Average.

    Class `MA`:
    * MA()
    * MA(dataset[:])
    * MA(dataset[:], period=24, method=0, price=0, shift=0)
    * MA("EURUSD", timeframe=1)
    * MA("EURUSD", timeframe=1, period=24, method=0, price=0, shift=0)

    Instance `ma = MA()`:
    * ma
    * ma[42]
    * ma(period=24, method=0, price=0, shift=0, bar=42)

    int iMA(
        string               symbol,            // имя символа
        ENUM_TIMEFRAMES      period,            // период
        int                  ma_period,         // период усреднения
        int                  ma_shift,          // смещение индикатора по горизонтали
        ENUM_MA_METHOD       ma_method,         // тип сглаживания
        ENUM_APPLIED_PRICE   applied_price      // тип цены или handle
    );
    """

    name = "Moving Average"
    type = "MA"
    description = __doc__

    print("MA")

    def __init__(
            self,
            reader: Union[list[Any], str, None] = None,
            timeframe: int = 1,
            *,
            period: int = 14,
            method: int = 0,
            price: int = 0,
            shift: int = 0,
            bar: int = 0
    ) -> None:
        print("__init__:MA", self)

        match reader:
            case list() as dataset:
                super().__init__(dataset)
                self.dataset = dataset
            case str() as symbol:
                self.symbol = symbol

        self.timeframe = timeframe
        self.period = period
        self.method = method
        self.price = price
        self.shift = shift
        self.bar = bar
        self.ma = self

        #super(MA, self).__init__()

    def calc(self, bar: int) -> float:
        print("calc:MA", self, bar)
        return 42.2568


if __name__ == "__main__":
    # ma = MA(ind.EURUSD, ind.TIMEFRAME_M1)
    # ma = MA()
    # print(ma(42))

    ma1 = MA([1.32, 2.7, 3.92])
    #print(ma1(43))
    print(ma1[2])
    #ma1[2] = 9.61
    #print(ma1[2])
    #print(ma1.ma)

    # ma2 = MA([1, 2, 3], period=24, method=0, price=0, shift=0)
    # print(ma2.dataset)
    #
    # ma3 = MA("EURUSD", 1)
    # print(ma3.dataset)
    #
    # ma4 = MA("EURUSD", timeframe=1, period=24, method=0, price=0, shift=0)
    #
    # ma5 = MA(period=24, method=0, price=0, shift=0)

    #print("-")
