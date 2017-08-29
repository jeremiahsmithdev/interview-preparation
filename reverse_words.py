#https://www.careercup.com/question?id=5106757177180160
#given to me in previous interview

#this method will not work: strings are immutable in python
#this method is just to demonstrate how in-place reverse would work in another language
def reverse_inplace(string):
    start = 0
    end = len(string) - 1
    while start < end:
        temp = string[start]
        string[start] = string[end]
        string[end] = temp
        start += 1
        end -= 1
    return string

def reverse_inplace_xor(string):
    start = 0
    end = len(string) - 1
    while start < end:
        string[start] ^= string[end]
        string[end] ^= string[start]
        string[start] ^= string[end]
        start += 1
        end -= 1
    return string

def reverse(string):
    new_string = ""
    for i in reversed(range(len(string))):
        new_string += string[i]
    return new_string

def reverse_words(string):
    string += " "
    start = 0
    end = 0
    while end < len(string):
        if string[end] == ' ':
            string = string[:start] + reverse(string[start:end]) + string[end:] #this would be so much nicer with pointers...
            print(string)
            start = end + 1
        end += 1
    return string

a = "the boy ran"
print(reverse_words(a))