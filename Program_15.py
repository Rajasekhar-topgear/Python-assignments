names = ["aaa", "bbb", "ccc", "ddd", "eee"]

def fun1():
    str = input("Enter the string::")
    res = str in names

    if res:
        print("String", str, "is present in the list")
    else:
        print("Element is not present in the list")

def fun2():
    str = input("Enter the string::")

    for item in names:
        if (item == str):
            print("Element present in the list")
            break
    else:
        print("Element is not present in the list")

def fun3():
    
    print("Elements in reverse order::") 

    names.reverse()
    print(names)
    
fun1()
fun2()
fun3()


    
    
