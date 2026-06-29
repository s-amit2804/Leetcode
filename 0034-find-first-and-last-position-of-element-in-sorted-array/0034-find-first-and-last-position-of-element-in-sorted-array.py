class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if len(nums)==0:
            return [-1,-1]
        st=0
        lst=len(nums)-1
        while st<lst:
            mid=(st+lst)//2
            if nums[mid]>target:
                lst=mid
            elif nums[mid]<target:
                st=mid+1
            else:
                lst=mid
                # break
        if nums[st]==target:
            res=[st]
        else:
            res=[-1]
        st=0
        lst=len(nums)-1
        while st<lst:
            mid=(st+lst)//2
            if nums[mid]>target:
                lst=mid
            elif nums[mid]<target:
                st=mid+1
            else:
                st=mid+1
        if nums[st]==target:
            res.append(st)
        elif nums[st-1]==target:
            res.append(st-1)
        else:
            res.append(-1)
        return res

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna