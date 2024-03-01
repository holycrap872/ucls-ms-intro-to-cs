#!/usr/bin/env python3

def draw_line(x):
    pass


def get_drawer(x):
    pass


def time_left_to_play():
    pass


def team_guess():
    pass


def declare_winner():
    pass


def get_random_word():
    pass


team_1 = []
team_2 = []

while time_left_to_play():
    drawer_1 = get_drawer(team_1)
    drawer_2 = get_drawer(team_2)
    word = get_random_word()

    current_drawer = drawer_1
    next_drawer = drawer_2
    guessed = False
    while True:
        draw_line(current_drawer, word)
        guessed = team_guess()

        if guessed == word:
            break
        else:
            tmp = drawer_2
            current_drawer = drawer_2
            next_drawer = drawer_1

declare_winner()    

