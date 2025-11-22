# ----1
# ---12
# --123
# -1234
# 12345

for k in range(1,6):
    for m in range( 5 - k):
        print("-",end="")
    for n in range(1,k + 1):
        print(n,end="")
    print()
