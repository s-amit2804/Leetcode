class Solution:
    def canAliceWin(self, n: int) -> bool:
        i=10
        while n>=0:
            n-=i
            if n<0:
                if i%2==0:
                    return False
                else:
                    return True
            i-=1
        return False

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna