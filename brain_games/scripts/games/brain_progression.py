#!/usr/bin/env python
from brain_games.brain_games_engine import *
import random

print('What number is missing in the progression?')


def progression():
    for i in range(ROUND_COUNT):
        begin_progression = random.randint(1, 10)
        end_progression = 1000
        step_progression = random.randint(3, 20)
        progression = list(range(begin_progression, end_progression, step_progression))[0:10]
        replaceable_item_index = random.randint(0, 9)
        correct_answer = str(progression[replaceable_item_index])
        progression[replaceable_item_index] = str('..')
        content_question = " ".join(str(_) for _ in progression)
        question(content_question)
        answer()
        comparsion(correct_answer)
    ok()


def main():
    progression()


if __name__ == '__main__':
    main()
