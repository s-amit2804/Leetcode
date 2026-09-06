class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        i=0
        j=0
        res=[]
        while i<len(mat) or j<len(mat[0]):
            #topright
            while i>=0 and j<len(mat[0]):
                res.append(mat[i][j])
                i-=1
                j+=1
            i+=1
            j-=1
            if j+1<len(mat[0]):
                j+=1
            else:
                i+=1
            #bottomleft
            while j>=0 and i<len(mat):
                res.append(mat[i][j])
                j-=1
                i+=1
            j+=1
            i-=1
            if i+1<len(mat):
                i+=1
            else:
                j+=1
        # if (len(mat)+len(mat[0])-1)%2==1:
        #     res.append(mat[-1][-1])
        return res


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna