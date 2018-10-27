n = int(input())

a = [0] * n

for i in range(n):
    a[i] = int(input())

a.sort()

r =[ 0] * len(a)

r[0] = a[(  n-1) // 2]

pr = 1
pi=0
pj=len(a)-1



while pr <len(a):
    r[pr] = a[pj]
    pr += 1
    pj -= 1
    if pr >=len(a):
        break
    r[pr] = a[pi]
    pr += 1
    pi += 1

result1 = 0
for i in range(n-1):
    result1 += abs(r[i+1] - r[i])

pr = 1
pi=0
pj=len(a)-1

while pr <len(a):
    r[pr] = a[pi]
    pr += 1
    pi += 1

    if pr >=len(a):
        break
    r[pr] = a[pj]
    pr += 1
    pj -= 1

result2 = 0
for i in range(n-1):
    result2 += abs(r[i+1] - r[i])

result = result1 if result1 > result2 else result2

print(result)
