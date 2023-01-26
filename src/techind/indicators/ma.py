from typing import Optional

from techind.indicator import Indicator, DatasetType, ResultType, BarType, DataType, moving_average
from techind.properties.method import Method
from techind.properties.period import Period
from techind.properties.price import Price


class Properties(Period, Method, Price):
    """Properties.
    """

    # slots: Union[list[str], str] = [
    #     Period.slots,
    #     "_method",
    #     "_price"
    # ]

    def __init__(self, *, period: int = 7, method: int = Method.SMA, price: int = Price.CLOSE) -> None:
        Period.__init__(self, period)
        Method.__init__(self, method)
        Price.__init__(self, price)


class MA(Indicator, Properties):
    """Moving Average.

    Class `MA`:

    * MA(dataset=[])
    * MA(dataset=[], period=24, method=0, price=0)

    Instance `ma = MA()`:

    * ma
    * ma[42]
    * ma[:42]
    * ma()
    * ma(period=24, method=0, price=0, bar=42)
    * ma(period=24, method=0, price=0, bar=slice(0, 42))

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

    name = "ma"
    type = "MA"
    description = __doc__

    def __init__(self, /, dataset: DatasetType, **kwargs: int) -> None:
        super().__init__(dataset)
        self.properties(**kwargs)
        self.buffer: Optional[list[Optional[float]]] = None

    def properties(self, **kwargs: int) -> None:
        Properties.__init__(self, **kwargs)

    def calculate(self, bar: BarType = None) -> ResultType:
        data: DataType = []
        match bar:
            case None:
                return None
            case int() if not isinstance(self.dataset, float | None) and 0 <= bar < len(self.dataset):
                data = self.dataset[bar:bar + self.period]
            case slice():
                data = self.dataset[bar.start:bar.stop + self.period - 1]
            case _:
                raise IndexError("Неверный индекс")

        print("calculate", self.dataset, bar, data)
        return moving_average(data, self.period)


if __name__ == "__main__":
    data_series: DatasetType = [0.0, 1.0, 2.0, 3.0, 4.0, 5.0, 7.0]

    ma = MA(data_series, period=4, method=3)
    # ma = MA(data_series)
    print(ma, ma.__dict__)

    print(ma(period=3, method=1, price=3, bar=3))
    print(ma(period=5, method=3, price=2))
    print(ma(bar=slice(1, 3)))
    print(ma())
    print(ma[2])
    # print(ma[:2])

    # ma1[2] = 9.61
    # print(ma1[2])
    print(ma.__dict__)
    # ma.period = 123
    # print(ma.__dict__)
    # print(ma1.name)
    # ma1.symbol = "CHFUSD"
    # print(ma.slots)

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
