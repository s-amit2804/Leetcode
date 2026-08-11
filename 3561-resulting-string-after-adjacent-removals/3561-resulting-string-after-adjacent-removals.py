class Solution:
    def resultingString(self, s: str) -> str:
        res=[]
        for i in list(s):
            if len(res)==0:
                res.append(i)
            elif abs(ord(i)-ord(res[-1]))%24==1:
                res.pop(len(res)-1)
            else:
                res.append(i)
        return "".join(res)



# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna