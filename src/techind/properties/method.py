from typing import Union


class Method:
    """Method.
    """

    slots: Union[list[str], str] = "_method"

    def __init__(self, method: int) -> None:
        self._method = method

    @property
    def method(self) -> int:
        return self._method

    @method.setter
    def method(self, value: int) -> None:
        if 0 < value < 1000:
            self._method = value
        else:
            raise ValueError("")
