from techind.indicator import Indicator as ind  # , Symbol, Timeframe


class MA(ind):
    """
    Moving Average.

    Class MA:
    * MA()
    * MA(dataset[:])
    * MA(dataset[:], period=24, method=0, shift=0)
    * MA(symbol="EURUSD", timeframe=1)
    * MA(symbol="EURUSD", timeframe=1, period=24, method=0, shift=0)

    Instance ma = MA():
    * ma
    * ma[42]
    * ma(period=24, method=0, shift=0)
    * ma(period=24, method=0, shift=0)[42]
    """

    name = "Moving Average"
    type = "MA"
    description = __doc__

    def __subclasscheck__(self, subclass):
        print("__subclasscheck__:MA", subclass)

    def __init__(self, *args, **kwargs) -> None:
        print("__init__:MA", self.name)

        super().__init__(*args)
        #self.dataset = dataset


if __name__ == "__main__":
    # ma = MA(ind.EURUSD, ind.TIMEFRAME_M1)
    ma = MA("EURUSD", 1)

    """

    """

    print(ma(42))
