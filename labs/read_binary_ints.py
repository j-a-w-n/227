# read_binary_ints.py

import pickle


print('Programmed by Kyle Connolly')

with open('integers.dat', 'r') as bin:
    eof = False
    num_list = []
    while not eof:
        try:
            num_list.append(i=pickle.load(bin))
        except eof:
            eof = True

print(num_list, end=' ')
print('The maximum value is {} and the minimum value is {}.').format(
        max(num_list),
        min(num_list)
        )
