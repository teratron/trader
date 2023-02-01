from techind.indicator import Indicator
from techind.properties.method import Method
from techind.properties.price import Price
from techind.types import DataSeriesType, ResultType, KeyType


class MA(Indicator, Method, Price):  # Period,
    """Moving Average.

    Class `MA`:

    * MA(data_series=[])
    * MA(data_series=[], period=24, method=0, price=0)

    Instance `ma = MA()`:

    * ma
    * ma[42]
    * ma[:42]
    * ma()
    * ma(period=24, method=0, price=0, bar=42)
    * ma(period=24, method=0, price=0, bar=slice(0, 42))
    """

    # __slots__ = ("_period", "_method", "_price")

    def __init__(
            self,
            /,
            dataset: DataSeriesType = None,
            *,
            period: int = 3,
            method: int = Method.SMA,
            price: int = Price.CLOSE
    ) -> None:
        Method.__init__(self, period, method)
        Price.__init__(self, price)

        if dataset is not None:
            super().__init__(dataset)

    def calculate(self, *, bar: KeyType = None) -> ResultType:
        if bar is None:
            if self.data_buffer is None:
                self.data_buffer = []

            if isinstance(self.data_series, list):
                for row in self.data_series:  # TODO:
                    match row:
                        case tuple():
                            # if isinstance(row, BarType):
                            self.data_buffer.append(self.get_price(*row[1:5]))
                        case float():
                            self.data_buffer = self.data_series[:]
                            break

                print(self.data_buffer)
                self.data_buffer = self.moving_average(self.data_buffer)
                self.data_buffer.extend([None] * (self.len_dataset - len(self.data_buffer)))
                print(self.data_buffer)
                # print("ma", list(map(lambda x: round(x, 6), self.moving_average(self.data_buffer))))

        # else:
        #     match bar:
        #         case int():
        #             data = self.data_series[bar:bar + self.period]
        #         case slice():
        #             data = self.data_series[bar.start:bar.stop + self.period - 1]
        #         case _:
        #             raise IndexError("Неверный индекс")

        # print("calculate", self.data_series, bar, data)
        # return self.moving_average(data, self.period)
        return None


if __name__ == "__main__":
    from techind.dataset import eurusd_rates

    if isinstance(eurusd_rates, list):
        ma = MA(eurusd_rates, period=2, method=Method.SMMA, price=Price.WEIGHTED)
        # print(ma)
        print(ma.__dict__)

    # from techind.data import test_rates
    # if isinstance(test_rates, list):
    #     ma = MA(test_rates, period=3, method=0, price=0)

    # data_series: DataSeriesType = [0.0, 1.0, 2.0, 3.0, 4.0, 5.0, 7.0]
    # ma = MA(data_series, period=4, method=0)
    # print(ma.__dict__)
    # print(ma(period=3, method=1, price=3, bar=3))
    # print(ma.__dict__)
    # print(ma(period=5, method=3, price=2))
    # print(ma.__dict__)
    # print(ma(bar=slice(1, 3)))
    # print(ma.__dict__)
    # print(ma())
    # print(ma.__dict__)
    # print(ma[2])
    # print(ma.__dict__)
    # print(ma[:2])
    # print(ma.__dict__)
    # ma.method = 0
    # print(ma.__dict__)
    # ma[2] = 9.61
    # print(ma.__dict__)
    # del ma[1]
