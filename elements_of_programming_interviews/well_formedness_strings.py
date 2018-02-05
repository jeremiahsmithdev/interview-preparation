matches = {'{' : '}', '(' : ')', '[' : ']'}

def is_well_formed(str):
    stack = []

    for ch in a:
        if ch in ['{', '(', '[']:
            stack.append(ch)
        else:
            if not len(stack) or matches[stack.pop()] != ch:
                return False

    return True

a = "{}()[]}"

print(is_well_formed(a))

