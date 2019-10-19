T = int(input())
for i in range(0, T):
    lenA = int(input())
    A = set(map(int, input().split()))
    lenB = int(input())
    B = set(map(int, input().split()))
    if len(A.difference(B)) == 0:
        print("True")
    else:
        print("False")
