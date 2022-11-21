from conversation import mathoperation, botmemory, joke
import random

input_words = {
    "hello_words": ["hi", "hello", "hey"],
    "exit_words": ["bye", "okay bye", "exit", "goodbye"],
    "math_words": ["add", "addition", "subtract", "+", "-", "*", "/", "subtraction", "multiply", "multiplication", "divide", "division"],
    "memory_words": ["remember", "recall", "remind", "notes"],
    "normal_words": ["okay", "ok", "fine", "no", "nothing"]
}


def check(reply, name):
    message = reply.split(" ")
    print("Jarvis: ", end=" ")
    for words in message:
        if words in input_words["normal_words"]:
            print("okayy")
            break
        if words in input_words["hello_words"]:
            print(random.choice(input_words["hello_words"]))
            break
        if words in input_words["memory_words"]:
            botmemory.filecheck(reply)
            break
        if words in joke.words["positive_words"] or words in joke.words["joke_words"] or words in joke.words["negative_words"]:
            print(joke.converse(reply, name))
            break
        found = check_op(words, reply)
        if found:
            break
    else:
        print("Sorry! I didn't get you")


def check_op(words, reply):
    if words in input_words["math_words"]:
        mathoperation.checkoperation(reply)
        return True
    for word in words:
        if word in input_words["math_words"]:
            mathoperation.checkoperation(reply)
            return True
    else:
        return False

