def add(a,b):
    return a + b
print(add(5, 6))
print(add("Hello ", "World!"))
print(add(20,200))



def IsPrime(n):
	for i in range(2, n//2 + 1):
		if n%i==0:
			return 0
	return 1
print ("IsPrime(20)  --> ", IsPrime(20))
print ("IsPrime(23)  --> ", IsPrime(23))
print ("IsPrime(200) --> ", IsPrime(200))
print ("IsPrime(37)  --> ", IsPrime(37))

def addN(n):
    s = sum(range(1,n+1))
    return s 
print(addN(10))
print(addN(100))

ass6.1
def sum_odd(n):
    total = 0
    for i in range(1, n + 1):
        if i % 2 != 0:
            total += i
    return total

n = int(input("Enter n: "))
print("Sum of odd numbers =", sum_odd(n))

ass6.2

def is_prime(num):
    if num < 2:
        return False

    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False

    return True


def sum_prime(n):
    total = 0

    for i in range(2, n + 1):
        if is_prime(i):
            total += i

    return total


n = int(input("Enter n: "))
print("Sum of prime numbers =", sum_prime(n))