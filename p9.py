# n = 5  # height of upper half

# # Upper part
# for i in range(n):
#     print(" " * (n - i - 1) + "*" * (2*i + 1))

# # Lower part
# for i in range(n - 2, -1, -1):
#     print(" " * (n - i - 1) + "*" * (2*i + 1))


# Upper part
for i in range(5):
    for j in range(5 - i):
        print(" ", end="")
    for k in range(i + 1):
        print("*", end="")
    for m in range(i):
        print("*", end="")
    print()

# Lower part
for i in range(4):
    for j in range(i + 2):
        print(" ", end="")
    for k in range(4 - i):
        print("*", end="")
    for m in range(3 - i):
        print("*", end="")
    print()
