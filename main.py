import intro
import checkword


if __name__ == '__main__':
    print('Hey this is Jarvis. who are you?')
    name = intro.take_name()


while True:
    message = input(f'{name}: ').lower()
    if message in checkword.exit_words:
        print(f"Jarvis: Okay, {name}, GoodBye!!!")
        break
    checkword.check(message, name)