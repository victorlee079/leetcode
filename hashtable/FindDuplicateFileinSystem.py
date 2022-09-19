"""
BFS vs DFS

BFS explores neighbors first. This means that files which are located close to each other are also accessed one after another. This is great for space locality and that's why BFS is expected to be faster. Also, BFS is easier to parallelize (more fine-grained locking). DFS will require a lock on the root node.

Very large files and false positives

For very large files we should do the following comparisons in this order:

    compare sizes, if not equal, then files are different and stop here!
    hash them with a fast algorithm e.g. MD5 or use SHA256 (no collisions found yet), if not equal then stop here!
    compare byte by byte to avoid false positives due to collisions.

Have you used an IDE in remote development mode?
For example, CLion has some options on how to compare the local files with the remote server files and then decides to synchronize or not.

Complexity

Runtime - Worst case (which is very unlikely to happen): O(N^2 * L) where L is the size of the maximum bytes that need to be compared
Space - Worst case: all files are hashed and inserted in the hashmap, so O(H^2*L), H is the hash code size and L is the filename size
"""
# O(nx) n strings of average length xxx is parsed.
class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        ans = []
        
        d = defaultdict(list)
        
        for path in paths:
            path, *files = path.split(" ")
            for f in files:
                start, end = f.rindex("("), f.rindex(")")
                fname = f[:start]
                content = f[start+1:end+1]
                d[content].append(path + "/" + fname)
                
        for k, v in d.items():
            if len(v) > 1:
                ans.append(v)
        
        return ans
                
