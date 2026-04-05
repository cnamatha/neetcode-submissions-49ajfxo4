class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph={i:[] for i in range(numCourses)}
        for i,j in prerequisites:
            graph[i].append(j)
        state=[0]*numCourses
        res=[]    
        def dfs(i):
            if state[i]==1:
                return False
            elif state[i]==2:
                return True
            state[i]=1
            for nei in graph[i]:
                if not dfs(nei):
                    return False
            state[i]=2
            
            res.append(i)
            return True
        for i in range(numCourses):
            if not dfs(i):
                return []
        return res                             
