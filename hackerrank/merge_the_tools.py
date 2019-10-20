t = ""
s = input()
n = len(s)
k = int(input())
for i in range(0, n):
    if not s[i] in t:
        t=t+s[i]
    if (i+1) % (k) == 0:
        print(t)
        t = ""


