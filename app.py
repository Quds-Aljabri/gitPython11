num1 = 0 
num2= 0
operation = ""
result = 0

num1 = int(input("Please enter the 1st number: "))
num2 = int(input("Please enter the 2nd number: "))
operation = input("Please enter one of + - * or /: ")

if operation == "+":
    result = num1 + num2

if operation == "-":
    result = num1 - num2
else:
    print("[Warn]Operation not supported!")

print("Result is: ",result, "!!!")

print("End of script")