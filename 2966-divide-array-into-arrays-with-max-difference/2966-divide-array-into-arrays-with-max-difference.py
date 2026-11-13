class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        res=[]
        nums.sort()
        for i in range(0,len(nums)//3):
            curarr=nums[i*3:i*3+3]
            if curarr[2]-curarr[0]<=k:
                res.append(curarr)
            else:
                return []
        return res

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna