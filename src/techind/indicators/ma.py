from typing import Optional

from techind.indicator import Indicator, Result, moving_average
from techind.properties.method import Method
from techind.properties.period import Period
from techind.properties.price import Price
from techind.properties.shift import Shift


class Properties(Period, Method, Price, Shift):
    """Properties.
    """

    # slots: Union[list[str], str] = [
    #     Period.slots,
    #     "_method",
    #     "_price",
    #     "_shift"
    # ]

    def __init__(
            self,
            *,
            period: int = 7,
            method: int = 0,
            price: int = 0,
            shift: int = 0
    ) -> None:
        Period.__init__(self, period)
        Method.__init__(self, method)
        Price.__init__(self, price)
        Shift.__init__(self, shift)


class MA(Indicator, Properties):
    """Moving Average.

    Class `MA`:
    * MA("EURUSD", timeframe=1)
    * MA("EURUSD", timeframe=1, period=24, method=0, price=0, shift=0)

    Instance `ma = MA()`:
    * ma
    * ma[42]
    * ma[35:42]
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

    # __slots__ = tuple(Indicator._slots_)

    name = "Moving Average"
    type = "MA"
    description = __doc__

    def __init__(self, /, symbol: str, timeframe: int, **kwargs: int) -> None:
        super().__init__(symbol, timeframe)
        Properties.__init__(self, **kwargs)
        self.buffer: Optional[list[float]] = None

    def __call__(self, *, bar: int = 0, **kwargs: int) -> Result:
        print("__call__", kwargs, bar)
        Properties.__init__(self, **kwargs)

        return self.calculate(bar=bar)

    def calculate(self, *, bar: int = 0) -> Result:
        print(self.dataset, bar)
        if bar is not None and isinstance(self.dataset, slice):
            return moving_average(self.dataset[bar:bar + self.period], self.period)

        return None

    # @property
    # def bar(self) -> int:
    #     return self._bar
    #
    # @bar.setter
    # def bar(self, value: int) -> None:
    #     if 0 <= value < 1000:
    #         self._bar = value
    #     else:
    #         raise ValueError("")


if __name__ == "__main__":
    ma = MA("EURUSD", MA.TIMEFRAME_H1, period=3, method=0)
    print(ma)
    print(ma(period=3, method=1, price=3, shift=0, bar=1))
    print(ma[2])
    # ma1[2] = 9.61
    # print(ma1[2])
    # print(ma1.__dict__)
    # ma1.name = "123"
    # print(ma1.name)
    # ma1.symbol = "CHFUSD"
    print(ma.slots)

    # pr = Properties()
    # print(pr, pr["period"])

    # ma2 = MA("EURUSD", Indicator.TIMEFRAME_H1, period=3, method=0)
    # ma3 = MA("EURUSD", Indicator.TIMEFRAME_H1, period=3, method=0)
    # print(ma2.name, ma3.name, MA.name)
    #
    # ma2.name = "123"
    # print(ma2.name, ma3.name, MA.name)
    #
    # MA.name = "987"
    # print(ma2.name, ma3.name, MA.name)
