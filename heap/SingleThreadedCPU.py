class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        # O (n log n)
        # Sort the tasks first
        tasks = deque(sorted([(enqTime, procTime, i) for i, (enqTime, procTime) in enumerate(tasks)]))
        ans = []

        # Initialize the start time by the first task
        q, startTime = [], tasks[0][0]

        while True:
            
            # While the enqueue time is less than or equal to the start time,
            # add to the min heap which is sorted by processing time and index
            while tasks and tasks[0][0] <= startTime:
                enqTime, procTime, index = tasks.popleft()
                heapq.heappush(q, (procTime, index))

            if q:
                procTime, index = heapq.heappop(q)
                ans.append(index)
                # Complete a task and increase the start time
                startTime += procTime
            else:
                # heap is cleared and no tasks left
                if not tasks:
                    break
                # heap is cleared, but still have tasks
                # when the start time of the remaining tasks > last completion time
                else:
                    startTime = tasks[0][0]

        return ans
