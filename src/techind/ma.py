from typing import Any, Optional

from techind.indicator import Indicator, Result, moving_average


class Properties:
    """Properties.
    """

    _slots_ = (
        "period",
        "method",
        "price",
        "shift",
        # "bar"
    )

    # props = {
    #     "period":  14,
    #     "method": 0,
    #     "price": 0,
    #     "shift": 0
    # }

    props: dict[str, Any] = {}

    def __init_subclass__(cls, **kwargs: Any) -> None:
        print("__init_subclass__:Indicator", cls, kwargs)
        # super().__init_subclass__(**kwargs)

    def __init__(
            self,
            *,
            period: int = 14,
            method: int = 0,
            price: int = 0,
            shift: int = 0
    ) -> None:
        self.period = period
        self.method = method
        self.price = price
        self.shift = shift
        self.props = self.__dict__
        # self.props2 = self.props.pop("props")
        # super().__init__()

        # print("dir", self.props.pop("props"))

    # def __dir__(self) -> Iterable[str]:
    #     print(self)


class MA(Indicator, Properties):
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
    * ma[:42]
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

    # _slots_ = list(Indicator._slots_).extend(list(Properties._slots_))
    # a = Indicator._slots_
    Indicator._slots_.extend(Properties._slots_)
    print(Indicator._slots_)

    # __slots__ = tuple(Indicator._slots_)

    name = "Moving Average"
    type = "MA"
    description = __doc__
    buffer: Optional[list[float]] = None

    # print(Properties.__dict__)

    print("dir", Properties.props)

    def __init__(self, *args, **kwargs) -> None:
        print("__init__:MA", self, args, kwargs)

        super().__init__(*args)
        Properties.__init__(self, **kwargs)

        # self.props = self.__dict__

        # self.__slots__ = (
        #     "period",
        #     "method",
        #     "price",
        #     "shift",
        #     "bar"
        # )

        # super(MA, self).__init__()

    def __call__(
            self,
            **kwargs
            # period: int = 14,
            # method: int = 0,
            # price: int = 0,
            # shift: int = 0
    ) -> Any:
        print("__call__:Indicator")
        print("kwargs", kwargs)
        # print(self.props)
        # print(MA.__slots__)
        # print(self.__slots__)

        return None

    def calculate(self, *, bar: Optional[int] = None) -> Result:
        if bar is not None:
            return moving_average(self.dataset[bar:bar + self.period], self.period)

        return None


if __name__ == "__main__":
    # ma = MA(ind.EURUSD, ind.TIMEFRAME_M1)
    # ma = MA()
    # print(ma(42))

    ma1 = MA("EURUSD", 1, period=3, )
    print(ma1(period=7, method=1, price=3))
    print(ma1[2])
    # ma1[2] = 9.61
    # print(ma1[2])
    # print(ma1.ma)
    #print(ma1(period=7, method=0, price=0, id=33))

    # ma2 = MA([1, 2, 3], period=24, method=0, price=0, shift=0)
    # print(ma2.dataset)
    #
    # ma3 = MA("EURUSD", 1)
    # print(ma3.dataset)
    #
    # ma4 = MA("EURUSD", timeframe=1, period=24, method=0, price=0, shift=0)
    #
    # ma5 = MA(period=24, method=0, price=0, shift=0)

    # print("-")

    # pr = Properties()
    #print(pr.__dict__)
