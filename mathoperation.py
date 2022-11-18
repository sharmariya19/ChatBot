def checkoperation(message):
    num1, num2, op = check_values(msg)



operations1 = ('+', '-', '*', '/')
operations2 = ('add', 'subtract', 'mulitply','divide')
operations3 = ('addition', 'subtraction', 'multiplication', 'division')
operations = tuple(zip(operations1, operations2, operations3))

def check_values(msg):
    res = [int(i) for i in msg.split() if i.isdigit()]
    for word in msg
        if i.isdigit():
            res.append(word)
        if word in operations:
            op = word
    return res[0], res[1]