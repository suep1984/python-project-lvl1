#!/usr/bin/env python
from brain_games.brain_games_engine import *
import random

print('Answer "yes" if given number is prime. Otherwise answer "no".')


def prime():
    for i in range(ROUND_COUNT):
        content_question = random.randint(3, 99)
        question(str(content_question))
        answer()
        correct_answer = 'yes'
        for i in range(3, content_question):
            if (content_question % i) == 0:
                correct_answer = 'no'
        comparsion(correct_answer)
    ok()


def main():
    prime()


if __name__ == '__main__':
    main()
