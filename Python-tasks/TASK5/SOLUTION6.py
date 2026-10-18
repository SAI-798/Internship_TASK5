
# Problem: Introduction to Sets
# https://www.hackerrank.com/challenges/py-introduction-to-sets/problem

def average(arr):
    arr = set(arr)
    return round(sum(arr) / len(arr), 3)

n = int(input())
arr = list(map(int, input().split()))

print(average(arr))
