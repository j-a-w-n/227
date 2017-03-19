# read_binary_ints.py

import pickle


eof = False
num_list = []

with open('integers.dat', 'rb') as bin:
    while not eof:
        try:
            i = pickle.load(bin)
            num_list.append(i)
        except:
            eof = True


print('Programmed by Kyle Connolly')
print(num_list)
print('The maximum value is {} and the minimum value is {}.'.format(
        max(num_list),
        min(num_list)))
