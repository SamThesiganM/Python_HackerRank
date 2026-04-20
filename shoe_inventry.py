from collections import Counter

num_shoes = int(input())
inventory = Counter(map(int, input().split()))
num_customers = int(input())
total_earned = 0
for i in range(num_customers):
    size, price = map(int, input().split())
    if inventory[size] > 0:
        total_earned += price
        inventory[size] -= 1

print(total_earned)

