A = 56565
B = 65662
C = A + B
print(C)
 
#code 2
physics = 40
chemistry = 95
maths = 56
total = maths + chemistry + physics
print(total)

#code 3
quantity = 20
price = 3
bill = quantity * price
print(bill)

#code 4
product = "7up"
quantity = 3
price = 20
bill = quantity * price
print("Product:" , product)
print("Quantity:" , quantity)
print("Price:" , price)
print("--------------------")
print("bill is" , bill)  
print("--------------------")
 
#code 5
rint("A")
nam = input("Please Enter you name:")
print("--------------------")
print("Your name is:",nam)

#code 6
num1 = input("Please First Num:")
num2 = input("Please Second Num:")
print("--------------------")
result = int(num1) + int(num2)  #int() function
print("The result is :",result)

#----------------------------
num1 = (float(input("Enter first number: "))) 
num2 = (float(input("Enter second number: "))) 
sum = num1 + num2
print("----------------------------------------------")
print("The result of the 'string addition' is: ",sum)
print("----------------------------------------------")

#code 7 
name = input("Enter Employee's Name:")
salary = input("Enter Employee's Salary:")

tax = float(salary) * 21/100
netsalary = float(salary) - tax
print("------------------------------")
print("Tax is :",tax)
print("Net Salary is :",netsalary)
print("------------------------------")

#code 8
temp = 5
if temp < 5:
    print("low 5")
if temp > 5:
     print("over 5")
if temp == 5:
     print(" 5") 

#code 9
name = input("Enter Employee's Name:")
salary = input("Enter Employee's Salary:")

if float(salary) > 100:
    tax = float(salary) * 21/100

if float(salary) <= 100:
    tax = float(salary) * 20/100    

netsalary = float(salary) - tax
print("------------------------------")
print("Tax is :",tax)
print("Net Salary is :",netsalary)
print("------------------------------") 

#code10
temp =   int(input("temp today: "))
if temp > 50:
    print("hoot")
else  :
    print("coold")
print("-----------------") 

#code 10
salary =   int(input("Pay today: "))

if salary >= 1000:
    if salary >= 10000:
        tax = salary * 25/100
    else :
       tax = salary * 15/100

else  :
    tax = 0

netSalary = salary - tax    
print("-----------------")   
print("Tax is :",tax)
print("Salary is :",salary)
print("NetSalary is :",netSalary)

