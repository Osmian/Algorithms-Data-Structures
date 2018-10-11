#Create a fibonacci sequence n-times
def fib_create(n):
    fibs = [0 for x in range(n)]
    fibs[0],fibs[1] = 1,2
    for x in range(2,n):
        fibs[x] = fibs[x-1]+fibs[x-2]
    return fibs

print(fib_create(10))
