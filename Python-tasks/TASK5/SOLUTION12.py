
# Problem: Capitalize!
# https://www.hackerrank.com/challenges/capitalize/problem

s = input()
print(' '.join(word.capitalize() for word in s.split(' ')))
