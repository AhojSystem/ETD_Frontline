import curses
from curses import wrapper
from text_color import TextColor, CursesColor
from smart_rectangle import SmartRectangle
from text_layout import TextLayout
from random import randint


class Game:
    def __init__(self):
        self.field = [line for line in self.file_loader("./resources/map.txt")]
        self.pos_x, self.pos_y = 40, 50
        self.player = "@"

    def init(self):
        self.color = TextColor()
        self.color.set_curses_color("Black", curses.COLOR_BLACK)
        self.color.set_color("Red", CursesColor(red=1000, green=200, blue=200))
        self.color.set_color("Orange", CursesColor(red=1000, green=500, blue=200))
        self.color.set_color("Yellow", CursesColor(red=1000, green=1000, blue=200))
        self.color.set_color("Aqua", CursesColor(red=500, green=800, blue=1000))
        self.color.set_color("Green", CursesColor(red=200, green=1000, blue=200))
        self.color.set_color("Raw_Green", CursesColor(red=0, green=1000, blue=0))
        self.color.set_color("Pink", CursesColor(red=1000, green=750, blue=750))
        self.color.make_pair("RED_AND_BLACK", "Red", "Black")
        self.color.make_pair("ORANGE_AND_BLACK", "Orange", "Black")
        self.color.make_pair("YELLOW_AND_BLACK", "Yellow", "Black")
        self.color.make_pair("AQUA_AND_BLACK", "Aqua", "Black")
        self.color.make_pair("GREEN_AND_BLACK", "Green", "Black")
        self.color.make_pair("GREEN", "Raw_Green", "Black")
        self.color.make_pair("PINK_AND_BLACK", "Pink", "Black")
        self.dic = dict()
        self.dic["D"] = self.color.defined_pair("RED_AND_BLACK")
        self.dic["M"] = self.color.defined_pair("ORANGE_AND_BLACK")
        self.dic["S"] = self.color.defined_pair("YELLOW_AND_BLACK")
        self.dic["G"] = self.color.defined_pair("AQUA_AND_BLACK")
        self.dic["T"] = self.color.defined_pair("GREEN_AND_BLACK")
        self.dic["."] = self.color.default_color
        self.dic["#"] = self.color.default_color

    def main(self, stdscr):
        stdscr.clear()
        stdscr.refresh()
        curses.curs_set(False)
        stdscr.refresh()
        self.init()
        win = curses.newwin(25, 45, 0, 40)
        sr = SmartRectangle(win, "map", self.color.defined_pair("GREEN"))
        win.addstr(0, 1, " ﾏｯﾌﾟ ", self.color.defined_pair("GREEN"))

        win2 = curses.newwin(25, 40, 0, 0)
        sr = SmartRectangle(win2, "status", self.color.defined_pair("GREEN"))
        win2.addstr(0, 1, " ｼﾞｮｳﾀｲ ", self.color.defined_pair("GREEN"))
        sr.add_rectangle("status", "status2", lry=6)
        win2.addstr(1, 2, " ｽﾃｰﾀｽ ", self.color.defined_pair("GREEN"))
        sr.add_rectangle("status", "log", uly=7)
        win2.addstr(7, 2, " ｲﾍﾞﾝﾄﾛｸﾞ ", self.color.defined_pair("GREEN"))

        key = 0
        turn = 1

        self.orgasm = 0
        self.anal_orgasm = 0
        self.nipple_orgasm = 0
        self.incontinence = 0
        frag = True

        txt = TextLayout(win2, 4, 30, self.color.defined_pair("PINK_AND_BLACK"), 2, 2)
        txt.add_string(["ｾﾞｯﾁｮｳ", " : ", f"{self.orgasm}"])
        txt.add_string(["ｺｳﾓﾝ ｾﾞｯﾁｮｳ", " : ", f"{self.anal_orgasm}"])
        txt.add_string(["ﾁｸﾋﾞ ｾﾞｯﾁｮｳ", " : ", f"{self.nipple_orgasm}"])
        txt.add_string(["ｵﾓﾗｼ", " : ", f"{self.incontinence}"])
        txt.print()

        while key != 27:
            for x in range(-10, 13):
                for y in range(-20, 23):
                    u, v = self.pos_x + x, self.pos_y + y
                    try:
                        if v >= 0 and u >= 0:
                            if self.field[u][v] == "#":
                                win.addstr(x + 11, y + 21, "#", self.dic[self.field[u][v]])
                            elif self.field[u][v] == "G":
                                win.addstr(x + 11, y + 21, "G", self.dic[self.field[u][v]])
                            else:
                                win.addstr(x + 11, y + 21, ".", self.dic[self.field[u][v]])
                        else:
                            win.addstr(x + 11, y + 21, "#", self.color.default_color)
                    except IndexError:
                        win.addstr(x + 11, y + 21, "#", self.color.default_color)
                    win.addstr(11, 21, self.player, self.color.player_color)
            win.refresh()
            win2.refresh()
            txt.clear()
            txt.add_string(["ｾﾞｯﾁｮｳ", " : ", f"{self.orgasm}"])
            txt.add_string(["ｺｳﾓﾝ ｾﾞｯﾁｮｳ", " : ", f"{self.anal_orgasm}"])
            txt.add_string(["ﾁｸﾋﾞ ｾﾞｯﾁｮｳ", " : ", f"{self.nipple_orgasm}"])
            txt.add_string(["ｵﾓﾗｼ", " : ", f"{self.incontinence}"])
            txt.print()

            key = stdscr.getch()
            if key == curses.KEY_UP:
                if self.field[self.pos_x - 1][self.pos_y] != "#":
                    self.pos_x -= 1
            if key == curses.KEY_DOWN:
                if self.field[self.pos_x + 1][self.pos_y] != "#":
                    self.pos_x += 1
            if key == curses.KEY_LEFT:
                if self.field[self.pos_x][self.pos_y - 1] != "#":
                    self.pos_y -= 1
            if key == curses.KEY_RIGHT:
                if self.field[self.pos_x][self.pos_y + 1] != "#":
                    self.pos_y += 1
            if self.field[self.pos_x][self.pos_y] == "G":
                win2.addstr(8, 2, "                                    ")
                win2.addstr(8, 2, "M200 ﾊ ｴﾛﾄﾗｯﾌﾟﾀﾞﾝｼﾞｮﾝ ｶﾗ ﾀﾞｯｼｭﾂｼﾀ")
                win2.addstr(9, 2, "                                    ")
                win2.addstr(9, 2, f"{self.orgasm}ｶｲ ﾉ ｾﾞｯﾁｮｳ ﾄ")
                win2.addstr(10, 2, "                                    ")
                win2.addstr(10, 2, f"{self.anal_orgasm}ｶｲ ﾉ ｺｳﾓﾝ ｾﾞｯﾁｮｳ ﾄ")
                win2.addstr(11, 2, "                                    ")
                win2.addstr(11, 2, f"{self.nipple_orgasm}ｶｲ ﾉ ﾁｸﾋﾞｾﾞｯﾁｮｳ ﾄ")
                win2.addstr(12, 2, "                                    ")
                win2.addstr(12, 2, f"{self.incontinence}ｶｲ ﾉ ｵﾓﾗｼ ｦ ｼﾃｼﾏｯﾀ")
                if not frag:
                    win2.addstr(13, 2, "                                    ")
                    win2.addstr(13, 2, f"ｻﾗﾆ, ﾄｳﾊﾂ ｦ ｲｯﾎﾟﾝﾉｺﾗｽﾞ ｿﾗﾚﾃ ｼﾏｯﾀ")
                    win2.addstr(14, 2, "                                    ")
                    win2.addstr(14, 2, f"ﾏﾙｶﾞﾘ ﾆ ｻﾚﾀ M200ﾁｬﾝ ｶﾜｲｲﾈ")
                win2.refresh()
                stdscr.getch()
                break


            rnd = randint(0, 99)

            def debuf():
                win2.addstr(8, 2, "                                    ")
                win2.addstr(9, 2, "                                    ")
                win2.addstr(10, 2, "                                    ")
                rnd2 = randint(0, 3)
                win2.addstr(8, 2, f"ﾀｰﾝ{turn} : M200 ﾊ ｼｮｸｼｭ ﾆ ｵｿﾜﾚﾀ")
                if rnd2 == 0:
                    win2.addstr(9, 2, "M200 ﾊ ｾﾞｯﾁｮｳ ｼﾀ")
                    self.orgasm += 1
                elif rnd2 == 1:
                    win2.addstr(9, 2, "M200 ﾊ ｺｳﾓﾝ ｾﾞｯﾁｮｳ ｼﾀ")
                    self.anal_orgasm += 1
                elif rnd2 == 2:
                    win2.addstr(9, 2, "M200 ﾊ ﾁｸﾋﾞ ｾﾞｯﾁｮｳ ｼﾀ")
                    self.nipple_orgasm += 1
                else:
                    win2.addstr(9, 2, "M200 ﾊ ｵﾓﾗｼ ｼﾀ")
                    self.incontinence += 1

            char = self.field[self.pos_x][self.pos_y]
            if char == "S":
                if rnd < 50:
                    debuf()
            elif char == "M":
                if rnd < 70:
                    debuf()
            elif char == "D":
                if rnd < 90:
                    debuf()
            elif char == "T":
                if rnd < 3 and frag:
                    win2.addstr(8, 2, "                                    ")
                    win2.addstr(9, 2, "                                    ")
                    win2.addstr(10, 2, "                                    ")
                    win2.addstr(8, 2, f"ﾀｰﾝ{turn} : M200 ﾊ ｼｮｸｼｭ ﾆ ｵｿﾜﾀ")
                    win2.addstr(9, 2, "M200 ﾊ ｼｮｸｼｭ ﾆ ﾄｳﾊﾂ ｦ ｿﾘｵﾄｻﾚﾃ ｼﾏｯﾀ")
                    win2.addstr(10, 2, "M200 ﾊ ﾏﾙﾎﾞｳｽﾞ ﾆ ﾅｯﾃｼﾏｯﾀ")
                    frag = False

            turn += 1

        curses.nocbreak()
        stdscr.keypad(False)
        curses.echo()
        curses.endwin()
        curses.curs_set(True)

    @staticmethod
    def file_loader(path):
        for line in open(path, "r", encoding="utf-8"):
            yield line.replace("\n", "")

    def __call__(self, *args, **kwargs):
        return self.main


if __name__ == '__main__':
    wrapper(Game()())
