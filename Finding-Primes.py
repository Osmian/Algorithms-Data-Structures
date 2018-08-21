#Generate a list of prime numbers less than n


def findPrimes(n):

    primes=[1]
    for num in range(2,n+1):
        isPrime = True
        for x in range(2,int(num**0.5)+1):
            if num%x==0:
                isPrime=False
                break
        if(isPrime):
            primes.append(num)

    print(primes)

findPrimes(100)
