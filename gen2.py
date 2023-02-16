def even():
    for i in range(x):
        if i%2 == 0:
            yield i

x = int(input())

for i in even():
    print(i, end=',')