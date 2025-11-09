maxval = 0
maxr,maxc = 0,0

for r in range(9):
    row = list(map(int,input().split()))
    
    for c in range(9):
        if row[c] > maxval:
            maxval = row[c]
            maxc =c
            maxr =r
print(maxval)
print("{} {}".format(maxr+1, maxc+1))