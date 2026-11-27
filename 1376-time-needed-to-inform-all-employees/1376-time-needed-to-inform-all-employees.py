class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: list[int], informTime: list[int]) -> int:
        @cache
        def helper(i):
            if manager[i]==-1:
                return informTime[i]
            return informTime[i]+helper(manager[i])
        hasboss=set()
        for i in manager:
            hasboss.add(manager[i])
        res=0
        for i in range(0,n):
            if i not in hasboss:
                res=max(res,helper(i))
        return res


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna