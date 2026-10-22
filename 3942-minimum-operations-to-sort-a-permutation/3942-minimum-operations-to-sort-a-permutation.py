class Solution:
    def minOperations(self, nums: List[int]) -> int:
        res=1000000000
        ress=sorted(nums)
        if ress==nums:
            return 0
        if ress[::-1]==nums:
            return 1
        def helper(nums):
            i=0
            while i<len(nums)-1 and nums[i+1]>nums[i]:
                i+=1
            bpt=i #break point
            i+=1
            while i<len(nums)-1 and nums[i+1]>nums[i]:
                i+=1
            if i!=len(nums)-1:
                return False
            if nums[0]>nums[i]:
                return min(bpt+1,i-bpt+2)
            return False
        def helper2(nums):
            i=0
            while i<len(nums)-1 and nums[i+1]<nums[i]:
                i+=1
            bpt=i #break point
            i+=1
            while i<len(nums)-1 and nums[i+1]<nums[i]:
                i+=1
            if i!=len(nums)-1:
                return False
            if nums[i]>nums[0]:
                # print(i,bpt,nums)
                return min(bpt+2,1+i-bpt)
            return False
        if helper(nums):
            res=min(res, helper(nums))
        if helper(nums[::-1]):
            res=min(res,helper(nums[::-1])+1)
        if helper2(nums):
            res=min(res, helper2(nums))
        if helper2(nums[::-1]):
            res=min (res,helper2(nums[::-1])+1)
        if res==1000000000:
            return -1
        return res

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna