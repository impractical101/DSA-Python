class Solution:
    def search(self, nums: List[int], target: int) -> int:
        dict1 = {nums[i]:i for i in range(len(nums))}
        nums = sorted(nums)
        low, hi = 0, len(nums) - 1
        while(low <= hi):
            mid = low + (hi - low) // 2
            if target == nums[mid]:
                return dict1[nums[mid]]
            elif target > nums[mid]:
                low = mid + 1
            elif target < nums[mid]:
                hi = mid - 1
        return -1 

