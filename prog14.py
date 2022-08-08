# Check disjoint or not
s1 = {12, 34, 11, 9, 3}
s2 = {2, 1, 3, 5}
m = s1.intersection(s2)
if(m):
    (element,) = m
    print("Not disjoint", element)
else:
    print("Disjoint")
