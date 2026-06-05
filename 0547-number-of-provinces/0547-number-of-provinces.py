class Solution:
    def findCircleNum(self, isc: List[List[int]]) -> int:
        vis=set()
        res=0
        for i in range (0,len(isc)):
            if i in vis:
                continue
            vis.add(i)
            res+=1
            x=[i]
            while x:
                cur=x.pop()
                for p in range(0,len(isc)):
                    if isc[cur][p]==1 and p not in vis:
                        vis.add(p)
                        x.append(p)
        return res

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/leethub-v4/bcilpkkbokcopmabingnndookdogmbna