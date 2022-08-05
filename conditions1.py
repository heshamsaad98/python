from cs50 import get_string

s = get_string("Do you agree?\n")

if s in ["y", "Y", "yes", "Yes"]:
    print("Agreed.")
elif s in ["n", "N", "no", "No"]:
    print("Not agread.")
