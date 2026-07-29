class Solution:
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        p1=len(nums1)-1
        res=0
        p2=len(nums2)-1
        while p1>=0 and p2>=0:
            if nums1[p1]<=nums2[p2]:
                while nums1[p1]<=nums2[p2]:
                    p1-=1
                    if p1==-1:
                        return max(res,p2)
                res=max(res,p2-p1-1)
            else:
                p2-=1
        return res
                





# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna