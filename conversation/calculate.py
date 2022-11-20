class Calculate:
    _num1 = 0
    _num2 = 0

    def __init__(self, num1, num2):  # class constructor
        self._num1 = int(num1)
        self._num2 = int(num2)

    def add(self):
        print("{}+{} = {}".format(self._num1, self._num2, self._num1 + self._num2))

    def subtract(self):
        print("{}-{} = {}".format(self._num1, self._num2, self._num1 - self._num2))

    def multiply(self):
        print("{}*{} = {}".format(self._num1, self._num2, self._num1 * self._num2))

    def divide(self):
        try:
            self._num1 / self._num2
        except ZeroDivisionError as e:
            print("Division by zero not allowed")
        else:
            print(
                "{}/{} = {}".format(self._num1, self._num2, self._num1 // self._num2))  # floor division
