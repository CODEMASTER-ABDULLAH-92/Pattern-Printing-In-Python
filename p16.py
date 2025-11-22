# **********
# ****  ****
# ***    ***
# **      **
# *        *
# Upper Part
for i in range(5):
    for j in range(5 - i):
        print("*", end="")
    for k in range(i):
        print(" ", end="")
    for m in range(i):
        print(" ", end="")
    for n in range(5 - i):
        print("*", end="")
    print("-")

# Lower Part
for i in range(1,6):
    for j in range(i):
        print("*", end="")
    for k in range(5 - i):
        print(" ", end="")
    for m in range(5 - i):
        print(" ", end="")
    for n in range(i):
        print("*", end="")
    print("-")
