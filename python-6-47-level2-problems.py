# find in a list for nearby 3
def has_33(nums):
    for i in range(0,len(nums)-1):
        if nums[i] == 3 and nums[i+1] == 3:  # or nums[i:i+1] == [3,3]
            return True
    return False

print (has_33([1,3,3]))