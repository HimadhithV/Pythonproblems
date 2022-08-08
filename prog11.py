#Difference between an element and the largest 
import math as m
def maxnum(arr):
    max=0
    for i in range(len(arr)):
        if max<arr[i]:
            max=arr[i]
    return max



arr=[2, 3, 10, 6, 4, 8, 1]
print("The difference is ",maxnum(arr)-arr[0])