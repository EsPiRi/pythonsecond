K = int(input())
room_numbers = list(map(int, input().split()))
rooms = set(room_numbers)

print(int((sum(rooms) * K - sum(room_numbers)) / (K - 1)))
