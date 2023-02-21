def square():
    for i in range(n+1):
        i = i*i
        yield i

n = int(input())

for i in square():
    print(i, end=' ')