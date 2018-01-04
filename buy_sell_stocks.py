def brute_force(prices):
    max_profit = 0;
    for i in range(0, len(prices)):
        for j in range(i + 1, len(prices)):
            temp_profit = prices[j] - prices[i]
            max_profit = max(max_profit, temp_profit)

    return max_profit

