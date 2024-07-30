fun: str = " fun-day "
# a
print(fun)
print(fun.replace(" ", ""))
# b
print("Hello".isalpha())
# c
print("777".isdigit())
# d
print("  ".isspace())
# e
print("".join(["N", "I", "N", "J", "A"]))
# f
print('*'.join(["N", "I", "N", "J", "A"]))
# g
print("e" in "hELLo")
# h
word = input("Give me a word")
lst: list[str] = [c.capitalize() for c in word if c.isalpha()]
print(lst)

