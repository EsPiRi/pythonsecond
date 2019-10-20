word1 = input()
n = len(word1)

stuart = 0
kevin = 0
for i in range(n):
    if (word1[i] in ('A', 'E', 'I', 'O', 'U')):
        kevin += n - i
    else:
        stuart += n - i

if kevin > stuart:
    print("Kevin", kevin)
elif stuart > kevin:
    print("Stuart", stuart)
else:
    print("Draw")
