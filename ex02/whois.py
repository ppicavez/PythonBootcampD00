import sys

params = sys.argv

if len(params) != 2:
    print("ERROR")
    sys.exit(0)

if not params[1].isdigit():
    print("ERROR")
    sys.exit(0)

n = int(params[1])

if n:
    if (n % 2):
        print("I'm Odd.")
    else:
        print("I'm Even.")
else:
    print("I'm Zero.")
