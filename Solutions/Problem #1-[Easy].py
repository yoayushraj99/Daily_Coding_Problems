# This problem was recently asked by Google.
#
# Given a list of numbers and a number k, return whether any two numbers from the list add up to k.
#
# For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.
#
# Bonus: Can you do this in one pass?


def checkSum(arr, k):
    for i in range(len(arr)):
        diff = k-arr[i]
        if diff in arr:
            return True
    return False


print(checkSum([10, 15, 3, 7], 17))  # TimeComplexity O(n)
