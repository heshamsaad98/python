from cs50 import get_string

s = get_string("Do you agree?\n")

if s == "Y":
    print("Agreed.")
elif s == "N":
    print("Not agread.")
