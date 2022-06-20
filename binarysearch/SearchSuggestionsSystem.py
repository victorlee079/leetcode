from bisect import bisect


class Solution:
    def suggestedProducts(self, A, word):
        A.sort()
        res, prefix, i = [], '', 0
        for c in word:
            prefix += c
            i = bisect.bisect_left(A, prefix, i)
            res.append([w for w in A[i:i + 3] if w.startswith(prefix)])
        return res
    
    def suggestedProducts2(self, products: List[str], searchWord: str) -> List[List[str]]:
        def search(prefix, products):
            n = len(products)
            l, r = 0, n-1
            
            while l <= r:
                mid = l + (r - l) // 2
                if prefix <= products[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            return l
        
        products.sort()
        
        res = []
        
        for i in range(len(searchWord)):
            matches = []
            prefix = searchWord[:i+1]
            index = search(prefix, products)
            for item in products[index:index+3]:
                if item.startswith(prefix):
                    matches.append(item)
                else:
                    break
            res.append(matches)
        return res
                    
