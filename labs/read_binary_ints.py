# read_binary_ints.py

import pickle
from sys import argv


print('Programmed by Kyle Connolly')

with open(argv[1], 'r') as bin:
    while pickle.load(bin):
        num_list = [].append(i=pickle.load(bin))
    print(bin, end=' ')
    print('The maximum value is {} and the minimum value is {}.').format(
            max(num_list),
            min(num_list)
            )
