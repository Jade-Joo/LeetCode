from collections import defaultdict
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        courses = defaultdict(list)
        for a, b in prerequisites:
            courses[a].append(b)

        temp = set()
        visited = set()
        def dfs(n):
            if n in temp:
                return False
            if n in visited:
                return True
            
            temp.add(n)
            for i in courses[n]:
                if not dfs(i):
                    return False
            temp.remove(n)
            visited.add(n)
            return True
        
        for i in list(courses.keys()):
            if not dfs(i):
                return False
        return True