import sys
sys.setrecursionlimit(50000)

def insert(string, index):
    return string[:index] + "()" + string[index:]

def generate(n, current_pairs, index, string, memo):
    if n == current_pairs:
        return string
    key = string + "-" + str(index)
    if key in memo:
        print("used")
        return memo[key]
    sols = []
    while index <= len(string):
        temp_string = insert(string, index)
        memo[key] = temp_string
        #exit()
        sols.append(generate(n, current_pairs + 1, index, temp_string, memo))
        index += 1
    return sols

def generate_parentheses(n):
    return generate(n, 1, 0, "()", {})

print(generate_parentheses(4))