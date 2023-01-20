class Timeframe:  # (IntEnum):
    # TICK = 0
    # TIMEFRAME_M1 = 1
    # TIMEFRAME_M5 = 2
    # TIMEFRAME_M15 = 3
    # TIMEFRAME_M30 = 4
    # TIMEFRAME_H1 = 5
    # TIMEFRAME_H4 = 6
    # TIMEFRAME_D1 = 7
    # TIMEFRAME_Y1 = 8

    TICK = 0
    M1 = 1
    M5 = 2
    M15 = 3
    M30 = 4
    H1 = 5
    H4 = 6
    D1 = 7
    Y1 = 8

    # @classmethod
    # def __getattr__(cls, item):
    #     return cls[item].value

    @classmethod
    def __call__(cls, item):
        return cls[item].value

# print(Timeframe["M1"])
# print(Timeframe["TIMEFRAME_M1"])
