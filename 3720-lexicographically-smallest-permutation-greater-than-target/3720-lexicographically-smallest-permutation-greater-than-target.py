class Solution:
    def lexGreaterPermutation(self, s: str, target: str) -> str:
        def poss(s,freq):
            r=[]
            for i in range(25,-1,-1):
                if freq[i]>0:
                    r.append(chr(ord('a')+i)*freq[i])
            return "".join(r)>s

        freq=[0 for i in range (0,26)]
        for i in s:
            freq[ord(i)-ord('a')]+=1
        res=[]
        for i in range(0,len(target)):
            if freq[ord(target[i])-ord('a')]>0:
                freq[ord(target[i])-ord('a')]-=1
                if poss(target[i+1:],freq):
                    res.append(target[i])
                    continue
                freq[ord(target[i])-ord('a')]+=1
                for x in range(ord(target[i])-ord('a')+1,26):
                    if freq[x]>0:
                        res.append(chr(ord('a')+x))
                        freq[x]-=1
                        for p in range(0,26):
                            if freq[p]>0:
                                res.append(chr(p+ord('a'))*freq[p])
                        return "".join(res)
                return ""
            else:
                for x in range(ord(target[i])-ord('a')+1,26):
                    if freq[x]>0:
                        res.append(chr(ord('a')+x))
                        freq[x]-=1
                        for p in range(0,26):
                            res.append(chr(p+ord('a'))*freq[p])
                        return "".join(res)
                return ""
        return "".join(res)

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna