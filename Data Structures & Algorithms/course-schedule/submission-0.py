class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph={i:[] for i in range(numCourses)}
        for i,j in prerequisites:
            graph[i].append(j)
        state=[0]*numCourses    
        def dfs(c):
            if state[c]==1:
                return False
            if state[c]==2:
                return True
            state[c]=1    
            for prereq in graph[c]:
                if not dfs(prereq):
                    return False
            state[c]=2
            return True
        for c in range(numCourses):
            if not dfs(c):
                return False
        return True        

