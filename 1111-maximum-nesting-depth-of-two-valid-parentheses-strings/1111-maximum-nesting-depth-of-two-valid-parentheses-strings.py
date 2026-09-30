class Solution:
    def maxDepthAfterSplit(self, seq: str) -> list[int]:
        res=[0]*len(seq)
        c=0
        r=0
        for i in range(0 , len(seq)):
            if seq[i]=="(":
                c+=1
            else:
                c-=1
            r=max(r,c)
        c=0
        for i in range(0 , len(seq)):
            if seq[i]=="(":
                c+=1
                if c>r//2:
                    res[i]=1
            else:
                if c>r//2:
                    res[i]=1
                c-=1
        return res

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna