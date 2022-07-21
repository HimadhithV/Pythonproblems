#Palindrome

s = input("Enter the string:")
ans=0
if s==s[::-1]:
    ans=1

if ans:
    print("\nIt is a palindrome")
else:
    print("\nNot a palindrome")