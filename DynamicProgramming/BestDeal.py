"""
Problem Statement: You are shopping and the store has a special sale, if you pay full
    price for an item, you will get the previous item for free. Your goal is to get
    all n items for the smallest amount of money possible.

Givens:
    - items 1, ... , n with corresponding prices p_i

Sub Problems: for a value i, where 0 <= i <= n, what is the smallest amount of money
    you can pay?

                    L(i) = min(L[i - 2] + p_i, L[i - 1] + p_i)

Correctness: The core decision within this problem is deciding whether for each item i, if
    you should pay full price for it (better deal for the previous item) or not (would
    result in needing to pay in full for the following item). The core recursion of this
    algorithm weights the best option for item i - 1 and preserves the minimum cost in the
    array.

Running Time: O(n) -- this algorithm solves n sub problems, each taking O(1) time to solve.
"""
def best_deal(costs, num_items):
    L = [0] * (num_items + 1)
    L[1] = costs[0]
    L[2] = costs[1]

    for i in range(3, num_items + 1):
        L[i] = min(L[i - 2] + costs[i - 1], L[i - 1] + costs[i - 1])

    return L[num_items]

if __name__ == "__main__":
    #Initializing Test Values
    prices = [1,5,2,1]
    n = 4

    result = best_deal(prices, n)
    print(f"Best Deal: ${result}")

