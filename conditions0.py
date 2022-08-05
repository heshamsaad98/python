from cs50 import get_string

s = get_string("Do you agree?\n")

if s == "Y" or s == "y":
    print("Agreed.")
elif s == "N" or s == "n":
    print("Not agread.")
