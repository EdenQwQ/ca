from random import randint

def next(prev_cell, neighbor, rule):
    next_cell = ""
    for n in range(len(prev_cell)):
        status = prev_cell[n]
        for i in range(1,neighbor+1):
            status = prev_cell[(n-i)%len(prev_cell)] + status + prev_cell[(n+i)%len(prev_cell)]
        next_cell += rule[int(status, 2)]
    return next_cell

def random_cell(length):
    cell = ""
    for _ in range(length):
        cell += str(randint(0,1))
    return cell

def evolve(init_cell, neighbor, rule, times):
    cells = [init_cell]
    for _ in range(times):
        next(cells[-1], neighbor, rule)
    return cells
