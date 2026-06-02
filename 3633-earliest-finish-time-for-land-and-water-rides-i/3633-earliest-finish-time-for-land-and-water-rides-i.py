class Solution:
    def earliestFinishTime(self, landStartTime: List[int], landDuration: List[int], waterStartTime: List[int], waterDuration: List[int]) -> int:
        res=1000000
        for i in range (0,len(landStartTime)):
            for j in range(0,len(waterDuration)):
                res=min(res,max(landStartTime[i]+landDuration[i],waterStartTime[j])+waterDuration[j])
        for i in range (0,len(waterStartTime)):
            for j in range(0,len(landDuration)):
                res=min(res,max(waterStartTime[i]+waterDuration[i],landStartTime[j])+landDuration[j])
        return res