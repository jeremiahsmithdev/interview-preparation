#ccti 1.5

def one_away(string, target_string):
    if string == target_string: #handles zero edits
        return True
    diff = abs(len(string) - len(target_string))
    if diff > 1:
        return False
    no_differences = 0
    #this is wrong...
    for i in range(min(len(string), len(target_string))):
        if string[i] != target_string[i]:
            #print(i)
            if len(string) > len(target_string):
                target_string = target_string[:i] + string[i] + target_string[i:]
                #print(target_string)
            else:
                string = string[:i] + target_string[i] + string[i:]
            break

    return True if string == target_string else False

print(one_away("plee", "ple"))