class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        res=[]
        def check(i):
            enddig=(i+1)
            for x in range(10):
                if low<=i<=high:
                    res.append(i)
                if enddig==10:
                    return
                i=i*10+enddig
                enddig=(enddig+1)
        for i in range(1,10):
            check(i)
        return sorted(res)


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna