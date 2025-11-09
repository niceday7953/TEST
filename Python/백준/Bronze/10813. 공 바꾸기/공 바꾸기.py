n,m = map(int,input().split())

basket = [i for i in range(n+1)]

for k in range(m):
    i,j = map(int,input().split())
    basket[i],basket[j] = basket[j],basket[i]
print(*basket[1:])