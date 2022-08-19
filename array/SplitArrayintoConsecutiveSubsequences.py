class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        n = len(nums)
        heaps = [[-nums[0]]]
        for i in range(1, n):
            num = nums[i]
            heap = None
            for j in range(len(heaps)-1, -1, -1):
                if -heaps[j][0] + 1 == num:
                    heap = heaps[j]
                    break
            if heap:
                heapq.heappush(heap, -num)
            else:
                heaps.append([-num])
        
        for i in range(len(heaps)):
            if len(heaps[i]) < 3:
                return False
        return True
            
    def isPossible2Maps(self, nums: List[int]) -> bool:
        counts = Counter(nums)
        end = defaultdict(int)
        
        for num in nums:
            if not counts[num]:
                continue
            counts[num] -= 1
            if end[num-1] > 0:
                end[num-1] -= 1
                end[num] += 1
            elif counts[num+1] and counts[num+2]:
                counts[num+1] -= 1
                counts[num+2] -= 1
                end[num+2] += 1
            else:
                return False
        return True
            
