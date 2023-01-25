class Method:
    """Method.
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
        self._method = self.check(method)

    @property
    def method(self) -> int:
        return self._method

    @method.setter
    def method(self, value: int) -> None:
        self._method = self.check(value)

    def check(self, value: int) -> int:
        if self.SMA <= value <= self.LWMA:
            return value
        else:
            raise ValueError("")  # TODO: add text exception
