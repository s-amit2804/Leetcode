class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # s=s.lower()
        # t=t.lower()
        def poss(tarr,sarr):
            for i in range(0,58):
                if curf[i]<freq[i]:
                    return False
            return True
        l=0
        res=1000000
        r=0
        freq=[0 for i in range(58)]
        for i in t:
            freq[ord(i)-ord('A')]+=1
        curf=[0 for i in range(58)]
        ans=[]
        while r<len(s):
            curf[ord(s[r])-ord('A')]+=1
            while l<r and poss(curf,freq):
                if poss(curf,freq):
                    if r-l<res:
                        res=r-l
                        ans=[l,r]
                curf[ord(s[l])-ord('A')]-=1
                l+=1
            if poss(curf,freq):
                    if r-l<res:
                        res=r-l
                        ans=[l,r]
            r+=1
        if len(ans)==0:
            return ""
        return s[ans[0]:ans[1]+1]

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna