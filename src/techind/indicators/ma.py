from techind.indicator import Indicator
from techind.properties.method import Method
from techind.properties.price import Price
from techind.types import DataSeriesType, KeyType, ResultType, DataType


class MA(Indicator, Method):  # Price Period
    """Moving Average.

    Class `MA`:

    * MA(data_series=[]) -- создаёт экземпляр индикатора и рассчитывает переданные данные с параметрами по умолчанию.
    * MA([], period=24, method=2, price=0) -- тоже самое, что выше, но с заданными параметрами.

    Instance `ma = MA()`:

    * ma
    * ma[42] -- возвращает значение индикатора в определённом баре.
    * ma[:42] -- тоже самое, что выше, но возвращает срез баров.
    * ma() -- пересчитывает все значения индикатора с заданными ранее параметрами.
    * ma(period=24, method=0) -- тоже самое, что выше, но параметры задаются непосредственно аргументами.
    * ma(bar=42) -- вычисляет и заменяет значение индикатора для заданного бара.
    * ma(method=0, price=0, bar=42) -- тоже самое, что выше, но с заданными параметрами.
    * ma(period=24, bar=slice(0, 42)) -- тоже самое, что выше, но с заданными параметрами и для среза баров.

    int iMA(
        string               symbol,            // имя символа
        ENUM_TIMEFRAMES      period,            // период
        int                  ma_period,         // период усреднения
        int                  ma_shift,          // смещение индикатора по горизонтали
        ENUM_MA_METHOD       ma_method,         // тип сглаживания
        ENUM_APPLIED_PRICE   applied_price      // тип цены или handle
    );
    """

    __slots__ = ("_period", "_method", "_price")

    def __init__(
            self,
            /,
            dataset: DataSeriesType,
            *,
            period: int = 3,
            method: int = Method.SMA,
            price: int = Price.CLOSE
    ) -> None:
        Method.__init__(self, method, period)
        super().__init__(dataset, price)

    def calculate(self, *, bar: KeyType = None) -> ResultType:
        # print(self.data_buffer)
        # if isinstance(self.data_buffer, list):
        #     if isinstance(self.data_buffer[0], float):
        data: DataType = self.data_buffer
        self.data_buffer = self.moving_average(data)
        # self.data_buffer.extend([None] * (self.len_dataset - len(self.data_buffer)))
        # print(self.data_buffer)
        # print("ma", list(map(lambda x: round(x, 6), self.moving_average(self.data_buffer))))

        return None


if __name__ == "__main__":
    # from techind.dataset import eurusd_rates
    #
    # if isinstance(eurusd_rates, list):
    #     ma = MA(eurusd_rates, period=2, method=MA.EMA, price=MA.TYPICAL)
    #     # print(ma)
    #     ma.period = 5
    #     print(ma.__dict__)

    # from techind.data import test_rates
    # if isinstance(test_rates, list):
    #     ma = MA(test_rates, period=3, method=0, price=0)

    data_series: DataSeriesType = [0.0, 1.0, 2.0, 3.0, 4.0, 5.0, 7.0]
    ma = MA(data_series, period=4, method=0)
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
    ma.method = 0
    print(ma.__dict__)
    ma[2] = 9.61
    print(ma.__dict__)
    del ma[1]

    print("+++", ma)
