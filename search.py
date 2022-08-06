import csv 
title = input("Title: ") 
with open("shows2.csv", "r") as input: 
  reader = csv.DictReader(input)
  for row in reader: 
      if title.lower() == row["primaryTitle"].lower(): 
          print(row["primaryTitle"], row["startYear"], row["genres"], sep=" | ")
