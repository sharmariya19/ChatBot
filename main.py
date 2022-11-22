import intro
import checkword


if __name__ == '__main__':
    print('Hey this is Jarvis. who are you?')
    name = intro.take_name()


while True:
    message = input(f'{name}: ').lower()

    if message in checkword.input_words["exit_words"]:
        print(f"Jarvis: Okay, {name}, GoodBye!!!")
        break
    try:
        checkword.check(message, name)
    except Exception as e:
        print("I think something is wrong here", e)