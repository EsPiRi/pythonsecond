A = set(map(int, input().split()))
N = int(input())
result = True
for i in range(0, N):
    B = set(map(int, input().split()))
    if not B.issubset(A):
        result=False
    if len(B)>len(A):
        result=False

print(result)
