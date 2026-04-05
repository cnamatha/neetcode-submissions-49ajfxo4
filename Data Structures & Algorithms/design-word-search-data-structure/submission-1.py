class WordDictionary:

    def __init__(self):
       self.root={} 

    def addWord(self, word: str) -> None:
        node=self.root
        for ch in word:
            if ch not in node:
                node[ch]={}
            node=node[ch]
        node["#"]={}        

        

    def search(self, word: str) -> bool:
        node=self.root
        def dfs(node,i):
            if i==len(word):
                return "#" in node 
            ch=word[i]
            if ch==".":
                for e in node:
                    if e!="#" and dfs(node[e],i+1):
                        return True
                return False
            else:
                if ch not in node:
                    return False
                return dfs(node[ch],i+1)
        return dfs(self.root,0)                             

