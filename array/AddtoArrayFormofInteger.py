class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        ans, carry = [], 0
        while k > 0 or num:
            if k > 0:
                carry += k % 10
                k = k // 10
            if num:
                carry += num.pop()
            carry, val = carry // 10, carry % 10
            ans.append(val)
        if carry:
            ans.append(carry)
        return ans[::-1]
