from typing import Optional, Any

from techind.indicator import Indicator, Result, moving_average


class Properties:
    """Properties.
    """

    # _slots_ = (
    #     "period",
    #     "method",
    #     "price",
    #     "shift",
    #     # "bar"
    # )

    # props = {
    #     "period":  14,
    #     "method": 0,
    #     "price": 0,
    #     "shift": 0
    # }

    # period: int
    # method: int
    # price: int
    # shift: int

    def __init__(
            self,
            # *args,
            *,
            period: int = 14,
            method: int = 0,
            price: int = 0,
            shift: int = 0
    ) -> None:
        print("__init__:Properties")
        self._period = period
        self.method = method
        self.price = price
        self.shift = shift

    @property
    def period(self) -> int:
        return self._period

    @period.setter
    def period(self, value: int) -> None:
        if 0 < value < 1000:
            self._period = value
        else:
            raise ValueError("d,dd,d")

    # super().__init__(self.__dict__)

    # def __getitem__(self, key: Any) -> Any:
    #     return self.__dict__[key]

    # self.props2 = self.props.pop("props")
    # super().__init__()

    # print("dir", self.props.pop("props"))

    # def __dir__(self) -> Iterable[str]:
    #     print(self)


class MA(Indicator, Properties):
    """Moving Average.

    Class `MA`:
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

    # Indicator._slots_.extend(Properties._slots_)
    # print(Indicator._slots_)
    # __slots__ = tuple(Indicator._slots_)

    # __slots__ = (
    #     "period",
    #     "method",
    #     "price",
    #     "shift",
    #     # "bar"
    # )

    name = "Moving Average"
    type = "MA"
    description = __doc__
    buffer: Optional[list[float]] = None
    bar: int = 0

    def __init__(
            self,
            # /,
            # symbol: Optional[str]=None,
            # timeframe: int=Indicator.TIMEFRAME_H1,
            *args: Ellipsis,  # [str, int],
            **kwargs: Any
            # *,
            # period: int = 14,
            # method: int = 0,
            # price: int = 0,
            # shift: int = 0
    ) -> None:
        # print("__init__:MA", self, args, kwargs)
        # super().__init__(symbol, timeframe)
        super().__init__(*args)
        Properties.__init__(self, **kwargs)
        # self.period = period
        # self.method = method
        # self.price = price
        # self.shift = shift
        # self.props = self.__dir__()
        # print("pr", self.props)

        # self.props = self.__dict__

        # self.__slots__ = (
        #     "period",
        #     "method",
        #     "price",
        #     "shift",
        #     "bar"
        # )

        # super(MA, self).__init__()

    # def _get_props(self, d):
    #     a = d.pop("props")
    #     print("a", a)
    #     return a

    def __call__(
            self,
            # *,
            # period: int = 14,
            # method: int = 0,
            # price: int = 0,
            # shift: int = 0,
            *,
            bar: int = 0,
            **kwargs,
    ) -> Result:
        print("__call__:Indicator", kwargs)
        print("kwargs", self.__dict__)
        Properties.__init__(self, **kwargs)
        self.bar = bar

        return self.calculate(bar=bar)

    def calculate(self, *, bar: Optional[int] = None) -> Result:
        print(self.dataset)
        if bar is not None:
            return moving_average(self.dataset[bar:bar + self.period], self.period)

        return None


if __name__ == "__main__":
    ma1 = MA(MA.TIMEFRAME_H1, "EURUSD", period=3, method=0)
    print(ma1(period=7, method=1, price=3, shift=0))
    # print(ma1[2])
    # ma1[2] = 9.61
    # print(ma1[2])
    print(ma1.__dict__)
    ma1.symbol = "CHFUSD"

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
