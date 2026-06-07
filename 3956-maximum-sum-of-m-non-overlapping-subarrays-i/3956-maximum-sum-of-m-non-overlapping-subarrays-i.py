class Solution:
    def maximumSum(self, nums: List[int], gm: int, l: int, r: int) -> int:
        if(l==1 and gm==len(nums)):
            nums.sort()
            i=len(nums)-2
            res=nums[-1]
            while i>=0 and nums[i]>0:
                res+=nums[i]
                i-=1
            return res
        dp=[dict() for i in range(len(nums))]
        def helper(index,m):
            # print(index,m)
            if m==0:
                return 0
            if index+l-1>=len(nums):
                if m==gm:
                    return float('-inf')
                return 0
            if m in dp[index]:
                return dp[index][m]
            sum=0
            for i in range(0,l):
                sum+=nums[i+index]
            # print(sum)
            pm=helper(index+1,m)
            pm=max(pm,sum+helper(index+l,m-1))
            for i in range (index+l,index+r):
                if i<len(nums):
                    sum+=nums[i]
                else:
                    break
                pm=max(pm,sum+helper(i+1,m-1))
            dp[index][m]=pm
            return pm
        return helper(0,gm)

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/leethub-v4/bcilpkkbokcopmabingnndookdogmbna