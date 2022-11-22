from conversation import mathoperation, botmemory, joke
import random
# from database.postgres import insert_data
import datetime
from database.mongo_db import insert_data

input_words = {
    "hello_words": ["hi", "hello", "hey"],
    "exit_words": ["bye", "okay bye", "exit", "goodbye"],
    "math_words": ["add", "addition", "subtract", "+", "-", "*", "/", "subtraction", "multiply", "multiplication", "divide", "division"],
    "memory_words": ["remember", "recall", "remind", "notes"],
    "normal_words": ["okay", "ok", "fine", "no", "nothing"]
}


def check(reply, name):

    insert_data.store_session(name, reply) #mongo
    # insert_data.insert_detail(name, reply) #postgres

    message = reply.split(" ")
    print("Jarvis: ", end=" ")
    for words in message:
        if words in input_words["normal_words"]:
            msg = "okayy"
            break
        if words in input_words["hello_words"]:
            msg = random.choice(input_words["hello_words"])
            break
        if words in input_words["memory_words"]:
            msg = botmemory.filecheck(reply)
            break
        if words in joke.words["positive_words"] or words in joke.words["joke_words"] or words in joke.words["negative_words"]:
            msg = joke.converse(reply, name)
            break
        msg, bool_val = check_op(words, reply)
        if bool_val:
            break
    else:
        msg = "Sorry! I didn't get you"
    print(msg)

    insert_data.store_session("Jarvis", msg)    #mongo
    # insert_data.insert_detail("Jarvis", msg)   # postgres


def check_op(words, reply):
    if words in input_words["math_words"]:
        val = mathoperation.checkoperation(reply)
        return val, True
    for word in words:
        if word in input_words["math_words"]:
            val = mathoperation.checkoperation(reply)
            return val, True
    else:
        return None, False

