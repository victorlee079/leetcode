class Queue:
    def __init__(self):
        self.stk1 = []
        self.stk2 = []

    def enQueue(self, x):
        self.stk1.append(x)

    def deQueue(self):
        if not self.stk1 and not self.stk2:
            return

        if self.stk2:
            return self.stk2.pop()
        else:
            while self.stk1:
                self.stk2.append(self.stk1.pop())
            return self.stk2.pop()