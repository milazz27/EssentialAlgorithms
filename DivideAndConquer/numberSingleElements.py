"""
Problem Statement: Given the sorted array A of size n, where n >= 2 and is a power of 2
    and where elements occur either once or twice. Create an algorithm to find the
    number of single numbers in the array that will have a runtime of O(n).

Algorithm Steps:
    1. Base Case: if n = 2 and A[1] == A[2] return 0, else if A[1] != A[2], return 2
    2. Divide: form the arrays L = [1 ... n/2] and R = [n/2 + 1 ... n].
    3. Recursively find the number of single elements in L and R (called l and r,
        respectively).
    4. Combine: if A[n/2] = A[n/2 + 1] return l + r - 2, else return l + r.

Runtime Analysis: 2 sub problems of size n/2 with a combine step runtime of O(1) yields
    a recurrence relation of:

        T(n) = 2T(n/2) + O(1) => O(n^(log_2 2)) => O(n) (By The Master's Theorem)
"""

def conquer(array, left_index, right_index):
    """
    Recursively searches for single elements in the array
    :param array: array to recursively search
    :param left_index: index of the left side of the array
    :param right_index: index of the right side of the array
    :return: number of single elements in the array
    """

    #base case
    if left_index < 0 or right_index < 0:
        return 0

    #elements are different --> single value found
    if array[left_index] != array[right_index]:
        singles = 1

    #elements are the same --> no single value found
    else:
        singles = 0

    return singles + conquer(array, left_index - 1, right_index - 1)


def numSingles(array, n):
    """
    Handles process of base cases, calling divide and conquer and returning final result
    :param array: input array to search
    :param n: size of array
    :return: number of single elements in array
    """
    #Base Case
    if n == 2:
        if array[0] == array[1]:
            return 0
        if array[0] != array[1]:
            return 2

    #Split into left and right sub-arrays
    mid = n//2
    print(mid)
    Left = array[0:mid]
    Right = array[mid:n]

    l = conquer(Left,mid - 2, mid - 1)
    r = conquer(Right, mid - 2, mid - 1)

    if array[mid - 1] == array[mid]:
        return (l + r) - 2
    else:
        return l + r

if __name__ == "__main__":

    #Testing
    A1 = [1,2]
    A2 = [0,0]
    A3 = [0,1,1,2,3,4,4,5]
    A4 = [0,1,1,2,2,3,4,4]

    result1 = numSingles(A1, 2)
    assert result1 == 2

    result2 = numSingles(A2, 2)
    assert result2 == 0

    result3 = numSingles(A3, 8)
    assert result3 == 4

    result4 = numSingles(A4, 8)
    assert result4 == 2

