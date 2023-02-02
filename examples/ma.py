import matplotlib.pyplot as plt
import pandas as pd
from pandas.plotting import register_matplotlib_converters

from techind.dataset import eurusd_rates
from techind.indicators.ma import MA


def main() -> None:
    register_matplotlib_converters()

    if isinstance(eurusd_rates, list):
        frame_eurusd = pd.DataFrame(eurusd_rates)
        # print(frame_eurusd)

        plt.plot(frame_eurusd[0], frame_eurusd[1], 'r-o', label='open')
        plt.plot(frame_eurusd[0], frame_eurusd[2], 'g-o', label='high')
        plt.plot(frame_eurusd[0], frame_eurusd[3], 'y-o', label='low')
        plt.plot(frame_eurusd[0], frame_eurusd[4], 'b-o', label='close')

        # Moving Average
        ma = MA(eurusd_rates, period=4, method=MA.LWMA, price=MA.CLOSE)

        if ma:
            frame_buffer = pd.DataFrame(ma.data_buffer)
            # print(frame_buffer)

            plt.plot(frame_eurusd[0], frame_buffer[0], 'black', label='ma')

        plt.title(f'EURUSD: Period: {ma.period}, Method: {ma.method}, Price: {ma.price}')
        plt.legend(loc='upper left')
        plt.show()


if __name__ == "__main__":
    main()
