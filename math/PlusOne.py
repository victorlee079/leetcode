class Solution:
    def plusOne(self, digits):
        i = len(digits) - 1
        while digits[i] == 9:
            digits[i] = 0
            i -= 1
        if(i < 0):
            digits = [1] + digits
        else:
            digits[i] += 1
        return digits