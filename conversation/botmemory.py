
msg_store = ['remind', "recall", "remember"]


def store(reply):
    msg = reply.split("that")
    try:
        file = open('./memory.txt', 'a')
        file.write(msg[1]+"\n")
        print("Sure!")
        file.close()
    except:
        print("Sorry, I can't do it")


def remind():
    try:
        file = open("./memory.txt", "r")
        print(file.read())
        file.close()
    except:
        print("There is nothing to remind you")


def filecheck(message):
    msg = message.split(" ")
    for word in msg:
        if word == "notes":
            remind()
        elif word in msg_store:
            store(message)
