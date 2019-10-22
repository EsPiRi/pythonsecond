string=input()
alnum=False
alpha=False
digit=False
lowercase=False
uppercase=False
for s in string:
    if(s.isalnum()):
        alnum=True
    if(s.isalpha()):
        alpha=True
    if(s.isdigit()):
        digit=True
    if(s.islower()):
        lowercase=True
    if(s.isupper()):
        uppercase=True

print(alnum)
print(alpha)
print(digit)
print(lowercase)
print(uppercase)