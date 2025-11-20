#      *
#     ***
#    *****
#   *******
#  *********

for i in range(5):
    for j in range(5 - i):
        # print("-",end="")
        print(" ",end="")
    for k in range(i + 1):
        print("*", end="")
    for m in range(i):
        print("*",end="")
    print()  
