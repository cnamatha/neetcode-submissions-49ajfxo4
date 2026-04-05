class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res=[]
        candidates.sort()
        def bck(start,path,net):
            if net==0:
                res.append(path[:])
                return
            if net<0:
                return
            for i in range(start,len(candidates)):
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                path.append(candidates[i])
                bck(i+1,path,net-candidates[i])
                path.pop()
        bck(0,[],target)
        return res                  