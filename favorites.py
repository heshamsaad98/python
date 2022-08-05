import csv

counts = {}

with open("CS50 2019 - Lecture 7 - Favorite TV Shows (Responses) - Form Responses 1.csv", "r") as file:
    reader = csv.DictReader(file)
    
    for row in reader:
        title = row["title"].lower()
        if title in counts:
            counts[title] += 1
        else:
            counts[title] = 1
def f(item):
    return item[1]

for title, count in sorted(counts.items(), key = f, reverse = True):
    print(title, count, sep=" | ")
