#ass5.1
a = input("Enter First num: ")
b = input("Enter Second num: ")
c = input("Enter Third num: ")
print(max(a, b, c))

#ass5.2

n = int(input("Enter a number: "))
s = 0 
for i in range(1, n+1):
    if i % 7 ==0 and i %9 == 0 :
        s += i
        print("Sum of all numbers from 1 to", n, "that are divisible by both 7 and 9 is:",s)

n = int(input("Enter n: "))

#ass5.3
total = 0

for num in range(2, n + 1):
    prime = True

    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            prime = False
            break

    if prime:
        total += num

print("Sum of prime numbers =", total)