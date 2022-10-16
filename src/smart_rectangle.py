import curses


class SmartRectangle:
    def __init__(self, win, name: str, color, uly: int = None, ulx: int = None, lry: int = None, lrx: int = None):
        self.__window_instance = win
        self.__default_color = color

        if uly is None:
            uly = 0
        if ulx is None:
            ulx = 0

        y, x = win.getmaxyx()
        self.lr_corner = (y - 1, x - 1)
        if lry is None:
            lry = self.lr_corner[0]
        if lrx is None:
            lrx = self.lr_corner[1]
        self.__rectangle(self.__window_instance, self.__default_color, uly, ulx, lry, lrx)
        self.__rectangles = dict()
        self.__rectangles[name] = (0, 0, lry, lrx)

    @property
    def rectangles(self):
        return self.__rectangles

    def add_rectangle(self, parent, name, color=None, uly=None, ulx=None, lry=None, lrx=None):
        p_uly, p_ulx, p_lry, p_lrx = self.__rectangles[parent]
        if uly is None:
            uly = p_uly + 1
        if ulx is None:
            ulx = p_ulx + 1
        if lry is None:
            lry = p_lry - 1
        if lrx is None:
            lrx = p_lrx - 1
        if color is None:
            color = self.__default_color
        self.__rectangle(self.__window_instance, color, uly, ulx, lry, lrx)
        self.__rectangles[name] = (uly, ulx, lry, lrx)

    def __rectangle(self, win, color, uly, ulx, lry, lrx) -> None:
        self.__hline(win=win, color=color, y=uly, x=ulx, n=abs(lrx - ulx))
        self.__hline(win=win, color=color, y=lry, x=ulx, n=abs(lrx - ulx))
        self.__vline(win=win, color=color, y=uly, x=ulx, n=abs(lry - uly))
        self.__vline(win=win, color=color, y=uly, x=lrx, n=abs(lry - uly))
        win.addch(uly, ulx, curses.ACS_ULCORNER, color)
        win.addch(uly, lrx, curses.ACS_URCORNER, color)
        win.addch(lry, ulx, curses.ACS_LLCORNER, color)
        if (lry, lrx) == self.lr_corner:
            win.insch(lry, lrx, curses.ACS_LRCORNER, color)
        else:
            win.addch(lry, lrx, curses.ACS_LRCORNER, color)

    def __hline(self, win, color, y: int, x: int, n: int) -> None:
        for h in range(x, x + n):
            if (y, h) == self.lr_corner:
                win.insch(y, h, curses.ACS_HLINE, color)
            else:
                win.addch(y, h, curses.ACS_HLINE, color)

    def __vline(self, win, color, y: int, x: int, n: int) -> None:
        for v in range(y, y + n):
            if (v, x) == self.lr_corner:
                win.insch(v, x, curses.ACS_VLINE, color)
            else:
                win.addch(v, x, curses.ACS_VLINE, color)
