from techind.types import DataType


class Method:
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

    def __init__(self, method: int) -> None:
        self._method: int = _check(method)

    @property
    def method(self) -> int:
        return self._method

    @method.setter
    def method(self, value: int) -> None:
        self._method = _check(value)

    def moving_average(self, data: DataType, period: int) -> list[float]:
        return moving_average(data, period, mode=self._method)


def _check(value: int) -> int:
    if Method.SMA <= value <= Method.LWMA:
        return value
    else:
        raise ValueError("Константа метода не соответствует существующим значениям")


def moving_average(
        data: DataType,
        period: int,
        *,
        mode: int = Method.SMA
) -> list[float]:
    """Скользящая средняя."""
    if period > len(data):
        raise ValueError("Период превышает длину массива")

    if not isinstance(data, list):
        data = list(data)

    match mode:
        case Method.EMA:
            return _get_ema(data, period)
        case Method.SMMA:
            return _get_smma(data, period)
        case Method.LWMA:
            return _get_lwma(data, period)
        case Method.SMA | _:
            return _get_sma(data, period)


def _get_sma(data: DataType, period: int) -> list[float]:
    """Простое усреднение.

    `SMA = sum(price(i), n) / n`
    """
    length: int = len(data) - period + 1
    return [
        sum(data[i:i + period]) / period
        for i in range(length)
    ]


def _get_ema(_data: DataType, _period: int) -> list[float]:
    """Экспоненциальное усреднение.

    `EMA = price(i) * p + ema(i - 1) * (100 - p)`
    """
    return [0.0]


def _get_smma(_data: DataType, _period: int) -> list[float]:
    """Сглаженное усреднение.

    `SMMA(0) = sum(price(i), n) / n`
    `SMMA = (sum(price(i), n) - smma(i - 1) + price(i)) / n`
    """
    return [0.0]


def _get_lwma(data: DataType, period: int) -> list[float]:
    """Линейно-взвешенное усреднение.

    `LWMA = sum(price(i) * i, n) / sum(i, n)`
    """
    length: int = len(data) - period + 1
    array: list[float] = [0.0] * length

    for i in range(length):
        n = 0
        for y in range(i, i + period):
            z = y + 1
            n += z
            array[i] += data[y] * z

        array[i] /= n

    return array

# print(_get_sma([0.0, 1.0, 2.0, 3.0, 4.0, 5.0, 7.0], 7))
