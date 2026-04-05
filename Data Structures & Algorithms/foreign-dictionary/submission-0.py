class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        graph=defaultdict(set)
        indegree={c:0 for word in words for c in word}
        for i in range(len(words)-1):
            a,b=words[i],words[i+1]
            min_len=min(len(a),len(b))
            if a[:min_len]==b[:min_len] and len(a)>len(b):
                return ""
            for j in range(min_len):
                if a[j]!=b[j]:
                    if b[j] not in graph[a[j]]:
                        graph[a[j]].add(b[j])
                        indegree[b[j]]+=1
                    break
        q=deque([c for c in indegree if indegree[c]==0])
        res=[]
        while q:
            ch=q.popleft()
            res.append(ch)
            for nei in graph[ch]:
                indegree[nei]-=1
                if indegree[nei]==0:
                    q.append(nei)
        return "".join(res) if len(res)==len(indegree) else ""            


