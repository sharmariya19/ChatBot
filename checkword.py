from conversation import mathoperation, botmemory, joke
import random


hello_words = ["hi", "hello", "hey"]
exit_words = ["bye" , "exit", "goodbye"]
math_ = ["add", "addition", "subtract", "+", "-", "*", "/", "subtraction", "multiply", "multiplication", "divide", "division"]
memory = ["remember", "recall", "remind", "notes"]
normal_words = ["okay", "ok", "fine", "no", "nothing"]


def check(reply, name):
    message = reply.split(" ")
    print("Jarvis: ", end=" ")
    for words in message:
        if words in normal_words:
            print("okyy")
            break
        if words in hello_words:
            print(random.choice(hello_words))
            break
        if words in memory:
            botmemory.filecheck(reply)
            break
        if words in joke.positive_words or words in joke.joke_words or words in joke.negative_words:
            print(joke.converse(reply, name))
            break
        found = check_op(words, reply)
        if found:
            break
    else:
        print("Sorry! I didn't get you")


def check_op(words, reply):
    if words in math_:
        mathoperation.checkoperation(reply)
        return True
    for word in words:
        if word in math_:
            mathoperation.checkoperation(reply)
            return True
    else:
        return False

