class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        nums=[abs(i) for i in nums]
        nums.sort()
        n=len(nums)
        psum=0
        nsum=0
        print(nums)
        for i in range(0,n//2):
            nsum+=nums[i]*nums[i]
        for i in range(n//2,n):
            psum+=nums[i]*nums[i]
        return psum-nsum

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna