# Given an integer array nums, return an array answer such that answer[i] is equal
# to the product of all the elements of nums except nums[i].

# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

# You must write an algorithm that runs in O(n) time and without using the division operation.

# Example 1:

# Input: nums = [1,2,3,4]
# Output: [24,12,8,6]

# Example 2:
# Input: nums = [-1,1,0,-3,3]
# Output: [0,0,9,0,0]

# The time complexity of this solution is O(n^2) because for each element in the input array,
# we are iterating through the entire array to calculate the product of all other elements.

# The space complexity is O(n) because we are creating a new array to store the results.

class Solution:
    def productExceptSelf(self, nums):
        result = []
        def multiply(nums):
            product = 1
            for n in nums:
                product *= n
            return product
        for n in range(len(nums)):
            temp = nums[n]
            nums[n] = 1
            product_of_array = multiply(nums)
            result.append(product_of_array)
            nums[n] = temp
        return print(result)

# answer = Solution()
# answer.productExceptSelf([5, 2, 3, 4])
    
# The time complexity of this solution is O(n), where n is the length of the input array nums.
# This is because we iterate through the array twice, once to calculate the prefix products and 
# once to calculate the postfix products. Each iteration takes O(n) time.

# The space complexity of this solution is O(1) because we are using a constant amount
# of extra space to store the prefix and postfix products.
# We are not using any additional data structures that depend on the size of the input array.

class Solution:
    def productExceptSelf(self, nums):
        result = [1] * len(nums)
        prefix = 1
        for i in range(len(nums)):
            result[i] = prefix
            prefix *= nums[i]
        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            result[i] *= postfix
            postfix *= nums[i]
        return(print(result))
answer2 = Solution()
answer2.productExceptSelf([1, 2, 3, 4])