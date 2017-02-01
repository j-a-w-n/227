# unique_names_in_order.py

from sys import argv

programmer = """
Programmed by Kyle Connolly\
"""
print(programmer)
names_in = []

for name in argv[1:len(argv)]:
    names_in.append(name)
    names_in.sort()

unique_order = set(names_in)
for name in unique_order:
    print(name, end="\n")
