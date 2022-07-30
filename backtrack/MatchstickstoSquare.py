# Bin Packing Problem, NP-complete, No possible for a solution that take less than exponential time
# Time O(4^N) 
# Space O(N)
class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        if not matchsticks:
            return False
        
        perimeter = sum(matchsticks)
                
        if perimeter % 4 != 0:
            return False
        
        side_len = perimeter // 4
        
        sides = [0] * 4
        
        # Optimized by chosing the longer first
        matchsticks.sort(reverse=True)
        
        def backtrack(index):
            if sides[0] == sides[1] == sides[2] == sides[3] == side_len:
                return True
            
            for i in range(4):
                if sides[i] + matchsticks[index] <= side_len:
                    sides[i] += matchsticks[index]
                    if backtrack(index+1):
                        return True
                    sides[i] -= matchsticks[index]
            return False
        
        return backtrack(0)
