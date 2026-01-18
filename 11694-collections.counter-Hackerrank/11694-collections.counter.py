# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter

n = int(input())

shoe_size = list(map(int,input().split()))

inventory = Counter(shoe_size)

m = int(input())

total_earnings = 0

for _ in range(m):
    size, price = map(int, input().split())
    
    if inventory[size]> 0 :
        total_earnings += price
        inventory[size] -= 1
        
print(total_earnings)
