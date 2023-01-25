class Expert:
    """
    Class `Expert`:
    * Expert("EURUSD", timeframe=1)
    """

    name = "expert"
    type = "Expert"
    description = __doc__

    def __init__(self, /, symbol: str, timeframe: int, *, shift: int = 0) -> None:
        super().__init__(symbol, timeframe, shift)
        # Symbol.__init__(self, symbol)
        # Timeframe.__init__(self, timeframe)
        # Shift.__init__(self, shift)
