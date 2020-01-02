# Insertionsort Algorithm
# Time Complexity
# Best:     n
# Average:  n**2
# Worst:    n**2
# Space Complexity
# Worst:    1

import random as rn

ylst = [5,7,1,3,2]
# for i in range(0,30):
#     x = rn.randint(1,100)
#     ylst += [x]

def insertionSort(a):
    i = 1
    while i < len(a):
        j = i
        while j > 0:
            if a[j] < a[j-1]:
                a[j],a[j-1] = a[j-1],a[j]
            j -= 1
        i += 1
        print(a)
    return a

print(ylst)
print("="*20)
print(insertionSort(ylst))

             