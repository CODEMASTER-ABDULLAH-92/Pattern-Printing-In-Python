# 12345
# 1234
# 123
# 12
# 1

# Outer loop for the Rows
for i in range(5):
    # Inner Loop for the column
    for j in range(1,6 - i):
        print(j,end="")
    print()