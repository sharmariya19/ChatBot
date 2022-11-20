from conversation import mathoperation, botmemory
import random

hello_words = ["hi", "hello", "hey"]
exit_words = ["bye", "exit", "goodbye"]
math_ = ["add", "addition", "subtract", "+", "-", "*", "/", "subtraction", "multiply", "multiplication", "divide", "division", "power", "square root"]
conversation_ = ["joke", "other", "another", "hahaha"]
memory = ["remember", "recall", "remind", "notes"]


def check(reply, name):
    message = reply.split(" ")
    print("Jarvis: ", end=" ")
    for words in message:
        if words in hello_words:
            print(random.choice(hello_words))
            break
        if words in memory:
            botmemory.filecheck(reply)
            break
        if words in conversation.positive_words or words in conversation.joke_words:
            print(conversation.converse(reply, name))
            break
        found = check_op(words, reply)
        if found:
            break
    else:
        print("i didn't get you")


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

