class Solution:
    def earliestFinishTime(self, lstart: List[int], ldur: List[int], wstart: List[int], wdur: List[int]) -> int:
        x=1000000
        y=1000000
        for i in range (0,len(lstart)):
            x=min(x,lstart[i]+ldur[i])
        for j in range (0,len(wstart)):
            y=min(y,max(wstart[j],x)+wdur[j])
            
        x=1000000
        yy=1000000
        for i in range (0,len(wstart)):
            x=min(x,wstart[i]+wdur[i])
        for j in range (0,len(lstart)):
            yy=min(yy,max(lstart[j],x)+ldur[j])
        return min(y,yy)