class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count=Counter(tasks)
        max_freq=max(count.values())
        many=list(count.values()).count(max_freq)
        t=(max_freq-1)*(n+1)+many
        return max(len(tasks),t)