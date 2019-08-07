
num = int(input("Enter the number::"))

if num > 1: 
      
   for i in range(2, num//2): 
       if (num % i) == 0: 
           print(num, "is not a prime number") 
           break
   else: 
       print(num, "is a prime number") 
  
else: 
   print(num, "is not a prime number") 


number = int(input("Enter the number for prime numbers:"))
             
primes = []

for j in range(2, number):
    isPrime = True
    for k in range(2, j):
        if (j % k == 0):
            isPrime = False
      
    if isPrime:
        primes.append(j)

print("Prime numbers::", primes)

             
