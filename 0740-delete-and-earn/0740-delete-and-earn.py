class Solution:
    def deleteAndEarn(self, nums: list[int]) -> int:
        freq=dict()
        for i in nums:
            if i in freq:
                freq[i]+=1
            else:
                freq[i]=1
        unums=list(set(nums))
        unums.sort()
        @lru_cache(None)
        def helper(index):
            if index==len(unums):
                return 0
            res=helper(index+1)
            if index+1<len(unums) and unums[index+1]==unums[index]+1:
                res=max(res,unums[index]*freq[unums[index]]+helper(index+2))
            else:
                res=max(res,unums[index]*freq[unums[index]]+helper(index+1))
            return res
        return helper(0)

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna