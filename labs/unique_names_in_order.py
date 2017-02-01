# unique_names_in_order.py
from sys import argv

programmer = """
Programmed by Kyle Connolly\
"""
print(programmer)
names_in = []

for name in argv[1:len(argv)]:
    names_in.append(name)

unique = set(names_in)
order = list(unique)
order.sort()
for name in order:
    print(name, end="\n")
