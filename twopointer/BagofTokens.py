class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        tokens.sort()
        ans = score = 0
        l, r = 0, len(tokens)-1
        while l <= r:
            if power >= tokens[l]:
                score += 1
                power -= tokens[l]
                l += 1
                ans = max(score, ans)
            elif score > 0:
                power += tokens[r]
                score -= 1
                r -= 1
            else:
                break
        return ans
        
