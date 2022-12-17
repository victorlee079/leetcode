class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stk = []
        for token in tokens:
            if token in "+-*/":
                b = stk.pop()
                a = stk.pop()
                if token == "+":
                    stk.append(a + b)
                elif token == "-":
                    stk.append(a - b)
                elif token == "*":
                    stk.append(a * b)
                else:
                    stk.append((int)(a / b))
            else:
                stk.append(int(token))
        return stk[-1]
