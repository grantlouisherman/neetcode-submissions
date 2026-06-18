class Solution:
    def binary_search(self, nums, target, N): # target is 9
        #[-1,0,3,5,9,12]
        mid = len(nums) // 2 #3
        print(nums)
        if len(nums) <= 0 or mid >= N:
            return -1
        if nums[mid][1] == target: # 5
            return nums[mid][0]
        if nums[mid][1] > target:
            return self.binary_search(nums[:mid], target, N)
        return self.binary_search(nums[mid+1:],target, N)
    
    def search(self, nums: List[int], target: int) -> int:
        for idx, num in enumerate(nums):
            nums[idx] = (idx, num)
        return self.binary_search(nums, target, len(nums))
    
        