n = int(input())
first = n
count =0
    
while True:
    count += 1
    ten = n//10
    one = n%10
    
    ab = ten+one
    
    abone = ab%10
    new = one*10 + abone
    
    n = new
    
    if n == first:
        break
print(count)
    
        
     