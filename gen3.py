def div():
    for i in range(n+1):
        if i%3 == 0:
            yield i
        elif i%4 == 0:
            yield i

n = int(input())

for i in div():
    print(i, end=' ')