class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        hold=-prices[0]
        sell=0
        rest=0
        n=len(prices)
        for i in range(1,n):
            prev_hold,prev_sell,prev_rest=hold,sell,rest
            hold=max(prev_hold,prev_rest-prices[i])
            sell=prev_hold+prices[i]
            rest=max(prev_rest,prev_sell)
        return max(sell,rest)    