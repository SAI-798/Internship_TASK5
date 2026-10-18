
# Problem: The Minion Game
# https://www.hackerrank.com/challenges/the-minion-game/problem

s = input()

kevin = 0
stuart = 0
n = len(s)

for i in range(n):
    if s[i] in "AEIOU":
        kevin += n - i
    else:
        stuart += n - i

if kevin > stuart:
    print("Kevin", kevin)
elif stuart > kevin:
    print("Stuart", stuart)
else:
    print("Draw")
