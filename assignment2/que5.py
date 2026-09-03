my_dict = {
    "name": "Your Name",
    "roll_no": "your roll number",
    "branch": "your branch",
    "age": 19,
    "city": "your home city"
}

my_dict["location"] = my_dict.pop("city")
my_dict["cgpa"] = 8.3
my_dict["age"] = my_dict["age"] + 1

dict_with_pop = my_dict.copy()
dict_with_del = my_dict.copy()

dict_with_pop.pop("branch")
del dict_with_del["branch"]

print("pop() returns the removed value, while del returns nothing and raises KeyError if the key is missing.")

for key, value in my_dict.items():
    print(f"{key} → {value}")

if "email" in my_dict:
    print(f"email: {my_dict['email']}")
else:
    print("email not found in the dictionary")

friend_dict = {
    "name": "Friend Name",
    "roll_no": "20240000",
    "branch": "CSE",
    "age": 20,
    "city": "Delhi"
}

merged_dict = {**my_dict, **friend_dict}
print(merged_dict)
print("When both dictionaries share a key, the later dictionary's value wins during merge.")

string_dict = {key: value for key, value in my_dict.items() if isinstance(value, str)}
print(string_dict)
