from cs50 import get_int

scores = []
for i in range(3):
    scores.append(get_int("Scores: "))

avarage = sum(scores) / len(scores)
print(f"Average: {avarage}")
