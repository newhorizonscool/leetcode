class Solution:
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            for j in range(len(nums)):
                if(i != j and nums[i] + nums[j] == target):
                    index = []
                    index.append(i)
                    index.append(j)
                    return index


