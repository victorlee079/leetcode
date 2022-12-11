class Solution:
    # TLE
    def jobSchedulingRecur(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        jobs = sorted(zip(startTime, endTime, profit),
                      key=lambda item: item[1])
        n = len(jobs)

        @lru_cache(maxsize=None)
        def recur(ret, i, end):
            if i == n:
                return ret

            # Start Time >= Last End Time
            if jobs[i][0] >= end:
                # Take the job or not take the job
                return max(recur(ret + jobs[i][2], i+1, jobs[i][1]), recur(ret, i+1, end))
            else:
                return recur(ret, i+1, end)

        return recur(0, 0, 0)

    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        jobs = sorted(zip(startTime, endTime, profit),
                      key=lambda item: item[1])
        n = len(jobs)
        dp = [0] * n
        start, end, dp[0] = jobs[0]

        def findLastNonConflictingJob(jobs, n):
            # search space
            low, high = 0, n
            # iterate till the search space is exhausted
            while low <= high:
                mid = (low + high) // 2
                if jobs[mid][1] <= jobs[n][0]:
                    if jobs[mid + 1][1] <= jobs[n][0]:
                        low = mid + 1
                    else:
                        return mid
                else:
                    high = mid - 1
            # return the negative index if no non-conflicting job is found
            return -1

        for i in range(1, n):
            index = findLastNonConflictingJob(jobs, i)
            profit = jobs[i][2]
            if index > -1:
                profit += dp[index]
            dp[i] = max(profit, dp[i-1])

        return dp[-1]
