from math import inf
def cut(n, prices, curr_cost, sol, temp_sol):
    if n == 0:
        sol.append((temp_sol.copy(),curr_cost))
        return curr_cost #valid solution
    if n < 0:
        return float(-inf) #not valid solution
    best_sol = float(-inf)
    #max problem
    for i in range(len(prices)):#cutting options
        this_cut = i + 1
        remaining = n - this_cut
        temp_sol.append(this_cut)
        result = cut(remaining, prices, curr_cost + prices[i], sol, temp_sol)
        temp_sol.pop()
        if result > best_sol:
            best_sol = result
    return best_sol

n = 4
prices = [1,5,8,9]
sols = []
print(cut(n,prices, 0, sols, []))
print(sols)