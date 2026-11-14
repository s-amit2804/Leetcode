class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        res=0
        msumm=100000000000
        summ=0
        for i in range(0,len(nums)):
            summ=0
            for j in range(i,len(nums)):
                summ+=nums[j]
                if l<=j-i+1<=r and summ<msumm and summ>0:
                    msumm=summ
                    res=j-i+1
        if msumm==100000000000:
            return -1
        return msumm


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna