class Solution:
    def asteroidsDestroyed(self, mass: int, arr: list[int]) -> bool:
        arr.sort()
        for i in arr:
            if i>mass:
                return False
            else:
                mass+=i
        return True

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna