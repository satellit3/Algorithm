#until it becomes 1
#1.N-1 2.N/k
#N<=K
#N(2<= N <= 100,000) K(2<= N <= 100,000)
#Prints the minimum number of times that performed until N becomes 1.

n, k = map(int, input().split())
result = 0

while n >= k:
    #if n is not split apart, do -1
    while n % k != 0:
        n -= 1
        result += 1
    n //= k
    result += 1

#last left num -1

while n > 1:
    n -= 1
    result += 1

print(result)
