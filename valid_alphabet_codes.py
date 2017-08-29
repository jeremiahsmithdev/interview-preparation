c = 0

def permutations(a, options, temp_sol, sols):
    print("hi")
    if len(a) == 0:
        sols.append(temp_sol.copy())
        return

    for option in options:
        curr = a[:option]
        temp_sol.append(curr)
        print(curr)
        remainder = a[option:]
        print(remainder)
        if int(curr) <= 26:
            permutations(remainder, options, temp_sol, sols)
        temp_sol.pop()

    return sols

a = "1126" #get all permutations that are <= 26?...wait...substrings

options = {1, 2}

sols = []

print(permutations(a, options, [], sols))
