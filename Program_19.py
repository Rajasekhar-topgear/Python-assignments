
print("Prime Numbers 1 to 100 using FOR LOOP, continue for ODD numbers")
for num in range(1,101):
    if (num % 2 == 0):
        print(num)
    else:
        continue

print("Prime Numbers 1 to 100 using FOR LOOP, pass for ODD numbers")

for num in range(1,101):
    if (num % 2 == 0):
        print(num)
    else:
        pass

print("Prime Numbers 1 to 100 using FOR LOOP, BREAK if number is 50")

for num in range(1,101):
    if (num == 50):
        break
    if (num % 2 == 0):
        print(num)

print("Prime Numbers 1 to 100 using FOR LOOP, CONTINUE if number is 10/20/30/40/50")
for num in range(1,101):
    if (num == 10 or num == 20 or num == 30 or num == 40 or num == 50):
        continue
    
    if (num % 2 == 0):
        print(num)
            
        

print("Prime Numbers 1 to 100 using WHILE LOOP, continue for ODD numbers")
num = 1

while (num <= 100):
    if (num % 2 == 0):
        print(num)
        num+=1
    else:
        num+=1 
        continue
    

print("Prime Numbers 1 to 100 using WHILE LOOP, pass for ODD numbers")
num=1
while (num <=100):
    if (num % 2 == 0):
        print(num)
    else:
        pass
    num+=1
    
print("Prime Numbers 1 to 100 using WHILE LOOP, BREAK if number is 90")
num=1
while (num <= 100):
    if (num == 90):
        break
    if (num % 2 == 0):
        print(num)
    num+=1

print("Prime Numbers 1 to 100 using WHILE LOOP, CONTINUE if number is 60/70/80/90")
num=1
while (num <= 100):
    if (num == 60 or num == 70 or num == 80 or num == 90):
        num+=1 
        continue
    
    if (num % 2 == 0):
        print(num)
    num+=1
    
        
