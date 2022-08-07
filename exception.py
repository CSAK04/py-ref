
b=int(input("divide 10 by"))

try:
    a=10/b
    print(a)
    print("try completed")
except ZeroDivisionError:
    print("can't divide a number by zero")

print("program completed")
