L = [10, 20, 30, 40, 50, 60, 70, 80, 90, 0]
scores = tuple(L[:8])
print(scores)
highest_score = max(scores)
print("Highest score is:", highest_score)
lowest_score = min(scores)
print("Lowest score is:", lowest_score) 
reversed_scores = scores[::-1]
print("Reversed scores are:", reversed_scores) 
reversed_list = list(reversed_scores) # Tuples are immutable, so they cannot be changed in place; therefore, we create a reversed copy.
print("Reversed list is:", reversed_list)
score = int(input("Enter a score: "))
if score in scores : 
    print("first occurence index:" , scores.index(score))
else : 
    print("Score not found in the list.")
    scores[0] = 100
first_score, second_score, *remaining_scores = scores
print("First score is:", first_score)
print("Second score is:", second_score)
print("Remaining scores are:", remaining_scores)