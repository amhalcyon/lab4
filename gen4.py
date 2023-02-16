def squares():
    for i in range(a,b+1):
        i = i*i
        yield i

a = int(input())
b = int(input())

for i in squares():
    print(i, end=' ')