from cs50 import get_string

s = get_string("Do you agree?\n")

if s.lower() in ["y", "yes"]:
    print("Agread.")
elif s.lower() in ["n", "no"]:
    print("Not agread")
