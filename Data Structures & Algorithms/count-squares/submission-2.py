class CountSquares:

    def __init__(self):
        self.point_set=set()
        self.point_count={}
        

    def add(self, point: List[int]) -> None:
            if tuple(point) in self.point_set:
                self.point_count[tuple(point)]+=1
            else:
                self.point_count[tuple(point)]=1
                self.point_set.add(tuple(point))    


    def count(self, point: List[int]) -> int:
        res=0
        x,y=point
        for x1,y1 in self.point_set:
            if abs(x-x1)==abs(y-y1) and (x1!=x):
                if (x,y1) in self.point_set and (x1,y) in self.point_set:
                    res+=(self.point_count[(x,y1)])*(self.point_count[(x1,y)])*self.point_count[(x1,y1)]
        return res            


        
