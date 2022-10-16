class CursesColor:
    def __init__(self, red: int, green: int, blue: int) -> None:
        self.__red = red
        self.__green = green
        self.__blue = blue

    @property
    def red(self) -> int:
        return self.__red

    @property
    def green(self) -> int:
        return self.__green

    @property
    def blue(self) -> int:
        return self.__blue

    def __setattr__(self, key, value):
        assert isinstance(value, int), "Only integer can be assigned."
        assert 0 <= value <= 10 ** 3, "Only values between 0 to 1000 can be assigned."
        object.__setattr__(self, key, value)
