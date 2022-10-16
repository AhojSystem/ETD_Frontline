import text_print
from itertools import zip_longest


class TextLayout:
    def __init__(self, win, max_height, max_width, color, y, x):
        self.__window = win
        self.__max_height = max_height
        self.__max_width = max_width
        self.__color = color
        self.default_y = y
        self.y = y
        self.x = x

        self.__strings = []
        self.__colors = []
        self.__yx = []
        self.__max_parts = 1
        self.__max_lens = []

    def add_string(self, strs: list[str], color=None, xy=None):
        self.__strings.append(strs)
        self.__max_parts = max(self.__max_parts, len(strs))
        self.__max_lens = [max(len(i), j) for i, j in zip_longest(strs, self.__max_lens, fillvalue=0)]

        if color is not None:
            assert len(color) == 1 or len(color) == len(strs), f"Too many or too few colors"
            self.__colors.append(color)
        else:
            self.__colors.append(self.__color)

        if xy is not None:
            self.__yx.append(xy)
        else:
            self.__yx.append((self.y, self.x))
            self.y += 1

    def print(self):
        for line, color, yx in zip(self.__strings, self.__colors, self.__yx):
            text = "".join([txt + " " * (max_len - len(txt)) for txt, max_len in zip(line, self.__max_lens)])
            text_print.text_print(self.__window, yx[0], yx[1], self.__max_height, self.__max_width, text, color)

    def clear(self):
        self.__strings = []
        self.__colors = []
        self.__yx = []
        self.y = self.default_y
        self.__max_parts = 1
        self.__max_lens = []
