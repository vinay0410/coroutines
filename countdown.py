def countdown(n):
    print "Counting Down from", n
    while n > 0:
        yield n
        n -= 1

for i in countdown(5):
    print i,

x = countdown(10)
print(x)

print(x.next())
print(x.next())

x = countdown(2)

print(x.next())
print(x.next())
print(x.next())