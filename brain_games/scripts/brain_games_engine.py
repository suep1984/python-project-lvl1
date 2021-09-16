#!/usr/bin/python3
from brain_games.cli import name
import prompt
import random


def question(arg1, arg2, arg3):
    print('Question: {} {} {}'.format(arg1, arg2, arg3))


def ans():
    global answer
    answer = prompt.string('Your answer: ')


def ok():
    print('Congratulations, ' + name + '!')


def comparsion():
    if answer == result:
        print('Correct!')
    else:
        print('\'' + str(answer) + '\'' + " is wrong answer ;(. "
              "Correct answer was " + '\'' + str(result) + '\'' + ""
              ". \nLet's try again, " + name + '!')
        exit()


def even():
    global result
    for i in range(3):
        num = random.randint(0, 20)
        question(num, '', '')
        ans()
        if (num % 2) == 0:
            result = 'yes'
        elif (num % 2) != 0:
            result = 'no'
        comparsion()
    ok()


def calc():
    global result
    for i in range(3):
        num1 = random.randint(1, 20)
        num2 = random.randint(1, 20)
        oper = random.choice('+-*')
        question(str(num1), oper, str(num2))
        ans()
        if oper == '+':
            result = str(num1 + num2)
        elif oper == '-':
            result = str(num1 - num2)
        elif oper == '*':
            result = str(num1 * num2)
        comparsion()
    ok()


def gcd():
    global result
    for i in range(3):
        num1 = random.randint(1, 20)
        num2 = random.randint(1, 20)
        question(str(num1), str(num2), '')
        ans()
        while num1 != 0 and num2 != 0:
            if num1 > num2:
                num1 = num1 % num2
            else:
                num2 = num2 % num1
            result = str(max(num1, num2))
        print(result)
        comparsion()
    ok()


def progression():
    global result
    for i in range(3):
        start = random.randint(1, 10)
        multiply = random.randint(3, 20)
        my_list = list(range(start, 10000, multiply))
        progression = my_list[0:10]
        i = random.randint(0, 9)
        result = str(progression[i])
        progression[i] = str('..')
        str_progression = " ".join(str(_) for _ in progression)
        question(str_progression, '', '')
        ans()
        comparsion()
    ok()


def prime():
    global result
    for i in range(3):
        num = random.randint(3, 99)
        question(str(num), '', '')
        ans()
        result = 'yes'
        for i in range(3, num):
            if (num % i) == 0:
                result = 'no'
        comparsion()
    ok()


def main():
    pass


if __name__ == '__main__':
    main()
