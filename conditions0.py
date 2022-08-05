from cs50 import get_string

s = get_string("Do you agree?\n")

if s == "Y" or "y":
    print("Agreed.")
elif s == "N" or "n":
    print("Not agread.")
