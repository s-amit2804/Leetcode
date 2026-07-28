class Solution:
    def smallestPalindrome(self, s: str) -> str:
        arr=list(s)
        arr.sort()
        res=[]
        i=0
        finalchar=""
        while i<len(arr):
            if i==len(arr)-1:
                finalchar=arr[i]
                break
            if arr[i+1]==arr[i]:
                res.append(arr[i])
                i+=2
            else:
                finalchar=arr[i]
                i+=1
        return "".join(res)+finalchar+"".join(res[::-1])
        


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna