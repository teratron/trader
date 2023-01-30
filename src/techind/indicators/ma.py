from techind.indicator import Indicator, DataSeriesType, ResultType, KeyType, DataType, BarType
from techind.properties.method import Method
from techind.properties.period import Period
from techind.properties.price import Price


class MA(Indicator, Period, Method, Price):
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

    # __slots__ = ("_period", "_method", "_price")

    def __init__(
            self,
            /,
            dataset: DataSeriesType,
            *,
            period: int = 7,
            method: int = Method.SMA,
            price: int = Price.CLOSE
    ) -> None:
        super().__init__(dataset)
        Period.__init__(self, period)
        Method.__init__(self, method)
        Price.__init__(self, price)
        # self.properties(period=period, method=method, price=price)

        pr = []
        # for i in range(self.len_dataset):
        #     pr.append(round(self.get_price(*self.dataset[i][1:5]), 6))

        if isinstance(self.dataset, list):
            for d in self.dataset:
                # print(d, type(d))
                if d is BarType:
                    pr.append(round(self.get_price(*d[1:5]), 6))

        # print(pr)
        # maa = moving_average(pr, self.period)  # : list[float | None]
        # maa.extend([None] * 2)
        # print(maa)

    def calculate(self, *, bar: KeyType = None) -> ResultType:
        if self.buffer is None:
            pass

        data: DataType = []
        match bar:
            case None:
                return None
            case int():
                data = self.dataset[bar:bar + self.period]

            case slice():
                data = self.dataset[bar.start:bar.stop + self.period - 1]
            case _:
                raise IndexError("Неверный индекс")

        print("calculate", self.dataset, bar, data)
        return self.moving_average(data, self.period)


if __name__ == "__main__":
    # from techind.data import eurusd_rates
    #
    # if isinstance(eurusd_rates, list):
    #     ma = MA(eurusd_rates, period=3, method=0, price=PriceMode.WEIGHTED)
    #     # ta = MA(test_rates, period=3, method=0, price=0)
    #
    #     print(ma.__dict__)

    data_series: DataSeriesType = [0.0, 1.0, 2.0, 3.0, 4.0, 5.0, 7.0]

    ma = MA(data_series, period=4, method=3)
    print(ma)
    print(ma.__dict__)

    print(ma(period=3, method=1, price=3, bar=3))
    print(ma.__dict__)
    print(ma(period=5, method=3, price=2))
    print(ma.__dict__)
    print(ma(bar=slice(1, 3)))
    print(ma.__dict__)
    print(ma())
    print(ma.__dict__)
    print(ma[2])
    print(ma.__dict__)
    print(ma[:2])
    print(ma.__dict__)
    ma[2] = 9.61
    print(ma.__dict__)
    ma.method = 0
    print(ma.__dict__)
