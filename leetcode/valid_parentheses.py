a = ["()", "()[]{}", "(]", "([)]"]

d = {"[": "]", "(": ")", "{": "}"}

def match(a, b):
    return True if d[a] == b else False

def check_string(string):
    stack = []
    for char in example:
        if char in d:
            stack.insert(0, char)
        else:  # find matching opening bracket
            potential_opening = stack.pop(0)
            if not match(potential_opening, char):
                return False
    return True

for example in a:
    print(check_string(example))

