# sum_values.py

from sys import argv

programmer = """
Programmed by Kyle Connolly
"""

print()
print(programmer)
for item in argv[1:]:
    total = sum(int(item) for i in argv[1:])
print("The sum is {}.".format(total))
input("Press Enter to continue ... ")
