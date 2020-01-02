# Radixsort
# Time Complexity
#   Best:     nk
#   Average:  nk
#   Worst:    nk
# Space Complexity
#   Worst:    n+k

import random as rn

ylst = []
for i in range(0,10):
    x = rn.randint(1,10000)
    ylst += [x]

def radixSort(a):
    maxNum = max(a)
    for i in range(len(a)):
        print(f"i: {i}")
        print(f"a[i]: {a[i]}")
        for j in range(len(str(maxNum))):
            print({f"a[i][j]: {a[i][j]}"})
            # if a[i][len(a[i])-1] < a[i+1][len(a[i])-1]:
                # a[i],a[i+1] = a[i+1],a[i]
    return a

print(f"ylst to sort: {ylst}")
print("="*30)
print(radixSort(ylst))
