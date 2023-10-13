class Stack:
    def __init__(self, size: int = 5):
        self._list = []
        self._size = size
        self._top = -1

    def push(self, item: int):
        if len(self._list) == self._size:
            raise Exception("Stack Overflow")

        self._list.append(item)
        self._top += 1

    def pop(self):
        if self._top == -1:
            raise Exception("Stack Underflow")

        print(self._list[self._top])
        self._top -= 1


if __name__ == "__main__":
    stack = Stack(5)
    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.push(4)
    stack.push(5)
