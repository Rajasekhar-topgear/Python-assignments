numbers = []
num = int(input("Enter how many numbers in the list: "))
for n in range(num):
    elem = int(input("Enter number:: "))
    numbers.append(elem)
print("Biggest element in the list is :: ", max(numbers))
print("Smallest element in the list is :: ", min(numbers))

def find_small_num():
    smallest = numbers[0]
    for n in range(0,num):
        if (numbers[n] < smallest):
            smallest = numbers[n]

    print("Smallest number::", smallest)


def find_big_num():
    biggest = numbers[0]
    for n in range(0,num):
        if (numbers[n] > biggest):
            biggest = numbers[n]

    print("Biggest number::", biggest)


find_small_num()
find_big_num()


