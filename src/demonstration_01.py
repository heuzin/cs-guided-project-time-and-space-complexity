"""
Given an array of integers `nums` and an integer `target`, return the indices
of the two numbers that add up to the `target`.

Examples:

- two_sum(nums = [2,5,9,13], target = 7) -> [0,1] (nums[0] + nums[1] == 7)
- two_sum(nums = [4,3,5], target = 8) -> [1,2] (nums[1] + nums[2] == 8)

Notes:

- Each input will have only one solution.
- You may not use the same element twice.
- You can return the answer in any order.
"""
def two_sum(nums, target): #o(n) x o(n) = o(n^2) - LINEAR
    # Your code here
    for i in range(len(nums)): # o(n)
        for j in range(i + 1, len(nums)): # o(n)
            num1 = nums[i]
            num2 = nums[j]
            if num1 + num2 == target:
                return [i, j]
    
    return None

print(two_sum(nums = [2, 5, 9, 15], target = 7))