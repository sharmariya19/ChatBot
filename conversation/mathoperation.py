import re
from conversation import calculate


operations1 = ('+', '-', '*', '/')
operations2 = ('add', 'subtract', 'multiply', 'divide')
operations3 = ('addition', 'subtraction', 'multiplication', 'division')
operations = tuple(zip(operations1, operations2, operations3))


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

    calc = calculate.Calculate(*nums)
    if op == 'add':
        res = calc.add()
    elif op == 'subtract':
        res = calc.subtract()
    elif op == 'multiply':
        res = calc.multiply()
    elif op == 'divide':
        res = calc.divide()

    return res


def check_values(msg):
    regex = '\d+'
    values = re.findall(regex, msg)
    return values
