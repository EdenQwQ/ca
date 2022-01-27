from random import randint

def next(prev_cell, neighbor, rule):
    next_cell = ""
    for n in range(len(prev_cell)):
        status = prev_cell[n]
        for i in range(1,neighbor+1):
            status = prev_cell[(n-i)%len(prev_cell)] + status + prev_cell[(n+i)%len(prev_cell)]
        next_cell += rule[int(status, 2)]
    return next_cell

def random_bin(length):
    rbin = ""
    for _ in range(length):
        rbin += str(randint(0,1))
    return rbin

def evolve(init_cell, neighbor, rule, times):
    cells = [init_cell]
    for _ in range(times):
        cells.append(next(cells[-1], neighbor, rule))
    return cells

def dTb(d, length):
    b = ""
    for _ in range(length):
        b += str(d%2)
        d //= 2
    return b


neighbor = 3
length = 100
times = 100
# rule = dTb(30, 2**(neighbor*2+1))
rule = "00000101000000000101010100000101000001010000000001010101000001010101010111111111010101011111111101010101111111110101010111111111"
print(rule)
test = evolve(random_bin(length), neighbor, rule, times)
for i in test:
    line = ""
    for n in i:
        line += "█" if n == "1" else " "
    print(line)
