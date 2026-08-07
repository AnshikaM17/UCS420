i = 1 
while i <= 10:
    print(i)
    i += 1

    print ("range(10) --> ", list(range(10)))
    print ("range(10,20) --> ", list(range(10,20)))
    print ("range(0, 10, 2) --> ", list(range(2, 10, 2)))
    print ("range(10, -20, 2) --> ", list(range(-10, -20, 2)))
    print ("range(-10, -20, 2) --> ", list(range(-10, -20, -2)))

# forloop
for i in range(0,10): 
    print(i)

for i in range(0,20,2): 
    print(i)

    for i in range(0 , -10 , -1):
        print(i)

#sum  of all numbers from 1 to 10
        s = 0 
        for i in range(1, 11):
            s += i
        print("Sum of first 10 natural numbers is:", s)



# ass4.1
for i in range(1, 11):
    print(7, "x", i, "=", 7*i)

for i in range(1, 11):
    print(9, "x", i, "=", 9*i)


# ass4.2
n = int(input("Enter a number: "))
for i in range(1, 11):
    print(n, "x", i, "=", n*i)

# ass4.3
n = int(input("Enter a number: "))
total = 0
for i in range(1, n+1):
    total += i
    print(total)