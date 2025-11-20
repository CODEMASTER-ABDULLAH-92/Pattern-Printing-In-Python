#  *********
#   *******
#    *****
#     ***
#      *

for i in range(5):
    for j in range(i + 1):
        print(" ",end="")
    for k in range(5 - i):
        print("*",end="")
    for m in range(4 - i):
        print("*",end="")
    print()
