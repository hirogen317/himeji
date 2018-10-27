import math

n, m = map(int, input().split())
s = input().strip()
t = input().strip()

l = n * m //  math.gcd(m, n)

result = True

for i in range(0, n-1):
    if i * m % n == 0:
        k = i * m // n
        if k < len(t) and t[k] != s[i]:
            result = False

if result:
    print(l)
else:
    print(-1)
