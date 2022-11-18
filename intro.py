import random

first_name = ""

ignore_words = ["hey", "hello", "hi", "jarvis", "?", 'my', 'name', 'is', "it's", 'me', "this", "side", "i", "am"]
responses = [
        "Hi, {}, can I help you?",
        "Hello, {}, is there something I can do?",
        "Hey, {}, what's up?",
        "Hey, {}, How are you?"
    ]


def take_name():
    name = input()
    name_words = name.split((" "))
    for word in name_words:
        if word.lower() not in ignore_words:
            global first_name
            first_name = word.capitalize()
    print_hi(first_name)
    return first_name
    # message = input(f"{first_name}: ")


def print_hi(name):
    print((random.choice(responses)).format(first_name))

