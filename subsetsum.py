# https://en.wikipedia.org/wiki/Subset_sum_problem
# given a set of integers, is there a non-empty subset whose sum is zero?
from sys import argv


def combinations(test_set):
    """Generator to return every possible combination of the input set
    """
    set_length = len(test_set)
    # for each possible combination
    for i in range(2 ** set_length):
        combo = []
        for b in range(set_length):
            # shift bits in 'i' right by 'b' spaces
            # the same as //'ing i by 2**b
            # if odd, the 'b'th item in the set is part of this combo
            if (i >> b) % 2 == 1:
                combo.append(test_set[b])
        yield combo


def subset_sum(test_set):
    """Returns a tuple of True and the solution subset if a subset is found
    else returns False with an empty list"""
    # simple cases
    # 0 in the set can be returned by itself
    if 0 in test_set:
        return True, [0]
    for combo in combinations(test_set):
        if combo and sum(combo) == 0:
            return True, combo
    return False, []


def is_number(n):
    try:
        return int(n)
    except:
        return False


if len(argv) < 2:
    print('Require a set of integers as arguments!')
    exit(1)
input_set = argv[1:]
input_set_n = []
for arg in input_set:
    if not is_number(arg):
        print("Error! '%s' is not an integer." % arg)
        exit(1)
    input_set_n.append(int(arg))

print('In set', input_set_n, '\n', subset_sum(input_set_n))
