from itertools import permutations

S=input().split()

for i in permutations(sorted(S[0]),int(S[1])):
    print("".join(i))