# ----1
# ---21
# --321
# -4321
# 54321
for k in range(1, 6):

    # Print dashes
    for m in range(5 - k):
        print("-", end="")

    # Print numbers
    for n in range(k,0,-1):
        print(n, end="")

    print()
