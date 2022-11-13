'''


    Time Complexity: O(N2)O(N^2)O(N2), where NNN is the length of s.
        If k = 1, we need O(N)O(N)O(N) time to build each new string and O(N)O(N)O(N) time to check whether it's the lexicographically smallest string among the strings generated so far. In total, there are NNN such different strings to build and check. Therefore, the time complexity for this case is O(N2)O(N^2)O(N2).
        If k > 1, we need to convert our given string to an array of characters (this costs O(N)O(N)O(N) time), then sort the newly obtained array (sorting takes O(Nlog⁡N)O(N \log N)O(NlogN) time), and build the output string from the sorted array which takes O(N)O(N)O(N) time.
        Thus, the worst-case scenario is when k is 1, so the overall time complexity of the solution is O(N2)O(N^2)O(N2).

    Space Complexity: O(N)O(N)O(N).
        If k = 1, we need the space to store only two strings: the lexicographically smallest string found so far and a newly built string, that will be compared to the lexicographically smallest string. This requires O(N)O(N)O(N) space.
        If k > 1, we need O(N)O(N)O(N) space to store the character array. Other than that, sorting the array requires O(log⁡N)O(\log N)O(logN) additional space for Java and O(N)O(N)O(N) additional space for Python.
        Therefore, the overall space complexity of the solution is O(N)O(N)O(N).
        
'''
class Solution:
    def orderlyQueue(self, s: str, k: int) -> str:
        if k == 1:
            # Look for smallest string formed by splitting s
            return min(s[i:] + s[:i] for i in range(len(s)))
        else:
            return "".join(sorted(list(s)))
