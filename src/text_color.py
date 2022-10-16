import curses

from curses_color import CursesColor


class TextColor:
    def __init__(self):
        curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_BLACK)
        self.__default_color = curses.color_pair(1)

        curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_BLACK)
        self.__player = curses.color_pair(2)

        curses.init_pair(3, curses.COLOR_YELLOW, curses.COLOR_BLACK)
        self.__goal = curses.color_pair(3)

        curses.init_pair(4, curses.COLOR_BLACK, curses.COLOR_BLACK)
        self.__no_color = curses.color_pair(4)

        self.__defined_color = dict()
        self.__defined_color_pair = dict()
        self.__color_counter = 16
        self.__color_pair_counter = 5

    @property
    def default_color(self):
        return self.__default_color

    @property
    def player_color(self):
        return self.__player

    @property
    def goal_color(self):
        return self.__goal

    @property
    def no_color(self):
        return self.__no_color

    def set_color(self, color_name: str, color: CursesColor) -> None:
        assert color_name not in self.__defined_color, f"color {color_name} is already exist"
        curses.init_color(self.__color_counter, color.red, color.green, color.blue)
        self.set_curses_color(color_name=color_name, curses_color=self.__color_counter)

    def set_curses_color(self, color_name: str, curses_color) -> None:
        assert color_name not in self.__defined_color, f"color {color_name} is already exist"
        self.__defined_color[color_name] = curses_color
        self.__color_counter += 1

    def make_pair(self, pair_name: str, text_color: str, background_color: str) -> None:
        assert text_color in self.__defined_color, f"color {text_color} is not defined"
        assert background_color in self.__defined_color, f"color {background_color} is not defined"
        curses.init_pair(self.__color_pair_counter,
                         self.__defined_color[text_color],
                         self.__defined_color[background_color])
        self.__defined_color_pair[pair_name] = self.__color_pair_counter
        self.__color_pair_counter += 1

    def defined_pair(self, pair_name: str):
        assert pair_name in self.__defined_color_pair, f"color_pair {pair_name} is not defined"
        return curses.color_pair(self.__defined_color_pair[pair_name])
