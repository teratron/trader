from techind.properties.period import Period
from techind.types import DataType


class Method(Period):
    """Method.

    Усреднённые константы:

    * SMA -- Простое усреднение / Simple Moving Average (0).
    * EMA -- Экспоненциальное усреднение / Exponential Moving Average (1).
    * SMMA -- Сглаженное усреднение / Smoothed Moving Average (2).
    * LWMA -- Линейно-взвешенное усреднение / Linear Weighted Moving Average (3).
    """

    SMA: int = 0
    """Простое усреднение."""

    EMA: int = 1
    """Экспоненциальное усреднение."""

    SMMA: int = 2
    """Сглаженное усреднение."""

    LWMA: int = 3
    """Линейно-взвешенное усреднение."""

    def __init__(self, /, method: int, period: int = 3) -> None:
        self._method: int = Method._check(method)
        super().__init__(period)

    @property
    def method(self) -> int:
        return self._method

    @method.setter
    def method(self, value: int) -> None:
        self._method = Method._check(value)

    @classmethod
    def _check(cls, value: int) -> int:
        if cls.SMA <= value <= cls.LWMA:
            return value
        else:
            raise ValueError("Константа метода не соответствует существующим значениям")

    def moving_average(self, dataset: DataType) -> list[float]:
        return moving_average(dataset, period=self._period, method=self._method)


def moving_average(dataset: DataType, *, period: int = 3, method: int = Method.SMA) -> list[float]:
    """Скользящая средняя."""
    if period > len(dataset):
        raise ValueError("Период превышает длину массива")

    if not isinstance(dataset, list):
        dataset = list(dataset)

    match method:
        case Method.EMA:
            return _get_ema(dataset, period)
        case Method.SMMA:
            return _get_smma(dataset, period)
        case Method.LWMA:
            return _get_lwma(dataset, period)
        case Method.SMA | _:
            return _get_sma(dataset, period)


def _get_sma(dataset: DataType, period: int) -> list[float]:
    """Простое усреднение.

    `SMA = sum(price(i), n) / n`
    """
    return [
        sum(dataset[i:i + period]) / period
        for i in range(len(dataset) - period + 1)
    ]


def _get_ema(dataset: DataType, period: int) -> list[float]:
    """Экспоненциальное усреднение.

    `p = 2 / (n + 1)`
    `EMA(0) = sum(price(i), n) / n`
    `EMA = price(i) * p + ema(i - 1) * (1 - p)`
    """
    factor: float = 2.0 / (period + 1)
    delta: float = 1 - factor
    array: list[float] = []
    array.extend(_get_sma(dataset[:period], period))

    for i in range(1, len(dataset) - period + 1):
        array.append(dataset[i] * factor + array[i - 1] * delta)

    return array


def _get_smma(dataset: DataType, period: int) -> list[float]:
    """Сглаженное усреднение.

    `SMMA(0) = sum(price(i), n) / n`
    `SMMA = (sum(price(i), n) - smma(i - 1) + price(i)) / n`
    """
    array: list[float] = []
    array.extend(_get_sma(dataset[:period], period))

    for i in range(1, len(dataset) - period + 1):
        n = 0.0
        for j in range(i, i + period):
            n += dataset[j]
        array.append((n - array[i - 1] + dataset[i]) / period)

    return array


def _get_lwma(dataset: DataType, period: int) -> list[float]:
    """Линейно-взвешенное усреднение.

    `LWMA = sum(price(i) * i, n) / sum(i, n)`
    """
    array: list[float] = []

    for i in range(len(dataset) - period + 1):
        n = 0
        m = 0.0
        for j in range(i, i + period):
            k = j + 1
            n += k
            m += dataset[j] * k
        array.append(m / n)

    return array

# if __name__ == "__main__":
#   print(_get_smma([0.0, 1.0, 2.0, 3.0, 4.0, 5.0, 6.0], 3))
#   print(_get_lwma([0.0, 1.0, 2.0, 3.0, 4.0, 5.0, 6.0], 3))
