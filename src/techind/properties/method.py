class Method:
    """Method.
    """

    SMA = 0
    """Простое усреднение"""

    EMA = 1
    """Экспоненциальное усреднение"""

    SMMA = 2
    """Сглаженное усреднение"""

    LWMA = 3
    """Линейно-взвешенное усреднение"""

    slots: str = "_method"

    def __init__(self, method: int) -> None:
        self._method = method

    @property
    def method(self) -> int:
        return self._method

    @method.setter
    def method(self, value: int) -> None:
        if Method.SMA <= value <= Method.LWMA:
            self._method = value
        else:
            raise ValueError("")
