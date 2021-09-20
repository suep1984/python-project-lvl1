#!/usr/bin/env python
from brain_games.brain_games_engine import *
import random

print('Answer "yes" if the number is even, otherwise answer "no".')


def main():
    for i in range(ROUND_COUNT):
        content_question = random.randint(0, 20)
        question(content_question)
        answer()
        if (content_question % 2) == 0:
            correct_answer = 'yes'
        elif (content_question % 2) != 0:
            correct_answer = 'no'
        comparsion(correct_answer)
    ok()


if __name__ == '__main__':
    main()

