class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        def dfs(node,x):
            if vis[node]!=-1:
                return
            vis[node]=x
            for i in adj[node]:
                if vis[i]==-1:
                    dfs(i,x)
            return
        vis=[-1]*n
        x=0
        adj=[[] for i in range(n)]
        for i in edges:
            adj[i[0]].append(i[1])
            adj[i[1]].append(i[0])
        c=0
        for i in range(n):
            if vis[i]==-1:
                dfs(i,x)
                x+=1
                c+=1
        # print(vis)
        l=[[] for i in range(c)]
        count=[0]*c
        res=0
        for i in vis:
            count[i]+=1
        for i in edges:
            l[vis[i[0]]].append(edges)
        for i in range(0,len(l)):
            if len(l[i])==(count[i]*(count[i]-1))//2:
                res+=1
        return res


        

            

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna