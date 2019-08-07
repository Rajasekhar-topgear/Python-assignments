
fib = [0,1]
n = int(input("Enter how many fibonacci numbers::"))

a = 0
b = 1
for i in range(2,n):
    c = a + b 
    a = b 
    b = c 
    fib.append(c)  

print("Fibonacci series::")
for i in range(0, n):
    print(fib[i])


n = int(input("Enter the Max number of fibonacci series::"))

print("Fibonacci series till", n, "::")
for i in range(0, len(fib)):
    if (fib[i] <= n):
        print(fib[i])
    else:
        break

    
