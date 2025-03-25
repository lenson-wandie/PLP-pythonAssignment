num1= float(input("Enter the first number: " ))
num2= float(input("Enter the second number: " ))
operator = input("Enter the operation(+,-,*,/): " )
result = 0.0
if operator == "+":
 result = (num1 + num2)
   
elif operator == "-":
 result = (num1 - num2)

elif operator == "/":
    if num2 == 0:
        print("You can't divide by zero")
    else:
      result = (num1 / num2)
    
elif operator == "*":
 result = (num1 * num2)
    
else :
 result = "Invalid operator"
    
print(f" {num1} {operator} {num2} = {result}")