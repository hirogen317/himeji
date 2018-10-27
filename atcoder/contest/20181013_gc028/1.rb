
n, m = gets.chomp.split(" ").map(&:to_i);

s = gets.strip()
t = gets.strip()

l = n * m /  m.gcd(n)



result = true

for i in 0...n do
    if i * m % n == 0
        k = i * m / n
        if k < t.size() and t[k] != s[i]
            result = false
        end
    end
end

if result
    print(l)
else
    print(-1)
end
