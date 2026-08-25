class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        nums=[i%2 for i in nums]
        if nums[0]==1:
            nums=[1-i for i in nums ]
        ones=[]
        zeroes=[]
        for i in range(0,len(nums)):
            if nums[i]==1:
                ones.append(i)
            else:
                zeroes.append(i)
        if abs(len(ones)-len(zeroes))>1:
            return -1
        cnums=[1-i for i in nums]
        res=0
        l=0
        r=1
        res=0
        while l<len(nums):
            if nums[l]!=l%2:
                r=max(r,l+1)
                if r==len(nums):
                    res=-1
                    break
                while nums[r]==nums[l]:
                    r+=1
                    if r==len(nums):
                        res=-1
                        r=len(nums)+1
                        l=len(nums)
                        break
                nums[r]=1-nums[r]
                res+=r-l
            l+=1
        l=0
        r=1
        cres=0
        while l<len(cnums):
            if cnums[l]!=l%2:
                r=max(r,l+1)
                if r==len(nums):
                    cres= -1
                    break
                while cnums[r]==cnums[l]:
                    r+=1
                    if r==len(cnums):
                        cres=-1
                        r=len(nums)
                        l=len(nums)-1
                        break
                if r==len(cnums):
                        cres= -1
                        break
                cnums[r]=1-cnums[r]
                cres+=r-l
            l+=1
        if res==-1:
            return cres
        if cres==-1:
            return res
        return min(res,cres)


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna