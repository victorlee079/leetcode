class MyStack:

    def __init__(self):
        self.q2 = []

    def push(self, x: int) -> None:
        self.q2.append(x)
        for i in range(len(self.q2)-1):
            self.q2.append(self.q2.pop(0))            

    def pop(self) -> int:
        return self.q2.pop(0)

    def top(self) -> int:
        return self.q2[0]

    def empty(self) -> bool:
        return len(self.q2) == 0
