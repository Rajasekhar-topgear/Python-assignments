
total_numbers = []

print("Enter 10 numbers::")

for n in range(0, 10):
    number = int(input("Enter the number::"))
    total_numbers.insert(n, number)


average = sum(total_numbers)/10

print("Average of 10 numbers:: ", average)

print("Numbers greater than average")
for i in range(0, 10):
    if (total_numbers[i] > average):
        print(total_numbers[i])

print("Numbers less than average")
for i in range(0, 10):
    if (total_numbers[i] < average):
        print(total_numbers[i])        

    
