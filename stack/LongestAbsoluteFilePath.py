class Solution:
    def lengthLongestPath(self, input: str) -> int:
        paths = input.split("\n")
        
        stk = []
        max_len = curr_len = 0
        
        for i in range(len(paths)):
            lvl, path = 0, paths[i]
            for j in range(len(path)):
                if path[j:j+1] == "\t":
                    lvl += 1
                else:
                    break
                    
            curr_path= path[lvl:]
            
            if lvl <= len(stk):
                while stk and len(stk) >= lvl+1:
                    prev_path = stk.pop()
                    curr_len -= len(prev_path)
                    
            stk.append(curr_path)
            curr_len += len(curr_path)
            if curr_path.find('.') > -1:
                max_len = max(max_len, curr_len + len(stk)-1)
        
        return max_len
