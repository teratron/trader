from techind.indicator import Indicator
from techind.properties.method import Method
from techind.properties.price import Price
from techind.types import ResultType, KeyType, DataSeriesType


class TMPL(Indicator, Method):
    """Template.

    1. Различный Price
    2. Различный Method
    4. Различный Period
    """

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
        return 1


if __name__ == "__main__":
    data_series: DataSeriesType = [0.0, 1.0, 2.0, 3.0, 4.0, 5.0, 7.0]
    tmpl = TMPL(data_series, period=4, method=0)
    print(tmpl.__dict__)
    print(tmpl(period=3, method=1, price=3, bar=3))
    print(tmpl.__dict__)
    print(tmpl(period=5, method=3, price=2))
    print(tmpl.__dict__)
    # print(tmpl(bar=slice(1, 3)))
    # print(tmpl.__dict__)
    # print(tmpl())
    # print(tmpl.__dict__)
    # print(tmpl[2])
    # print(tmpl.__dict__)
    # print(tmpl[:2])
    # print(tmpl.__dict__)
    # tmpl.method = 0
    # print(tmpl.__dict__)
    # tmpl[2] = 9.61
    # print(tmpl.__dict__)
    # del tmpl[1]
