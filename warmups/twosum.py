class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        # Convert to sorted space O(nlgn)
        og_nums = nums
        nums = sorted(nums)
        
        # Find indexes in sorted space O(n)
        i = 0
        j = len(nums)-1
        while i < j and nums[i] + nums[j] != target:
            if nums[i] + nums[j] > target:
                j -= 1
            elif nums[i] + nums[j] < target:
                i += 1
                
        # Convert back to original space O(n)
        og_i = og_nums.index(nums[i])
        
        og_j = 0
        # If they are the same, find the second instance in original array
        if nums[i] == nums[j]: og_j += og_i + 1
        while og_nums[og_j] != nums[j]:
            og_j += 1
            
        return [ og_i, og_j ]
