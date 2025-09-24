#-----------------------#
#                       #
#   T H E  M A T R I X  #
#                       #
#       by jaekid       #
#                       #
#-----------------------#

import curses
import random
import time

# US ASCII characters
MATRIX_CHARS = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789@#$%&*")

def matrix_rain(stdscr):
    curses.curs_set(0)
    curses.start_color()
    curses.use_default_colors()

    # Colors: head (white), bright green, dim green
    curses.init_pair(1, curses.COLOR_WHITE, -1)  # head
    curses.init_pair(2, curses.COLOR_GREEN, -1)  # bright trail
    curses.init_pair(3, curses.COLOR_GREEN, -1)  # dim trail

    height, width = stdscr.getmaxyx()
    columns = [[] for _ in range(width)]

    stdscr.nodelay(True)

    density = 0.2       # Full screen
    speed = 0.05        # Falling speed
    trail_length = 6    # Length of fading trail

    while True:
        key = stdscr.getch()
        if key != -1:
            break

        stdscr.erase()

        for x in range(width):
            # Chance to start a new stream
            if random.random() < density:
                columns[x].append(0)

            new_positions = []
            for y in columns[x]:
                if 0 <= y < height:
                    char = random.choice(MATRIX_CHARS)
                    dist_from_head = y - max(columns[x])

                    if dist_from_head == 0 and y >= 3:
                        color = curses.color_pair(1)  # White head
                    elif 1 <= dist_from_head <= 2:
                        color = curses.color_pair(2)  # Bright green
                    elif 3 <= dist_from_head < trail_length:
                        color = curses.color_pair(3)  # Dim green
                    else:
                        color = curses.color_pair(2)

                    # Ensure we don't write past the right edge
                    if 0 <= x < width:
                        try:
                            stdscr.addstr(y, x, char, color)
                        except curses.error:
                            pass

                    new_positions.append(y + 1)

            # Keep positions within screen height + trail
            columns[x] = [pos for pos in new_positions if pos < height + trail_length]

        stdscr.refresh()
        time.sleep(speed)

if __name__ == "__main__":
    curses.wrapper(matrix_rain)
