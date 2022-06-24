import heapq

class Solution:
    def isPossible(self, A):
        total = sum(A)
        A = [-a for a in A]
        heapq.heapify(A)
        
        while True:
            a = -heapq.heappop(A)
            total -= a
            
            # All ones or (1, x) which is always correct
            if a == 1 or total == 1: return True
            
            # 1.) largest should be > the rest (becoz the rest + a number = largest)
            # 2.) total = 0 for length of array = 1
            if a < total or total == 0:
                return False
            
            a %= total
            
            # Same as (1)
            # a = x * total for any integer x
            if a == 0:
                return False
            
            total += a
            heapq.heappush(A, -a)
