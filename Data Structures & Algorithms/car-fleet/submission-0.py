class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        car_stat=list(zip(position,speed))
        car_stat.sort(reverse=True)
        stack=[]
        for pos,sp in car_stat:
            time=(target-pos)/sp
            if not stack or time>stack[-1]:
                stack.append(time)
        return len(stack)        


