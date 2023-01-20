from datetime import datetime

import MetaTrader5 as mt5

from techind.ma import MA

if __name__ == "__main__":
    if not mt5.initialize():
        print("initialize failed")
    else:
        print(mt5.version())
        print(mt5.terminal_info())

        euraud_ticks = mt5.copy_ticks_from("EURAUD", datetime(2020, 1, 28, 13), 1000, mt5.COPY_TICKS_ALL)
        audusd_ticks = mt5.copy_ticks_range("AUDUSD", datetime(2020, 1, 27, 13), datetime(2020, 1, 28, 13),
                                            mt5.COPY_TICKS_ALL)

        eurusd_rates = mt5.copy_rates_from("EURUSD", mt5.TIMEFRAME_M1, datetime(2022, 12, 28, 13), 1000)
        eurgbp_rates = mt5.copy_rates_from_pos("EURGBP", mt5.TIMEFRAME_M1, 0, 1000)
        eurcad_rates = mt5.copy_rates_range("EURCAD", mt5.TIMEFRAME_M1, datetime(2020, 1, 27, 13),
                                            datetime(2020, 1, 28, 13))

        print('euraud_ticks(', len(euraud_ticks), ')')
        for val in euraud_ticks[:10]:
            print(val)

        print('audusd_ticks(', len(audusd_ticks), ')')
        for val in audusd_ticks[:10]:
            print(val)

        print('eurusd_rates(', len(eurusd_rates), ')')
        for val in eurusd_rates[:10]:
            print(val)

        print('eurgbp_rates(', len(eurgbp_rates), ')')
        for val in eurgbp_rates[:10]:
            print(val)

        print('eurcad_rates(', len(eurcad_rates), ')')
        for val in eurcad_rates[:10]:
            print(val)

    mt5.shutdown()

    ma = MA()
    print(ma)
