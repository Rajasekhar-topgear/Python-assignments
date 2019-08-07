import sys

arg_len = len(sys.argv)

print ("Number of arguments:", arg_len - 1, "arguments.")

for i in range(1, arg_len):
    print ("Argument", i, "::", sys.argv[i])

if (arg_len- 1) != 3:
    print("Arguments are ", arg_len - 1, "please pass 3 arguments to find biggest number")
else:
    x = int(sys.argv[1])
    y = int(sys.argv[2])
    z = int(sys.argv[3])
    if (x > y) and (x > z):
        print("Biggest number is ::", x)
    elif (y > x) and (y > z):
        print("Biggest number is ::", y)
    else:
        print("Biggest number is ::", z)

