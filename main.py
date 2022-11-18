import intro
import mathoperation


if __name__ == '__main__':
    print('Hey this is Jarvis. who are you?')
    name = intro.take_name()

conversation = ["what", "doing", "joke", "song", "movie", "know"]
math_ = ["add", "addition", "sub", "subtraction", "multiply", "multiplication", "divide", "division", "power", "square root"]
memory = ["remember", "memorize", "recall"]
exit_words = ["bye", "exit"]

while True:
    message = input(f'{name}: ')
    sentance = message.split(" ")
    for words in sentance:
        if words in exit_words:
            print(f"Jarvis: Okay, {name}, GoodBye!!!")
            break
        if words in math_:
            mathoperation.checkoperation(message)









