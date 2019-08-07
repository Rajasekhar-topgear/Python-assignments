numbers = []
num = int(input("Enter how many numbers in the list: "))
for n in range(num):
    elem = int(input("Enter number:: "))
    numbers.append(elem)
print("Maximum element in the list is :: ", max(numbers))
print("Minimum element in the list is :: ", min(numbers))
