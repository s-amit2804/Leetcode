class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        def helper(x):
            sum=0
            while x>0:
                sum+=x%10
                x=x//10
            return sum
        nnums=nums[:]
        nnums.sort(key=lambda x:(helper(x),x))
        res=0
        actual=dict()
        n=len(nums)
        for i in range(0,n):
            actual[i]=nnums[i]
        present=dict()
        for i in range(n):
            present[nums[i]]=i
        for i in range(0,n):
            j=present[actual[i]]
            if i!=j:
                res+=1
                nums[i],nums[j]=nums[j],nums[i]
                present[nums[i]]=i
                present[nums[j]]=j
        return res

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna