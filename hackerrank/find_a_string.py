string = input()
substring = input()
count = 0
for i in range(len(string)):
    if i + len(substring) <= len(string):
        subs = string[i:i + len(substring)]
        if subs == substring:
            count += 1

print(count)
