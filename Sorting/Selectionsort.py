# Selectionsort Algorithm
# Time Complexity
# Best:     n**2
# Average:  n**2
# Worst:    n**2
# Space Complexity
# Worst:    1

import random as rn

ylst = []
for i in range(0,30):
    x = rn.randint(1,100)
    ylst += [x]

# print(ylst)

def selectionSort(xlst):
    # sortedList = []
    for i in range(len(xlst)):
        smallest = i
        for j in range(i+1,len(xlst)):
            if xlst[smallest] > xlst[j]:
                smallest = j
        xlst[smallest],xlst[i] = xlst[i],xlst[smallest]
        print(xlst)
                
    return xlst

print(selectionSort(ylst))