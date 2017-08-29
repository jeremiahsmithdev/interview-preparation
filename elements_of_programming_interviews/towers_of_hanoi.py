#eopi 16.1

NO_PEGS = 3
NO_RINGS = 6

def compute_steps(rings_to_move, pegs, from_peg, to_peg, use_peg):
    if rings_to_move == 0:
        return
    compute_steps(rings_to_move - 1, pegs, from_peg, use_peg, to_peg)
    pegs[to_peg].append(pegs[from_peg].pop())
    print("moved",from_peg,"to",to_peg)
    compute_steps(rings_to_move - 1, pegs, use_peg, to_peg, from_peg)

pegs = [[] for i in range(NO_PEGS)]

for i in range(NO_RINGS):
    pegs[0].append(i)

print(pegs)

compute_steps(NO_RINGS, pegs, 0, 1, 2)

print(pegs)