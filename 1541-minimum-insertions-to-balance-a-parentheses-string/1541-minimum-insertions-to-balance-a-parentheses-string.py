class Solution:
    def minInsertions(self, s: str) -> int:
        news=[]
        res=0
        i=0
        while i<len(s):
            if s[i]==')':
                if i==len(s)-1 or s[i+1]!=')':
                    res+=1
                    news.append(")")
                else:
                    news.append(")")
                    i+=1
            else:
                news.append("(")
            i+=1
        # print(res)
        c=0
        for i in news:
            if i==")":
                c-=1
            else:
                c+=1
            if c<0:
                res+=abs(c)
                c=0
        return res+2*c


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna