class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0

        wordList.append(beginWord)
        nei=defaultdict(list)
        for word in wordList:
            for i in range(len(word)):
                pattern=word[:i]+"*"+word[i+1:]
                nei[pattern].append(word)
        visited={beginWord}        
        q=deque([(beginWord,1)])
        while q:
            word,count=q.popleft()
            if word==endWord:
                return count
            for i in range(len(word)):
                pattern=word[:i]+"*"+word[i+1:]
                for e in nei[pattern]:
                    if e not in visited:
                        visited.add(e)
                        q.append((e,count+1))
                nei[pattern]=[]
        return 0          
