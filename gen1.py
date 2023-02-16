def square():
    for i in range(x):
        i = i*i
        yield i

x = int(input())

for i in square():
    print(i, end=' ')