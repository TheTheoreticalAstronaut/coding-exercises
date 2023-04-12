class BasicInt:
    def __init__(self, value = 0) -> None:
        self.value = value

    def get(self) -> int:
        return self.value

    def add(self, num: int) -> None:
        self.value += num

    def sub(self, num: int) -> None:
        self.value -= num

    def mul(self, num: int) -> None:
        self.value *= num

    def div(self, num: int) -> None:
        if(num == 0):
            raise ZeroDivisionError("Division by zero")
        else:
            self.value //= num