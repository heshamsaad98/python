import cs50
import csv

open(f"shows4.db", "w").close()
db = cs50.SQL("sqlite:///shows4.db")
db.execute("CREATE TABLE shows (id INT, title TEXT, year NUMERIC, PRIMARY KEY(id))")
db.execute("CREATE TABLE genres (show_id INT, genre TEXT, FOREIGN KEY(show_id) REFERENCES shows(id))")
with open("title.basics.tsv", "r") as titles:
    reader = csv.DictReader(titles, delimiter="\t")
    for row in reader:
        if row["titleType"] == "tvSeries" and row["isAdult"] == "0":
            if row["startYear"] != "\\N":
                startYear = int(row["startYear"])
                if startYear >= 1970:
                    id = int(row["tconst"][2:])
                    db.execute("INSERT INTO shows (id, title, year) VALUES(?, ?, ?)", id, row["primaryTitle"], startYear)
                    if row["genres"] != "\\N":
                        for genre in row["genres"].split(","):
                            db.execute("INSERT INTO genres (show_id, genre) VALUES(?, ?)", id, genre)
