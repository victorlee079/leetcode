d = { "2": ["a", "b", "c"], "3": ["d", "e", "f"], "4": ["g", "h", "i"], "5": ["j", "k", "l"], "6": ["m", "n", "o"], "7": ["p", "q", "r", "s"], "8": ["t", "u", "v"], "9": ["w", "x", "y", "z"]}

def combine(res, digits):
    if len(digits) < 1:
        return res

    letters, r = d[digits[0]], []
    if len(res) > 0:
        for i in letters:
            for j in res:
                r.append(j + i)
    else:
        r = letters
    return combine(r, digits[1:])


class Solution:
    def letterCombinations(self, digits):
        return combine([], digits)
