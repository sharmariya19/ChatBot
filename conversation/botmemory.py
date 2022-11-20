msg_store = ['remind', "recall", "remember"]


def store(reply):
    msg = reply.split("that")
    file = open('../memory.txt', 'a')
    file.write(msg[1]+"\n")
    file.close()


def remind():
    try:
        file = open("../memory.txt", "r")
        print(file.read())
        print("Sure!")
        file.close()
    except:
        print("There is nothing to remind you")


def filecheck(message):
    if message == "notes":
        remind()
    else:
        msg = message.split(" ")
        for word in msg:
            if word in msg_store:
                store(message)
