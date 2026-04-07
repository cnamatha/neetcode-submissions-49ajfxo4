class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        hashmap={}
        for h in hand:
            hashmap[h]=hashmap.get(h,0)+1
        hand.sort()
        for h in hand:
            while hashmap[h]>0:
                for i in range(groupSize):
                    if hashmap.get(h+i,0)==0:
                        return False
                    hashmap[h+i]-=1
        return True                      

