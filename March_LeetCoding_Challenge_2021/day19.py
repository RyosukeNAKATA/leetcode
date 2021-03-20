"""
Question: Keys and Rooms
There are N rooms and you start in room 0.  Each room has a distinct number in 0, 1, 2, ..., N-1, and each room may have some keys to access the next room. 
Formally, each room i has a list of keys rooms[i], and each key rooms[i][j] is an integer in [0, 1, ..., N-1] where N = rooms.length.  A key rooms[i][j] = v opens the room with number v.
Initially, all the rooms start locked (except for room 0). 
You can walk back and forth between rooms freely.
Return true if and only if you can enter every room.

Note:
- 1 <= rooms.length <= 1000
- 0 <= rooms[i].length <= 1000
- The number of keys in all rooms combined is at most 3000.
"""
class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        key_queue = []
        visited = [False] * len(rooms)
        for keys in rooms[0]:
            key_queue.append(keys)
        visited[0] = True
        while(key_queue):
            out = key_queue.pop(0)
            if visited[out] != True:
                for keys in rooms[out]:
                    key_queue.append(keys)
                visited[out] = True
        return True if all(visited) else False