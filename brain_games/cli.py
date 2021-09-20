import prompt

print("Welcome to the Brain Games!")

user_name = prompt.string('May I have your name? ')


def welcome_user():
    print('Hello, ' + user_name + '!')


def main():
    welcome_user()


if __name__ == '__main__':
    main()
