str = input("Enter the string1:: ")

for a in str:
    print(a)

x = int(input("starting index of the slice string:: "))
y = int(input("ending index of the slice string:: "))

print ("Slice string:: ", str[x:y])

print("Repeat string 100 times::")
print(str * 100)

str1 = input("Enter another string2:: ")

print("Concatenation of strings:: ", str + str1)


