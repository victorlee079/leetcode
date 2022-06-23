class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        courses = sorted(courses, key=lambda c:(c[1], c[0]))
        
        res, currTotalTime = 0, 0
        heap = []
        
        for duration, lastday in courses:
            if currTotalTime + duration <= lastday:
                currTotalTime += duration
                # Convert to Min heap
                heapq.heappush(heap, -duration)
            else:
                # Try swapping
                if heap and -heap[0] > duration and currTotalTime + heap[0] + duration <= lastday:
                    largest_duration = heapq.heappop(heap)
                    currTotalTime += duration + largest_duration
                    heapq.heappush(heap, -duration)
                    
        return len(heap)
