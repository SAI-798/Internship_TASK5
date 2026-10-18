
# Problem: Symmetric Difference
# https://www.hackerrank.com/challenges/symmetric-difference/problem

n = int(input())
a = set(map(int, input().split()))

m = int(input())
b = set(map(int, input().split()))

result = sorted(a ^ b)

for num in result:
    print(num)
