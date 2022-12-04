nums = [0,1,0,3,12]
# answer: [1,3,12,0,0]
#for i in range(len(nums)):
   # if (nums[i] == 0 and i < len(nums) -1):
        #nums[i], nums[i+1] = nums[i+1], nums[i]
#i = 0
#while i <= len(nums):
    if (nums[i] == 0 and i <= len(nums) - 1):
        nums[i], nums[i+1] = nums[i+1], nums[i]
        i += 1
    if i == len(nums) - 1:
        break
    print(nums)
#print(nums)



        

