"""
File: PotholeFilling.py
Name: KEVIN:
--------------------------
This program shows karel filling 3
potholes. Students learn the concept of
decomposition through the process.
"""

from karel.stanfordkarel import *


def main():
    for i in range(3):
        go_in()
        put_11()
        go_out()


def go_in():
    """
    pre-condition:karel is at upper left the pothole facing east.
    post-condition:karel is in the pothole,facing south.
    """
    move()
    turn_right()
    move()


def go_out():
    """
    pre-condition:karel is in the pothole,facing south.
    post-condition:karel is at upper left the pothole facing east.
    """
    turn_around()
    move()
    turn_right()
    move()


def turn_right():
    for i in range(3):
        turn_left()


def put_11():
    for i in range(11):
        put_beeper()


def turn_around():
    for i in range(2):
        turn_left()



# ----- DO NOT EDIT CODE BELOW THIS LINE ----- #
if __name__ == '__main__':
    execute_karel_task(main)
