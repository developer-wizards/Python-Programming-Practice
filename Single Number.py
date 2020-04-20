"""
Given a non-empty array of integers, every element appears twice except for one. Find that single one.
Note:
Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?
Example:
Input: [2,2,1]
Output: 1

Input: [4,1,2,1,2]
Output: 4
"""
########################################################################################################################################################################
"""
Approach 1: List operation
Algorithm:
1. Iterate over all the elements in \text{nums}nums
2. If some number in \text{nums}nums is new to array, append it
3. If some number is already in the array, remove it

"""

def singleNumber1(nums):
    no_duplicate_list = []
    for i in nums:
        if i not in no_duplicate_list:
            no_duplicate_list.append(i)
        else:
            no_duplicate_list.remove(i)
    return no_duplicate_list.pop()


"""
Complexity Analysis:
Time Complexity: O(n^2), We iterate through nums, taking O(n) time. We search the whole list to find whether there is duplicate number, taking O(n) time
Because search is in the for loop so we have to multiply both time complexities which is O(n^2)

Space Comlexity: O(n)We need a list of size nn to contain elements in nums

"""

#######################################################################################################################################################################

"""
Approach 2: Hash Table [We use hash table to avoid the O(n) time for searching the elements.]
Algorithm
1.Iterate through all elements in nums and set up {key, value} pair
2.Return the element which appeared only once.
"""
def singleNumber2( nums):
    hash_table = dict()
    for i, n in enumerate(nums):
        if n not in hash_table:
            hash_table[n] = 1
        else:
            hash_table[n] += 1

    for key, value in hash_table.items():
        if(value == 1):
            return key
        
#Using default dict:-
"""
from collections import defaultdict
def singleNumber2( nums):
    hash_table = defaultdict(int)
    for i in nums:
        hash_table[i] += 1
        
    for i in hash_table:
        if hash_table[i] == 1:
            return i

"""
"""
Time Complexity: O(n.1) = O(n).Time Complexity of for loop is O(n) and for hash operation is O(1).
Space Complexity: O(n) The space required by hash table is equal to the number of elements in nums
"""





########################################################################################################################################################################

"""
Approach 3: Math
Concept
2∗(a+b+c)−(a+a+b+b+c) = c
"""
def singleNumber3(nums):
    return 2 * sum(set(nums)) - sum(nums)

"""
Complexity Analysis
Time complexity : O(n + n) = O(n). sum will call next to iterate through nums. We can see it as sum(list(i, for i in nums)) which means the time complexity is O(n) because of the number of elements(n) in nums.
Space complexity : O(n + n) = O(n). set needs space for the elements in nums
"""

"""
Approach 4: Bit Manipulation
Concept
1. if we take XOR of zero and some bit, it will return that bit
 --> a XOR 0 = a
2. If we take XOR of two same bits, it will return 0
 --> a XOR a = 0
3. (a XOR b XOR a) = (a XOR a) XOR b = 0 XOR b = b
"""

def singleNumber4(nums):
    a = 0
    for i in nums:
        a ^= i
    return a

"""
Time complexity : O(n); Space Complexity: O(1)
"""

#Driver Code
nums = [4,1,2,1,2]
result1 = singleNumber1(nums)
result2 = singleNumber2(nums)
result3 = singleNumber3(nums)
result4 = singleNumber4(nums)
print("results of above four method are %d %d %d %d respectively " % (result1, result2, result3, result4) )

