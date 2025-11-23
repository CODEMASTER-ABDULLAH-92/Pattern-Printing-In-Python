# ****
# *  *
# *  *
# ****

# for i in range(1,5):
#     for j in range(1,5):
#         if (i == 2 and j == 2) or (i == 2 and j == 3) or (i == 3 and j == 2 ) or (i == 3 and j == 3):
#             print(" ",end="")
#         else:
#             print("*",end="") 
#     print()


# Optimal solution 

for i in range(1,5):
    for j in range(1,5):
        if 2<=i <=3 and 2<=j<=3:
            print(" ",end="")
        else:
            print("*",end="") 
    print()