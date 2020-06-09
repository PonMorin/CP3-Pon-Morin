x = int(input())
star = 1
for i in range(x):
    print(" " * (x-i) + "*"*star)
    star += 2
    print(x-i)
