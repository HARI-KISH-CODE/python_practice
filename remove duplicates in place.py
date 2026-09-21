def dup(nums):
  n=len(nums)
  s=0
  for i in range(1,n):
    if nums[i]!=nums[s]:
      s+=1
      nums[s]=nums[i]
  return nums
  
