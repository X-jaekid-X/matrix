#-----------------------#
#                       #
#  T H E  M A T R I X   #
#                       #
#       by jaekid       #
#                       #
#-----------------------#

import curses
import random
import time

MATRIX_CHARS = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789@#$%&*+><=|/")

# ASCII art letters for big font
BIG_FONT = {
    "A": ["  A  ",
          " A A ",
          "AAAAA",
          "A   A",
          "A   A"],
    "B": ["BBBB ",
          "B   B",
          "BBBB ",
          "B   B",
          "BBBB "],
    "C": [" CCC ",
          "C   C",
          "C    ",
          "C   C",
          " CCC "],
    "D": ["DDDD ",
          "D   D",
          "D   D",
          "D   D",
          "DDDD "],
    "E": ["EEEEE",
          "E    ",
          "EEE  ",
          "E    ",
          "EEEEE"],
    "H": ["H   H",
          "H   H",
          "HHHHH",
          "H   H",
          "H   H"],
    "I": ["IIIII",
          "  I  ",
          "  I  ",
          "  I  ",
          "IIIII"],
    "K": ["K   K",
          "K  K ",
          "KKK  ",
          "K  K ",
          "K   K"],
    "M": ["M   M",
          "MM MM",
          "M M M",
          "M   M",
          "M   M"],
    "R": ["RRRR ",
          "R   R",
          "RRRR ",
          "R R  ",
          "R  RR"],
    "T": ["TTTTT",
          "  T  ",
          "  T  ",
          "  T  ",
          "  T  "],
    "X": ["X   X",
          " X X ",
          "  X  ",
          " X X ",
          "X   X"],
    "Y": ["Y   Y",
          " Y Y ",
          "  Y  ",
          "  Y  ",
          "  Y  "],
    " ": ["     ",
          "     ",
          "     ",
          "     ",
          "     "],
    "J": ["  JJJ",
          "   J ",
          "   J ",
          "J  J ",
          " JJ  "],
    "D": ["DDDD ",
          "D   D",
          "D   D",
          "D   D",
          "DDDD "],
}

def big_text_lines(word):
    """Convert a word into list of strings representing big ASCII art lines"""
    lines = [""] * 5
    for c in word.upper():
        char_art = BIG_FONT.get(c, BIG_FONT[" "])
        for i in range(5):
            lines[i] += char_art[i] + "  "  # 2 spaces between letters
    return lines

def display_banner(stdscr, duration=3):
    curses.curs_set(0)
    curses.start_color()
    curses.use_default_colors()
    curses.init_pair(1, curses.COLOR_GREEN, -1)
    
    stdscr.nodelay(True)
    height, width = stdscr.getmaxyx()
    words = ["THE", "MATRIX", "by JAEKID"]
    
    total_lines = len(words) * 5 + (len(words) - 1)
    start_y = max((height - total_lines)//2, 0)
    
    start_time = time.time()
    while time.time() - start_time < duration:
        stdscr.erase()
        for w_idx, word in enumerate(words):
            lines = big_text_lines(word)
            for l_idx, line in enumerate(lines):
                y = start_y + w_idx*6 + l_idx
                x = max((width - len(line))//2, 0)
                display_line = ""
                for ch in line:
                    if ch != " " and random.random() < 0.4:  # 40% chance to replace
                        display_line += random.choice(MATRIX_CHARS)
                    else:
                        display_line += ch
                try:
                    stdscr.addstr(y, x, display_line, curses.color_pair(1) | curses.A_BOLD)
                except curses.error:
                    pass
        stdscr.refresh()
        time.sleep(0.1)
        key = stdscr.getch()
        if key != -1:
            break

def matrix_rain(stdscr):
    curses.curs_set(0)
    curses.start_color()
    curses.use_default_colors()
    curses.init_pair(1, curses.COLOR_GREEN, -1)

    height, width = stdscr.getmaxyx()
    columns = [[] for _ in range(width)]
    stdscr.nodelay(True)
    density = 0.2
    speed = 0.05
    trail_length = 6

    while True:
        stdscr.erase()
        for x in range(width):
            if random.random() < density:
                columns[x].append(0)
            new_positions = []
            max_y = max(columns[x]) if columns[x] else 0
            for y in columns[x]:
                if 0 <= y < height:
                    char = random.choice(MATRIX_CHARS)
                    try:
                        stdscr.addch(y, x, char, curses.color_pair(1))
                    except curses.error:
                        pass
                    new_positions.append(y + 1)
            columns[x] = [pos for pos in new_positions if pos < height + trail_length]
        stdscr.refresh()
        time.sleep(speed)
        key = stdscr.getch()
        if key != -1:
            break

def main(stdscr):
    display_banner(stdscr, duration=4)  # show dynamic banner for 4 seconds
    matrix_rain(stdscr)

if __name__ == "__main__":
    curses.wrapper(main)








