x = [1,2,3,4,5,6,7,8,9,10]

print("Elements in the list::", x)

start = int(input("Enter the slice starting index:: "))
end = int(input("Enter the slice ending index:: "))
print("Slice of the list::", x[start:end])

repeat = int(input("Enter the number of times to repeat the list::"))
print("Repeat::", x * repeat)

y = [30,31,32,33,34,35,36,37,38,39,40]

print("List - 1::", x)
print("List - 2::", y)
print("Concatenation of lists:: ", x + y)


