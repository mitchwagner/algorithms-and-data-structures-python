'''
Given two lists on which we can perform insert, delete, and replace
operations, determine the number of operations it would take to
transform one list into the other. 
'''

    
def edit_distance(xs, ys):
    table = init_table(len(xs), len(ys))
    return edit_distance_help(xs, ys, table)


def init_table(x, y):
    '''
    Create a table (x rows by y columns)
    '''
    return [[-1 for j in range(y + 1)] for i in range(x + 1)]


def edit_distance_help(xs, ys, table):
    x = len(xs)
    y = len(ys)

    prev = check_table(x, y, table)

    # Previously computed?
    if prev != -1:
        return prev

    # Trivial transformation?
    if x == 0: table[x][y] = y; return y
    if y == 0: table[x][y] = x; return x

    # If the last elements are the same, compute on sublists 
    if xs[-1] == ys[-1]:
        table[x][y] = edit_distance_help(xs[:-1], ys[:-1], table)
        return table[x][y]

    # Non-trivial recurrence (insert, delete, or replace)

    # Append to xs to match last element 
    # (symmetrically, delete from ys)
    insert_cost = edit_distance_help(xs, ys[:-1], table)

    # Delete last element from xs
    # (symmetrically, append to ys) 
    delete_cost = edit_distance_help(xs[:-1], ys, table)

    # replace last element of one to match the other
    replace_cost = edit_distance_help(xs[:-1], ys[:-1], table)

    cost = 1 + min(insert_cost, delete_cost, replace_cost)

    table[x][y] = cost

    return cost 


def check_table(x, y, table):
    return table[x][y]
