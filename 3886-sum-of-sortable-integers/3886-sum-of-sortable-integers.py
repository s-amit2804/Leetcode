class Solution:
    def sortableIntegers(self, nums: list[int]) -> int:
        def factors(n):
            ret=[]
            for i in range(1,n+1):
                if n%i==0:
                    ret.append(i)
            return ret
        def helper(n,sarr):
            # len=15 partion size=3 numparts=5
            for i in range(0,len(nums),n):
                #check if i-i+n are cyclic elements
                a=nums[i:i+n]
                b=sarr[i:i+n]
                # print(a,b)
                if not (''.join(map(str,b)) in ''.join(map(str,(a+a)))):
                    return False
            return True
                    
                
        arr=factors(len(nums))
        res=0
        rset=set()
        sarr=sorted(nums)
        for i in arr:
            if i in rset:
                continue
            if helper(i,sarr):
                res+=i
                rset.add(i)
                # for j in range(2,len(nums)//i):
                #     if j*i in arr and j*i not in rset:
                #         rset.add(i*j)
                #         res+=i*j
        return res

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna