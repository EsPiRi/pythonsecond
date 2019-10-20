n = int(input())
A = list(map(int, input().split()))


A.sort()
index=A.index(max(A))
print(A[index-1])