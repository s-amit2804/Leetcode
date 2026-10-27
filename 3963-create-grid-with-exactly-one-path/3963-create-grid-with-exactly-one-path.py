class Solution:
    def createGrid(self, m: int, n: int) -> list[str]:
        return ["."+"#"*(n-1) for i in range(0,m-1)] + ["."*n]


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna