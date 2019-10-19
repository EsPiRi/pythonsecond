lenA = int(input())
A = set(map(int, input().split()))
N = int(input())
for i in range(0, N):
    command = input().split()
    if (command[0] == "update"):
        A.update(set(map(int, input().split())))
    elif(command[0]=="symmetric_difference_update"):
        A.symmetric_difference_update(set(map(int,input().split())))
    elif(command[0]=="difference_update"):
        A.difference_update(set(map(int,input().split())))
    else:
        A.intersection_update(set(map(int,input().split())))

print(sum(A))