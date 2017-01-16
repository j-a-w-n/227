# sum_values.py

from sys import argv

programmer = """
Programmed by Kyle Connolly
"""
total = sum(int(i) for i in argv[1:])

print()
print(programmer)
print("The sum is {} .".format(total))
input("Press Enter to continue ... ")
