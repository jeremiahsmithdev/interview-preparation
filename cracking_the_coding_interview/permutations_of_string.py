#ccti 8.7

def get_permutations(a):

    if len(a) == 0:
        return [" "]

    permutations = []
    #take first letter
    letter = a[0]
    remainder = a[1:]
    #generate all possible sub-words
    words = get_permutations(remainder)
    #insert letter into all possible positions
    for word in words:
        for i in range(len(word)):
            new_word = word[:i] + letter + word[i:] #trick here is to insert letter at each point of word
            permutations.append(new_word)
    return permutations

a = "abcd"
print('\n'.join(get_permutations(list(a))))