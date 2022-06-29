class Solution:
    def minDeletions(self, s: str) -> int:
        
        # Store the frequency of each character
        frequency = [0] * 26
        for char in s:
            frequency[ord(char) - ord('a')] += 1
        
        delete_count = 0
        # Use a set to store the frequencies we have already seen
        seen_frequencies = set()
        for i in range(26):
            # Keep decrementing the frequency until it is unique
            while frequency[i] and frequency[i] in seen_frequencies:
                frequency[i] -= 1
                delete_count += 1
                
            # Add the newly occupied frequency to the set
            seen_frequencies.add(frequency[i])
        
        return delete_count
    
    # Time complexity: O(N+Klog⁡K)
    def minDeletionsHeap(self, s: str) -> int:
        
        frequency = [0] * 26
        # O(N)
        for char in s:
            frequency[ord(char) - ord('a')] += 1
        
        heap = [-freq for freq in frequency if freq != 0]
        heapq.heapify(heap)
        
        delete_count = 0
        
        while len(heap) > 1:
            top = -heapq.heappop(heap)
            
            if top == -heap[0]:
                top -= 1
                delete_count += 1
                # Only push back when the frequency > 0
                if top > 0:
                    heapq.heappush(heap, -top)
                
        return delete_count
