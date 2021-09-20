#!/usr/bin/env python
from brain_games.brain_games_engine import *
import random

print('Find the greatest common divisor of given numbers')


def gcd():
    for i in range(ROUND_COUNT):
        first_number = random.randint(1, 20)
        second_number = random.randint(1, 20)
        question(str(first_number) + ' ' + str(second_number))
        answer()
        while first_number != 0 and second_number != 0:
            if first_number > second_number:
                first_number = first_number % second_number
            else:
                second_number = second_number % first_number
            correct_answer = str(max(first_number, second_number))
        comparsion(correct_answer)
    ok()


def main():
    gcd()


if __name__ == '__main__':
    main()
