class Solution:
    def __init__(self):
        self.counts = []
        
        for i in range(31):
            self.counts.append(Counter(str(2 ** i)))
    
    def reorderedPowerOf2(self, n: int) -> bool:
        return Counter(str(n)) in self.counts
            
