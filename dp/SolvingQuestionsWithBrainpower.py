class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        @cache
        def helper(i):
            if i >= len(questions):
                return 0
            points, brainpower = questions[i]
            return max(points + helper(i + brainpower + 1), helper(i + 1))

        return helper(0)
