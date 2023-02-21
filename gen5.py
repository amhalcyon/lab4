def nums():
    for i in range(n,-1,-1):
        yield i

n = int(input())

for i in nums():
    print(i, end=' ')