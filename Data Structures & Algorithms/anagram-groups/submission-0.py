class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res_map=defaultdict(list)
        for word in strs:
            Alpha=[0]*26
            for i in word:
                Alpha[ord(i)-ord("a")]+=1
            res_map[tuple(Alpha)].append(word)
        return list(res_map.values())       
