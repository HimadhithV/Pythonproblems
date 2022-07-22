# Anagrams

words = {"act", "god", "cat", "dog", "tac"}
n=len(words)

for i in words:
    for j in words:
        if sorted(i)==sorted(j):
            print(j)


