a1 = int(input("Enter the number-1: "))
a2 = int(input("Enter the number-2: "))
a3 = int(input("Enter the number-3: "))
a4 = int(input("Enter the number-4: "))
 

print("Using If and ELIf :: ")
if (a1 > a2) and (a1 > a3) and (a1 > a4):
    print("Biggest number is::", a1)
elif (a2 > a1) and (a2 > a3) and (a2 > a4):
    print("Biggest number is::", a2)
elif (a3 > a1) and (a3 > a2) and (a3 > a4):
    print("Biggest number is::", a3)
else:
    print("Biggest number is::", a4)


print("Nested IF:: ")
if (a1 > a2):
    if (a1 > a3):
        if (a1 > a4):
            print("Biggest number is::", a1)

if (a2 > a1):
    if (a2 > a3):
        if (a2 > a4):
            print("Biggest number is::", a2)

if (a3 > a1):
    if (a3 > a2):
        if (a3 > a4):
            print("Biggest number is::", a3)

if (a4 > a1):
    if (a4 > a2):
        if (a4 > a3):
            print("Biggest number is::", a4)

print("Use IF and IF & Else")
if (a1 > a2):
    if (a1 > a3):
        if (a1 > a4):
            print("Biggest number is::", a1)
        else:
            print("Biggest number is::", a4)
    else:
        if (a3 > a4):
            print("Biggest number is::", a3)
        else:
            print("Biggest number is::", a4)
else:
    if (a2 > a3):
        if (a2 > a4):
            print("Biggest number is::", a2)
        else:
            print("Biggest number is::", a4)
    else:
        if (a3 > a4):
            print("Biggest number is::", a3)
        else:
            print("Biggest number is::", a4)            


a5 = int(input("Enter the number-5: "))
print("Using If and ELIf :: ")
if (a1 > a2) and (a1 > a3) and (a1 > a4) and (a1 > a5):
    print("Biggest number is::", a1)
elif (a2 > a1) and (a2 > a3) and (a2 > a4) and (a2 > a5):
    print("Biggest number is::", a2)
elif (a3 > a1) and (a3 > a2) and (a3 > a4) and (a3 > a5):
    print("Biggest number is::", a3)
elif (a4 > a1) and (a4 > a2) and (a4 > a3) and (a4 > a5):
    print("Biggest number is::", a4)
else:
    print("Biggest number is::", a5)


print("Nested IF:: ")
if (a1 > a2):
    if (a1 > a3):
        if (a1 > a4):
            if (a1 > a5):
                print("Biggest number is::", a1)

if (a2 > a1):
    if (a2 > a3):
        if (a2 > a4):
            if (a2 > a5):
                print("Biggest number is::", a2)

if (a3 > a1):
    if (a3 > a2):
        if (a3 > a4):
            if (a3 > a5):
                print("Biggest number is::", a3)

if (a4 > a1):
    if (a4 > a2):
        if (a4 > a3):
            if (a4 > a5):
                print("Biggest number is::", a4)

if (a5 > a1):
    if (a5 > a2):
        if (a5 > a3):
            if (a5 > a4):
                print("Biggest number is::", a5)


print("Use IF and IF & Else")
if (a1 > a2):
    if (a1 > a3):
        if (a1 > a4):
            if (a1 > a5):
                print("Biggest number is::", a1)
            else:
                print("Biggest number is::", a5)
        else:
            if (a4 > a5):
                print("Biggest number is::", a4)
            else:
                print("Biggest number is::", a5)
    else:
        if (a3 > a4):
            if (a3 > a5):
                print("Biggest number is::", a3)
            else:
                print("Biggest number is::", a5)
        else:
            if (a4 > a5):
                print("Biggest number is::", a4)
            else:
                print("Biggest number is::", a5)
else:
    if (a2 > a3):
        if (a2 > a4):
            if (a2 > a5):
                print("Biggest number is::", a2)
            else:
                print("Biggest number is::", a5)
        else:
            if (a4 > a5):
                print("Biggest number is::", a4)
            else:
                print("Biggest number is::", a5)
    else:
        if (a3 > a4):
            if (a3 > a5):
                print("Biggest number is::", a3)
            else:
                print("Biggest number is::", a5)
        else:
            if (a4 > a5):
                print("Biggest number is::", a4)
            else:
                print("Biggest number is::", a5)

            
                
                
