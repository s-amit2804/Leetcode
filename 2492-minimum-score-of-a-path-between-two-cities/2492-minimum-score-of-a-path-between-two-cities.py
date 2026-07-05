class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        poss=set()
        vis=[[] for i in range (n+1)]
        for i in roads:
            vis[i[0]].append([i[1],i[2]])
            vis[i[1]].append([i[0],i[2]])
        q=[1]
        while q:
            x=q.pop(0)
            for i in vis[x]:
                if i[0] not in poss:
                    poss.add(i[0])
                    q.append(i[0])
        res=10000000
        for i in roads:
            if i[0] in poss:
                res=min(res,i[2])
        return res


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna