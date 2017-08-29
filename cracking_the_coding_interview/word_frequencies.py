#ccti 16.2

def count_frequencies(a, book):
    frequencies = 0
    for word in book:
        if word.lower() == a.lower(): #assumed no whitespace etc
            frequencies += 1
    return frequencies

def count_frequencies_dict(a, book, dict):
    if a in dict:
        print("found")
        return dict[a], dict
    for word in book:
        word = word.lower()
        if word in dict:
            dict[word] = dict[word] + 1
        else:
            dict[word] = 1
    return dict[a], dict


book = "The cat sat on the mat"
book = book.split(" ")
word = "the"

print(count_frequencies(word, book))

freq, dict = count_frequencies_dict(word, book, {})

print(freq)

word = "cat"

freq, dict = count_frequencies_dict(word, book, dict)

print(freq)