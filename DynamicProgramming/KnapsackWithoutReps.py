"""
Problem Statement: Given a set of items where each contains a weight and a value and a
    knapsack with a maximum weight capacity, devise an algorithm to find the MAXIMUM
    VALUE you can pack while staying within the constraints. Note tha you are given
    only 1 of each item.

    Let the number of items be referred to as 'n' and the max weight be W.

Sub problem: for some i, where 0 <= i <= W, what is the maximum value that can be packed?
                   i = capacity    j = item index   v = value

                L(i,j) = max{L(i - i_j, j - 1) + v_j, L(i, j - 1)}

Correctness: For each item we will consider whether we should pack it. At every decision
    point we will look for the option that will optimize (greatest value for minimal
    weight) the packing of the bag. We look at our previous best for the bag packed
    at the SAME weight and also the previous best of the bag if it did not contain
    the added weight of this item. In doing so we are ensuring that each decision is
    maximizing the state and in doing so allowing the algorithm to be 'built up' correctly
    to allow us to find our ultimate answer.

Running Time: O(n*W); This algorithm contains n sub problems each taking O(W) time to
    solve.
"""
#Class to represent the items
class Item:
    def __init__(self, value, weight):
        self.value = value
        self.weight = weight

    def get_weight(self):
        return self.weight

    def get_value(self):
        return self.value

#Implementation of the algorithm
def knapsack_without_reps(capacity, items, n):
    grid = [[0]*(capacity + 1) for _ in range(n + 1)]
    for j in range(1,n + 1):
        for i in range(1,capacity + 1):
            if items[j - 1].get_weight() <= i:
                grid[j][i] = max( grid[j - 1][i], grid[j - 1][i - items[j - 1].get_weight()] + items[j - 1].get_value())
            else:
                grid[j][i] = grid[j-1][i]

    return grid[n][capacity]


#Initializing the items
if __name__ == "__main__":

    #Setting up the knapsack
    item_1 = Item(2,3)
    item_2 = Item(2,1)
    item_3 = Item(4,3)
    item_4 = Item(5,4)
    item_5 = Item(3,2)

    knapsack = [item_1, item_2, item_3, item_4, item_5]
    result = knapsack_without_reps(7, knapsack, 5)
    print(f"Maximum Value = {result}")
