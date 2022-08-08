#Hash function to find minimum no of operations to make elements equal

from collections import defaultdict
 
def minOperation(arr, n):
 
    Hashtable = defaultdict(lambda:0)
    for i in range(0, n):
        Hashtable[arr[i]] += 1

    count = 0
    for i in Hashtable:
        if count < Hashtable[i]:
            count = Hashtable[i]
 

    return n - count
 
arr = [1, 5, 2, 1, 3, 2, 1]
n = len(arr)
print(minOperation(arr, n))


