class Solution:
    def maxTaxiEarnings(self, n: int, rides: List[List[int]]) -> int:
        @lru_cache(None)
        def helper(index):
            print(index)
            if index>=n:
                return 0
            r=0
            for i in poss[index]:
                r=max(r,i[1]+helper(i[0])+i[0]-index)
            # print(index,max(helper(index+1),r))
            return max(helper(index+1),r)
        poss=[[] for i in range (0,n)]
        poss[0]=[]
        for i in rides:
            poss[i[0]].append([i[1],i[2]])
        # print(poss)
        return helper(1)

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna