price = int(input())
next = 1000 - price

coin=[500,100,50,10,5,1]
total = 0

for i in coin:
    count = next // i
    total += count
    next %= i
    
print(total)