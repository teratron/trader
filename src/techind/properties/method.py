class Method:
    """Method.

    * SMA -- Простое усреднение / Simple Moving Average (0).
    * EMA -- Экспоненциальное усреднение / Exponential Moving Average (1).
    * SMMA -- Сглаженное усреднение / Smoothed Moving Average (2).
    * LWMA -- Линейно-взвешенное усреднение / Linear Weighted Moving Average (3).
    """

    SMA = 0
    """Простое усреднение."""

    EMA = 1
    """Экспоненциальное усреднение."""

    SMMA = 2
    """Сглаженное усреднение."""

    LWMA = 3
    """Линейно-взвешенное усреднение."""

    slots: str = "_method"

    def __init__(self, method: int) -> None:
        self._method = Method.check(method)

    @property
    def method(self) -> int:
        return self._method

    @method.setter
    def method(self, value: int) -> None:
        self._method = self.check(value)

    @classmethod
    def check(cls, value: int) -> int:
        if cls.SMA <= value <= cls.LWMA:
            return value
        else:
            raise ValueError("")  # TODO: add text exception
