import re
import calculate


def checkoperation(message):
    nums = check_values(message)
    op = ''
    for words in message:
        for word in words:
            if word == '+' or word == '-' or word == '*' or word == '/':
                op = operations2[operations1.index(word)]
    if not op:
        message = message.split(" ")
        for words in message:
            for i in range(len(operations)):
                if words in operations[i]:
                    op = operations2[i]
                    break

    obj1 = calculate.Calculate(*nums)
    if op == 'add':
        obj1.add()
    elif op == 'subtract':
        obj1.subtract()
    elif op == 'multiply':
        obj1.multiply()
    elif op == 'divide':
        obj1.divide()


operations1 = ('+', '-', '*', '/')
operations2 = ('add', 'subtract', 'multiply', 'divide')
operations3 = ('addition', 'subtraction', 'multiplication', 'division')
operations = tuple(zip(operations1, operations2, operations3))


def check_values(msg):
    regex = '\d+'
    values = re.findall(regex, msg)
    return values
