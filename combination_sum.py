
import sys
sys.setrecursionlimit(50000)

def _combination_sum(a,tar,curr,sols,temp_sol,start):

    if curr == tar:
        sols.append(temp_sol.copy())
        return

    if curr > tar:
        return

    for i in range(start,len(a)): #n times
        temp_sol.append(a[i])
        _combination_sum(a,tar,curr + a[i],sols,temp_sol,i)
        temp_sol.pop()

    return


def combination_sum(a,tar):
    sols = []
    _combination_sum(a, tar, 0, sols, [], 0)
    return sols

a = [2,3,6,7]
tar = 7
print(combination_sum(a,tar))