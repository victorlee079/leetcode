class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        # min heap
        return [i[0] for i in heapq.nsmallest(k, Counter(words).items(), key=lambda item : (-item[1], item[0]))]
