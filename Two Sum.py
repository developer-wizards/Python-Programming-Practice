#Using dictionary - takes on average 40ms for execution
def twoSum(nums, target):
    residual = dict()
    for i, n in enumerate(nums):
        if n in residual: return sorted([i, residual[n]])
        else: residual[target - n] = i


#Using two pointer Solution - takes on average 90ms for execution
def TwoSum(nums, target):
    nums = enumerate(nums) #enumerate is a list of tuple, where tuple is(index, value) [(0,9),(1,4),(2,6),(3,3)]
    nums = sorted(nums, key = lambda x:x[1]) #Sorting list of tuple based on value i.e x[1] nums = [(3,3),(1,4),(2,6),(0,9)]
    l,u = 0, len(nums)-1 #l and u are initially pointing to the lower and upper bound of the sorted list
    while l<u:
        if(nums[l][1] + nums[u][1] == target):
            return(sorted([nums[l][0], nums[u][0]]))
        elif(nums[l][1] + nums[u][1] < target):
            l += 1
        else:
            u -= 1
        
            


#driver code 
nums = [9,4,6,3]
target = 9
result = twoSum(nums, target)
result_tp = TwoSum(nums, target)
print(result); print(result_tp)

#driver code 


