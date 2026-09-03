import random
random.seed(1234567890)

# i. Generate 100 random numbers between 100 and 900
numbers = [random.randint(100, 900) for _ in range(100)]

print("Random numbers:")
print(numbers)


# ii. Count odd numbers
odd_numbers = [x for x in numbers if x % 2 != 0]

print("Number of odd numbers:", len(odd_numbers))


# iii. Count even numbers
even_numbers = [x for x in numbers if x % 2 == 0]

print("Number of even numbers:", len(even_numbers))


# iv. Find prime numbers
def is_prime(n):
    if n < 2:
        return False

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False

    return True


prime_numbers = [x for x in numbers if is_prime(x)]

print("Number of prime numbers:", len(prime_numbers))
print("Prime numbers:", prime_numbers)


# v. Find most frequent number
most_frequent = max(set(numbers), key=numbers.count)
frequency = numbers.count(most_frequent)

print("Most frequent number:", most_frequent)
print("Number of occurrences:", frequency)