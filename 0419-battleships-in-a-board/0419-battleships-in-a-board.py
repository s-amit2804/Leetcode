class Solution:
    def countBattleships(self, board: list[list[str]]) -> int:
        res=0
        for i in range(0,len(board)):
            for j in range(0,len(board[0])):
                if board[i][j]=='X':
                    res+=1
                    a=i
                    b=j
                    while a+1<len(board) and board[a+1][b]=='X':
                        board[a+1][b]='.'
                        a+=1
                    a=i
                    while b+1<len(board[0]) and board[a][b+1]=='X':
                        board[a][b+1]='.'
                        b+=1
        return res

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna