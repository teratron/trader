from enum import IntEnum
from typing import Union

from techind.indicator import DataType, ResultType


class MethodMode(IntEnum):
    """MethodMode.

    Усреднённые константы:

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


MethodType = Union[MethodMode, int]


class Method:
    """Method.
    """

    slots: str = "_method"

    def __init__(self, method: MethodMode) -> None:
        self._method: MethodMode = _check(method)

    @property
    def method(self) -> MethodMode:
        return self._method

    @method.setter
    def method(self, value: MethodMode) -> None:
        self._method = _check(value)

    def moving_average(self, data: DataType, period: int) -> ResultType:
        return moving_average(data, period, mode=self._method)


def _check(value: MethodMode) -> MethodMode:
    if MethodMode.SMA <= value <= MethodMode.LWMA:
        return value
    else:
        raise ValueError("")  # TODO: add text exception


def moving_average(data: DataType, period: int, *, mode: MethodMode = MethodMode.SMA) -> ResultType:
    """Скользящая средняя."""
    length = len(data)
    if period > length:
        print(f"Период `{period=}` превышает длину массива `{length=}`")
        return None
    elif period == length:
        return sum(data) / period

    if not isinstance(data, list):
        data = list(data)

    match mode:
        case MethodMode.SMA:
            return _get_sma(data, period)
        case MethodMode.EMA:
            return _get_ema(data, period)
        case MethodMode.SMMA:
            return _get_smma(data, period)
        case MethodMode.LWMA:
            return _get_lwma(data, period)

    return None


def _get_sma(data: DataType, period: int) -> ResultType:
    """Простое усреднение.

    SMA = SUM(CLOSE(i), N) / N
    """
    length = len(data) - period + 1
    return [
        sum(data[i:period + i]) / period
        for i in range(length)
    ]


def _get_ema(_data: DataType, _period: int) -> ResultType:
    """Экспоненциальное усреднение.

    EMA = CLOSE(i) * P + EMA(i - 1) * (100 - P)
    """
    return 0.0


def _get_smma(_data: DataType, _period: int) -> ResultType:
    """Сглаженное усреднение.

    SMMA(0) = SUM(CLOSE(i), N) / N; SMMA = (SUM(CLOSE(i), N) - SMMA(i - 1) + CLOSE(i)) / N
    """
    return 0.0


def _get_lwma(data: DataType, period: int) -> ResultType:
    """Линейно-взвешенное усреднение.

    LWMA = SUM(CLOSE(i) * i, N) / SUM(i, N)
    """
    length = len(data) - period + 1
    # for i in range(length):
    #     y = i + 1
    #     z = data[i:period + i] * y

    return [
        sum(data[i:period + i]) / period
        for i in range(length)
    ]
