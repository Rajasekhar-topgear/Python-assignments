
print("Numbers from 1 to 100 using FOR LOOP")

for i in range (1,101):
    print(i)

print("Numbers from 100 to 1 using FOR LOOP")

for i in range (100, 0, -1):
    print(i)

    
print("Numbers from 1 to 100 using WHILE LOOP")

i = 1
while (i <= 100):
    print(i)
    i+=1
    
print("Numbers from 100 to 1 using WHILE LOOP")

i = 100
while (i >= 1):
    print(i)
    i-=1


str = "Hello World"

print("Print the string using FOR LOOP:")
for x in range(0, len(str)):
    print(str[x])

    
print("Print the string using WHILE LOOP:")
str_len = len(str)
i = 0

while (i < str_len):
    print(str[i])
    i+=1   
    

    
