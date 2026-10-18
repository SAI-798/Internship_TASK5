
# Problem: Finding the Percentage
# https://www.hackerrank.com/challenges/finding-the-percentage/problem

n = int(input())
students = {}

for i in range(n):
    data = input().split()
    name = data[0]
    marks = list(map(float, data[1:]))
    students[name] = marks

name = input()
average = sum(students[name]) / len(students[name])

print(f"{average:.2f}")
