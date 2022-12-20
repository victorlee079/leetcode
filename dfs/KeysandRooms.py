class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        n = len(rooms)
        visited = set()
        visited.add(0)
        keys = []
        keys += rooms[0]
        while keys:
            num_of_keys = len(keys)
            for i in range(num_of_keys):
                key = keys.pop()
                if key not in visited:
                    visited.add(key)
                    keys += rooms[key]
        return len(visited) == n
