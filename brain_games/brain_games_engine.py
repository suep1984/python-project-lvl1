#!/usr/bin/python3
from brain_games.cli import user_name
import prompt

ROUND_COUNT = 3


def question(content):
    print('Question: {}'.format(content))


def answer():
    global user_answer
    user_answer = prompt.string('Your answer: ')


def comparsion(correct_answer):
    if user_answer == correct_answer:
        print('Correct!')
    else:
        print('\'' + str(user_answer) + '\'' + " is wrong answer ;(. "
              "Correct answer was " + '\'' + str(correct_answer) + '\'' + ""
              ". \nLet's try again, " + user_name + '!')
        exit()


def ok():
    print('Congratulations, ' + user_name + '!')


def main():
    pass


if __name__ == '__main__':
    main()
