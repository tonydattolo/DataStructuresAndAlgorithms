# Bubblesort Algorithm
# Time Complexity
# Best:     n
# Average:  n**2
# Worst:    n**2
# Space Complexity
# Worst:    1

import random as rn

def bubbleSort(a):
    
    for i in range(len(a)):
        for j in range(len(a)-1-i): #you subtract 1 because you cant swap past the end of the len(list)
            if a[j] > a[j+1]:
                a[j],a[j+1] = a[j+1],a[j] #you have to assign concurrently to swap
                print(a)


    return a

xlst = []
for i in range(0,30):
    x = rn.randint(1,100)
    xlst += [x]

print(xlst)
bubbleSort(xlst)
print(bubbleSort(xlst))

if sorted(xlst) == bubbleSort(xlst):
    print("SUCCESS")