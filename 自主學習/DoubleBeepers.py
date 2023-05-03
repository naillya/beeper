"""
File: DoubleBeepers.py
Name:
-------------------------------
TODO:
"""

from karel.stanfordkarel import *


def main():
    """
    Karel will double the beepers
    """
    move()
    doble_beepers()
    put_beeper_back()
    karel_goes_home()


def put_beeper_back():
    move()
    while on_beeper():
        pick_beeper()
        turn_around()
        move()
        put_beeper()
        turn_around()
        move()


def karel_goes_home():
    turn_around()
    move()
    move()
    turn_around()


def doble_beepers():
    while on_beeper():
        pick_beeper()
        move()
        put_beeper()
        put_beeper()
        turn_around()
        move()
        turn_around()


def turn_around():
    for i in range(2):
        turn_left()


# ----- DO NOT MODIFY CODE BELOW THIS LINE ----- #
if __name__ == '__main__':
    execute_karel_task(main)
