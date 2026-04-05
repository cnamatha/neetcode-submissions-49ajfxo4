class Twitter:

    def __init__(self):
        self.time=0
        self.follows=defaultdict(set)
        self.tweets=defaultdict(list)
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.time+=1
        self.tweets[userId].append((self.time,tweetId))
        

    def getNewsFeed(self, userId: int) -> List[int]:
        res=[]
        heap=[]
        self.follows[userId].add(userId)
        for f in self.follows[userId]:
            if self.tweets[f]:
                index=len(self.tweets[f])-1
                time,tId=self.tweets[f][index]
                heapq.heappush(heap,(-time,tId,f,index-1))
        while heap and len(res)<10:
            time,tId,user,index=heapq.heappop(heap)
            res.append(tId)
            if index>=0:
                time,tId=self.tweets[user][index]
                heapq.heappush(heap,(-time,tId,user,index-1))
        return res               
        

    def follow(self, followerId: int, followeeId: int) -> None:
        self.follows[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.follows[followerId]:
            self.follows[followerId].remove(followeeId)
        
