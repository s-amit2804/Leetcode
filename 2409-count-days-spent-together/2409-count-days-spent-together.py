class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        days=[31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        alice_arr=int(arriveAlice[3:])+sum(days[:int(arriveAlice[:2])-1])
        alice_leave=int(leaveAlice[3:])+sum(days[:int(leaveAlice[:2])-1])
        Bob_arr=int(arriveBob[3:])+sum(days[:int(arriveBob[:2])-1])
        Bob_leave=int(leaveBob[3:])+sum(days[:int(leaveBob[:2])-1])
        # print(sum(days[:int(leaveAlice[:2])]),sum(days[:int(arriveBob[:2])]),alice_arr,alice_leave,Bob_arr,Bob_leave)
        return max(0,min(Bob_leave,alice_leave)-max(alice_arr,Bob_arr)+1)

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna