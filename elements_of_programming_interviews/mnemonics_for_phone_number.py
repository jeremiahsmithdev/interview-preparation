mappings = ["0", "1", "ABC", "DEF", "GHI", "JKL", "MNO", "PQRS", "TUV", "WXYZ"]

number = str(7987456)

def generate_mnemonics(n, partials):
    if n == len(number):
        print(partials)
        return

    # ie for P, Q, R, S
    for option in mappings[int(number[n])]:
        partials.append(option)
        generate_mnemonics(n + 1, partials)
        partials.pop()

generate_mnemonics(0, [])