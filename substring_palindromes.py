#https://www.careercup.com/question?id=5177378863054848

#challenging problem. can leverage another algorithm to solve faster?

def is_palindrome(string):
    start = 0
    end = len(string) - 1
    while start < end:
        #print(start, end)
        if string[start] != string[end]:
            return False
        start += 1
        end -= 1
    return True

def substring_palindromes(string):
    no_palindromes = 0
    for i in range(len(string)): #this is poor
        for j in range(i + 1, len(string) + 1):
                substring = string[i:j]
                print(substring)
                if is_palindrome(substring):
                    #print(substring)
                    no_palindromes += 1
        #print()
    return no_palindromes

string = "abba"
print(substring_palindromes(string))