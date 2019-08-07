a = int(input("Enter the number-1::"))

b = int(input("Enter the number-2::"))

c = a & b

print("Bitwise AND operation of", a, b, "is ::", c)

c = a | b

print("Bitwise OR operation of", a, b, "is ::", c)

c = a ^ b

print("Bitwise XOR operation of", a, b, "is ::", c)

c = ~a
d = ~b

print("One's compliment of", a, b, "is ::", c, d)

c = a >> 1
d = b >> 1

print("Right shift operation of", a, b, "by 1 bit is ::", c, d)


c = a << 1
d = b << 1

print("Left shift operation of", a, b, "by 1 bit is ::", c, d)
