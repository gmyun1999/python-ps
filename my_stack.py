class my_stack:
    def __init__(self, capacity):
        self.capacity = capacity
        self.stack = [None] * capacity
        self.ptr = 0

    def push(self, value):
        if self.ptr == self.capacity:
            print("stack is full")
        else:
            self.stack[self.ptr] = value
            self.ptr += 1

    def pop(self):
        if self.ptr == 0:
            print("stack is empty")
        else:
            self.ptr -= 1
            return self.stack[self.ptr]


if __name__ == "__main__":
    a = my_stack(3)
    a.push("a")
    a.push("a")
    a.push("a")
    a.pop()
    a.pop()
    a.pop()
    a.pop()
