#!/usr/bin/env python
from brain_games.brain_games_engine import question, \
    answer, comparsion, ok, ROUND_COUNT
import random

print('What is the result of the expression?')


def calc():
    for i in range(ROUND_COUNT):
        first_number = random.randint(0, 20)
        second_number = random.randint(0, 20)
        operator = random.choice('+-*')
        question(str(first_number) + ' ' + operator + ' ' + str(second_number))
        answer()
        if operator == '+':
            correct_answer = str(first_number + second_number)
        elif operator == '-':
            correct_answer = str(first_number - second_number)
        elif operator == '*':
            correct_answer = str(first_number * second_number)
        comparsion(correct_answer)
    ok()


def main():
    calc()


if __name__ == '__main__':
    main()
