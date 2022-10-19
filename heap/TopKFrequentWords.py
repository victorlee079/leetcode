class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        '''
        1. Count the frequency of each word O(n)
        2. Use heap to return the k smallest item O(nlog(t))
            - item[1] : frequency
            - item[0] : word
           (-item[1], item[0]) means higher frequency and lexicographical smaller go first
        3. Return the words only
        '''
        return [i[0] for i in heapq.nsmallest(k, Counter(words).items(), key=lambda item : (-item[1], item[0]))]
