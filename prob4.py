#Max and min element in an array

n=int(input("Enter the no of elements in the string:"))
arr=[]
max=0
min=99999
for i in range(n):
    j=int(input("Enter the number:"))
    arr.append(j)
k=0
while k<n:
    if arr[k]<min:
        min=arr[k]
    elif arr[k]>max:
        max=arr[k]
    k+=1

print("The max element is",max)
print("The min element is",min)
