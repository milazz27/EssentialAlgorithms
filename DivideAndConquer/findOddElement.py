"""
Problem Statement: We want to find the index where the sole odd element occurs within
    array A. This should run in at most O(log n)

Givens: A is an unsorted integer array of size n where all elements are even except 1.
    Array B represents the  summation of array A.

Algorithm: We will run a modified binary search algorithm to find the index where the
    odd number will occur in A by recursively searching through B. Instead of applying
    the > or < comparison to midpoint (like in traditional binary search), we will look
    to see if the midpoint is odd or even. Because an odd value is needed to sum to an even
    value we will explore the right half if mid is even or the left half if mid is odd.
"""

def modifiedBinarySearch(arr, low, high):
    """
    Modified binary search to find the odd index
    :param arr: array to search in
    :param low: lower bound of the array
    :param high: upper bound of the array
    :return: index of first odd element in the array, -1 if no such element exists
    """
    #Base case to handle invalid arrays
    if high < low:
        return -1
    mid = (high + low) // 2
    #midpoint is even --> search in right half
    if arr[mid] % 2 == 0:
        low = mid + 1
    #midpoint is odd --> search the lower half
    else:
        #check if this is the lowest odd index
        if arr[mid - 1] % 2 == 0 or mid == 0:
            return mid
        high = mid - 1
    #recurse
    return modifiedBinarySearch(arr, low, mid)

def findOddElement(array_A, array_B):
    """
    Handles base case and calls modifiedBinarySearch, returns final result
    :param array_A:
    :param array_B:
    :return:
    """
    length = len(array_A)
    if length == 2:
        if array_A[0] % 2 == 0:
            return array_A[1]
        else:
            return array_A[0]

    index = modifiedBinarySearch(array_A, 0, length - 1)

    return array_A[index - 1]

if __name__ == "__main__":

    #Testing
    A1 = [1,2]
    B1 = [1,3]

    A2 = [2,4,8,2,3,6]
    B2 = [2,6,14,16,19,25]

    result1 = findOddElement(A1, B1)
    assert result1 == 1

    result2 = findOddElement(A2, B2)
    assert result2 == 3

