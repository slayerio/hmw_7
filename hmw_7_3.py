# 1
def print_stars():
    """prints 6 stars"""
    print('******')


# b
# in another file (main.py)
from hmw_7_3 import print_stars
print_stars()
# other options:
# import hmw_7_3 ---> hmw_7_3.print_stars
# import hmw_7_3 as a ---> a.print_stars

# c
print(999 * 10)
if __name__ == "__main__":
    print(999 * 10)
# d
help(print_stars())