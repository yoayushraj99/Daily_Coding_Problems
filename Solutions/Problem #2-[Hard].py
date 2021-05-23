# This problem was asked by Uber.
#
# Given an array of integers, return a new array such that each element at index i of the new array is
# the product of all the numbers in the original array except the one at i.
#
# For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24].
#
# Follow-up: what if you can't use division?

# METHOD - 1
import math


def Solution(arr):
    x = []
    for i in range(len(arr)):
        new_arr = math.prod(arr[:i] + arr[i + 1:])
        x.append(new_arr)

    return x


print(Solution([1, 2, 3, 4, 6]))  # TimeComplexity O(n^2)


# METHOD - 2

# def Solution(arr):
#
#     i = 0
#     left = arr[:i]
#     right = arr[i+1:]
#
#     while i <= len(arr):
#         

