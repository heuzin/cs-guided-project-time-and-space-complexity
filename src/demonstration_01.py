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
def two_sum(nums, target): # o(n) x o(n) = o(n^2) - 
    # Your code here
    for i in range(len(nums)): # o(n)
        for j in range(i + 1, len(nums)): # o(n)
            num1 = nums[i]
            num2 = nums[j]
            if num1 + num2 == target:
                return [i, j]
    
    return None

print(two_sum(nums = [2, 5, 9, 15], target = 7))

def two_sum_bettet_solution(nums, target): # o(n) + o(n) = o(n) - LINEAR - we add each instead of multply because they are not nested
    # store numbers in a dictionary
    # space
    num_dict = {} # o(n) space

    for i in range(len(nums)): # o(n)
        # Go though each number and store it in a dictionary with its value as index
        num_dict[nums[i]] = i
    
    for i in range(len(nums)): # o(n)
        # store current number in a variable
        current_num = nums[i]
        # check if compliment is in dict - compliment is the number needed to be added to current number to get to target
        compliment = target - current_num

        if compliment in num_dict and i != num_dict[compliment]:
            return [i, num_dict[compliment]]
    


print(two_sum_bettet_solution(nums = [4,3,5], target = 8))