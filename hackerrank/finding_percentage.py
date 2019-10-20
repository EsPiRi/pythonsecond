N=int(input())
students={}
for i in range(N):
    students_list=input().split()
    marks=list(map(float,students_list[1:]))
    students[students_list[0]]=sum(marks)/float(len(marks))

print("%.2f" % students[input()])