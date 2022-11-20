import random

first_name = ""

ignore_words = ["hey", "hello", "hi", "jarvis", "?", 'my', 'name', 'is', "it's", 'me', "this", "side", "i", "am"]
responses = [
        "Hi {}, what can I do for you?",
        "Hello {}, how can i help you?",
        "Hey {}, can i do something for you?",
        "Hey {}, what should i do?"
    ]


def take_name():
    name = input()
    name_words = name.split(" ")
    for word in name_words:
        if word.lower() not in ignore_words:
            global first_name
            first_name = word.capitalize()
            break
    print_hi(first_name)
    return first_name


def print_hi(name):
    print((random.choice(responses)).format(first_name))

