
roll_number = "1024170409"

digits = [int(d) for d in str(roll_number)[:8]]

# A = {digit x 7 for each digit}, B = {digit x 9 for each digit}
A = {d * 7 for d in digits}
B = {d * 9 for d in digits}

print("Roll number digits:", digits)
print("Set A:", A)
print("Set B:", B)

# vi. Union of A and B
union_set = A | B
print("vi. Union of A and B:", union_set)

# vii. Intersection of A and B
intersection_set = A & B
print("vii. Intersection of A and B:", intersection_set)

# viii. Difference of A and B separately
A_minus_B = A - B
B_minus_A = B - A
print("viii. A - B:", A_minus_B)
print("viii. B - A:", B_minus_A)
print("Difference() keeps only elements unique to one set, while symmetric_difference() keeps elements that are in exactly one of the two sets, not both.")

# ix. Symmetric difference of A and B
symmetric_difference = A ^ B
print("ix. Symmetric difference of A and B:", symmetric_difference)

# x. Subset and superset checks
print("x. A subset of B:", A.issubset(B))
print("x. B superset of A:", B.issuperset(A))

# xi. Ask user for x and discard from A if present
x = int(input("xi. Enter a value x: "))
A.discard(x)
print("xi. Set A after discard(x):", A)
print("discard() is safer than remove() because it does nothing if the value is missing instead of raising a KeyError.")
