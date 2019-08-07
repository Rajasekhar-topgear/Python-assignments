emp_id = [100,101,102,103,104,105,106,107,108,109,110]
emp_name = ["aaa","bbb","ccc","ddd","eee","fff","ggg","hhh","iii","jjj"]

def fun1():
    print("Employee names::")
    for i in range(0,10):
        print(emp_name[i])

def fun_emp_id():
    print("Employee id::")
    for i in range(0,10):
        print(emp_id[i])
        
def fun2():
    i = int(input("Enter  the index::"))
    print("Employee name and id ::")
    print(emp_name[i], emp_id[i])

def fun3():
    print("Employee names from 4th position to 9th position::")
    for i in range(4,9):
        print(emp_name[i])

def fun4():
    print("Employee names from 3rd position till end ::")
    for i in range(3,10):
        print(emp_name[i])

def fun5(x):
    print("Elements", x, "repeated::")
    for i in range(0, x):
        fun1()
        fun_emp_id()

def fun6():
    print("Concatenated list::")
    concat_list = emp_name + emp_id
    print(concat_list)

def fun7():
    print("Emplayee names and id's:: ")
    for i in range(0,10):
        print(emp_name[i], "\t", emp_id[i])


fun1()
fun2()
fun3()
fun4()

r = int(input("Enter the number of times the elements to be printed::"))
fun5(r)

fun6()
fun7()



