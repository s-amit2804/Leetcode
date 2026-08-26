class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        l=0
        r=0
        res=s+"a"
        onec=0
        while r<len(s):
            # print(res)
            if s[r]=='1':
                onec+=1
            while onec>k:
                if s[l]=='1':
                    onec-=1
                l+=1
            while l<len(s) and s[l]=='0':
                l+=1
            if onec==k:
                if r-l+1<len(res):
                    res=s[l:r+1]
                elif r-l+1==len(res):
                    res=min(res,s[l:r+1])
            r+=1
        if res==s+"a":
            return ""
        return res

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna