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
        print("method:__init__")
        self._method = Method.check(method)

    @property
    def method(self) -> int:
        return self._method

    @method.setter
    def method(self, value: int) -> None:
        self._method = self.check(value)

    @classmethod
    def check(cls, value: int) -> int:
        print("method:check")
        if cls.SMA <= value <= cls.LWMA:
            return value
        else:
            raise ValueError("")  # TODO: add text exception
