count1 = int(input())
news1 = set(map(int, input().split()))
count2 = int(input())
news2 = set(map(int, input().split()))

print(len(news1.difference(news2))+len(news2.difference(news1)))