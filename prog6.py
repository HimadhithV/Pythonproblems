# Duplicates in an array 

arr =[8,9,6,8,5,1,8,5,1]
n=len(arr)

visited=[]
for i in range(n):
    count=0
    pos=[]
    j=0
    if arr[i] not in visited:
        while j<n:
            if  arr[i]==arr[j]:
                count+=1
                pos.append(j)
            
            else: pass
            j+=1
    
        visited.append(arr[i])  
    
    if count>0:
        print("The element",arr[i],"is a duplicate")
    else:
        continue
        