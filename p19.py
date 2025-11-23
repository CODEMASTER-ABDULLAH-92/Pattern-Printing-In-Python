# 4 4 4 4 4 4 4 
# 4 3 3 3 3 3 4 
# 4 3 2 2 2 3 4 
# 4 3 2 1 2 3 4 
# 4 3 2 2 2 3 4 
# 4 3 3 3 3 3 4 
# 4 4 4 4 4 4 4 

for i in range(1,8):
    for j in range(1,8):
        if (i==2 and 2<=j<=6) or (i==6 and 2<=j<=6) or (3<=i<=5 and j == 2) or (3<=i<=5 and j == 6):
            print("3 ", end="")
        elif (j == 3 and 3<=i<=5) or (j == 5 and 3<=i<=5) or(i ==3 and 3<=j<=5) or (i == 5 and 3 <=j<=5):
            print("2 ", end="")
        elif i == 4 and j== 4:
            print("1 ", end="")
        else:
            print("4 ",end="")
    print()