from techind.ma import MA


class MACD(MA):
    """Moving Average Convergence Divergence.

    MACD — это технический индикатор, позволяющий оценивать силу тренда и построенный
    с учетом усредненного изменения цены.

    int iMACD(
        string              symbol,              // имя символа
        ENUM_TIMEFRAMES     period,              // период
        int                 fast_ema_period,     // период быстрой средней
        int                 slow_ema_period,     // период медленной средней
        int                 signal_period,       // период усреднения разности
        ENUM_APPLIED_PRICE  applied_price        // тип цены или handle
    );
    """

    name = "Moving Average Convergence Divergence"
    type = "MACD"
    description = __doc__

    print("MACD")

    fast_ema = MA()
    slow_ema = MA()

    def __init__(
            self,
            symbol: str,
            timeframe: int = 1,
            *,
            period: int = 14,
            method: int = 0,
            price: int = 0,
            shift: int = 0,
            bar: int = 0
    ) -> None:
        print("__init__:MACD")

        super().__init__()
        self.symbol = symbol
        self.timeframe = timeframe
        self.period = period
        self.method = method
        self.price = price
        self.shift = shift
        self.bar = bar


if __name__ == "__main__":
    # ma = MACD([1.32, 2.7, 3.92])
    ma = MACD("EURUSD")
    # print(ma(43))
    # print(ma[2])
    # ma[2] = 9.61
    # print(ma[2])

    print("macd")
