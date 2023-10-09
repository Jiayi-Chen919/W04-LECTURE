def first_fit(items, bin_capacity):
    '''
    First-fit heuristic for the bin packing problem.
    Takes in a list of items of different sizes, and a bin capacity.
    Returns a list of bins and how much they each contain.
    '''
    pass



# Testing our function
items = [2, 1, 3, 2, 1, 2, 3, 1]
bin_capacity = 4
bins = first_fit(items, bin_capacity)
print(bins)  # expected: [4, 4, 4, 3]
