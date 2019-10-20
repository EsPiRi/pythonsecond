string=input()
command=input().split()

string = string[:int(command[0])] + command[1] + string[int(command[0])+1:]
print(string)