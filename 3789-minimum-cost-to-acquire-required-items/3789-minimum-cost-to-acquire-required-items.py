class Solution:
    def minimumCost(self, cost1: int, cost2: int, costBoth: int, need1: int, need2: int) -> int:
        res=0
        if costBoth<=cost1+cost2:
            res+=costBoth*(min(need1,need2))
            if need1<need2:
                need2-=need1
                need1=0
            else:
                need1-=need2
                need2=0
        if costBoth<=cost1 :
            res+=costBoth*(need1)
            need2=max(0,need2-need1)
            need1=0
        # print(need1,need2)
        if costBoth<=cost2 :
            res+=costBoth*(need2)
            need1=max(0,need1-need2)
            need2=0
        # print(need1,need2)
        res+=need1*cost1+need2*cost2
        return res
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna