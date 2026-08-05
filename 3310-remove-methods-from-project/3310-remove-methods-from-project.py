class Solution:
    def remainingMethods(self, n: int, k: int, inv: List[List[int]]) -> List[int]:
        p=[False]
        def bfs(node,newvis,p):
            if vis[node]==1:
                p[0]=True
            if newvis[node]==0:
                newvis[node]=1
                res.append(node)
                for i in adj[node]:
                    bfs(i,newvis,p)
                return
        adj=[[] for i in range(n)]
        for i in inv:
            adj[i[0]].append(i[1])
        vis=[0]*(n)
        q=[k]
        while q:
            x=q.pop(0)
            vis[x]=1
            for i in range(0,len(adj[x])):
                if vis[adj[x][i]]==0:
                    q.append(adj[x][i])
        newvis=[0]*(n+1)
        res=[]
        for i in range(0,n):
            if vis[i]==0 and newvis[i]==0:
                bfs(i,newvis,p)
        # print(p)
        if p[0]:
            return [i for i in range (n)]
        return res


                    

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna