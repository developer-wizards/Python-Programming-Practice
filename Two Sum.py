def twoSum(nums, target):
    residual = dict()
    for i, n in enumerate(nums):
        if n in residual: return [i, residual[n]]
        else: residual[target - n] = i


#driver code
nums = [9,4,6,3]
target = 9
result = twoSum(nums, target)
print(result)
