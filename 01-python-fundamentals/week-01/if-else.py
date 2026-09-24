#1. Voting Eligibility
#Write a program that asks for a person's age.
#If age is 18 or above, print "You are eligible to vote."
#Otherwise, print "You are not eligible to vote."

my_age = int(input("Enter your age: "))

if my_age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")

#2. Even or Odd

num = int(input("Enter the numner: "))

if num%2 ==0:
    print("It's even number")
else:
    print("It's odd number")

#3. Find the given number is Positive or Negative

num = int(input("Enter the number"))

if num >=0:
    print("Number is positive")
else:
    print("Number is negative")
#4. Temperature
#If temperature is above 30°C, print "It's hot."
#Otherwise, print "The weather is pleasant."

temp_deg_cel = float(input("Enter the temp in degree celcius: "))

if temp_deg_cel > 30:
    print("it's hot")
else:
    print("it's cool")

 """
5. Password Check
Store a password in a variable:
If it matches, print "Login successful"
Otherwise, print "Incorrect password"

"""

pwd_1 = 'Python123'
pwd_2 = str(input("Enter the pwd: "))

if pwd_1 == pwd_2:
    print("Login sucessfull")
else:
    print("Wrong password. Enter the correct password again")
"""
6. Student Grade

90–100 → "Grade A"
75–89 → "Grade B"
50–74 → "Grade C"
Below 50 → "Fail"

"""

mark = float(input("Enter the mark: "))

if mark >=90 and mark <=100:
    print("Grade A")
elif mark >=75 and mark <=89:
    print("Grade B")
elif mark >=50 and mark<74:
    print("Grade C")
else:
    print("Fail")

'''
7. Movie Ticket Price
Ask the user's age.

Below 5 → Free
5–12 → ₹100
13–59 → ₹200
60 or above → ₹120

Print the appropriate ticket price.

'''

age = int(input("Enter your age: "))

if age<5:
    print("Free ticket")
elif age >=5 and age <=12:
    print("Ticket fare 100 Rs")
elif age >=13 and age <=59:
    print("Ticket fare is 200Rs")
else:
    print("Ticket fare is 120 Rs")
'''
8. Number Comparison

Ask the user to enter two numbers.

Print:

"First number is greater"
"Second number is greater"
"Both numbers are equal"

'''

num_1 = float(input("Enter the number1: "))
num_2 = float(input("Enter the number2: "))

if num_1 > num_2:
    print("First number is greater")
elif num_1 < num_2:
    print("Second number is greater")
else:
    print("Both numbers are equal")
'''
9. Traffic Signal

Ask the user to enter a traffic signal:

red
yellow
green
'''

signal_colr = str(input("Enter the signal colr: "))

if signal_colr == 'red':
    print("Stop")
elif signal_colr == 'yellow':
    print("get ready")
elif signal_colr == 'green':
    print("go")
else:
    print("invalid signal")

'''
10. Simple Calculator

Ask the user for:

First number
Second number
Operator (+, -, *, /)

'''

num_1 = float(input("Enter the First Num: "))
num_2 = float(input("Enter the second Num: "))
operator = str(input("Enter the operator: "))

if operator == '+':
    print("Add the number", num_1 + num_2)
elif operator == '-':
    print("Subsreact the number", num_1 - num_2)
elif operator == '*':
    print("Multiply the numbers", num_1 * num_2)
elif operator == '/':
    print("Divide the numbers", num_1/num_2)
else:
    print("Invalid operator")

'''
11. ATM Withdrawal

An ATM has a balance of ₹10,000.

Ask the user how much they want to withdraw.

If amount is greater than the balance → "Insufficient balance"
If amount is not a multiple of 100 → "Enter amount in multiples of 100"
Otherwise → display the remaining balance.

'''

balance = 10000
withdraw = int(input("Enter the withdrawl amount: "))

if withdraw > balance:
    print("Insufficient balance")
elif withdraw % 100 != 0:
    print("Enter amount in muliple of 100")
else:
    print("remaining balance: ", balance - withdraw )

'''
12. Shopping Discount

Ask the customer for their total shopping amount.

₹5,000 or more → 20% discount
₹3,000–₹4,999 → 10% discount
₹1,000–₹2,999 → 5% discount
Below ₹1,000 → No discount

Print the final amount after discount.

'''

amt = float(input("Enter the total shopping amount: "))

if amt >= 5000:
    print("20% Discount", amt-(amt*20/100))
elif amt >= 3000 and amt <= 4999:
    print("10% discount", amt - (amt*10/100))
elif amt >=1000 and amt <= 2999:
    print("5% discount", amt - (amt*5/100))
else:
    print("No discount", amt)

'''
13. Electricity Bill

Ask the user for the number of electricity units consumed.

Use these rates:

0–100 units → ₹2/unit
101–200 → ₹3/unit
201–300 → ₹5/unit
Above 300 → ₹7/unit

Calculate and display the bill.

'''

e_unit = int(input("Enter the electricity units: "))

if e_unit>=0 and e_unit <=100:
    print("2rs/unit", e_unit*2,"rs")
elif e_unit>=101 and e_unit<=200:
    print("3rs/unit", e_unit*3,"rs")
elif e_unit>=201 and e_unit<=300:
    print("5rs/unit", e_unit*5,"rs")
else:
    print("7rs/unit", e_unit*7,"rs")

''''
14. Login System

Create a simple login system.

Ask the user for username and password.

Possible outputs:

Both correct → "Login successful"
Username correct but password wrong → "Incorrect password"
Username wrong → "User not found"

'''

user_name = 'mypython'
pwd = 'Python123'

u_name = input("Enter the username: ")
pwd1 = input("Enter the pwd: ")

if user_name == u_name and pwd == pwd1:
    print("Login Sucessfull")
elif user_name != u_name and pwd==pwd1:
    print("User name is wrong. Enter the correct username")
else:
    print("Pwd is wrong. Enter the correct pwd")

'''
15. College Admission

Ask the student for:

Marks
Age

A student is eligible if:

Marks are 60 or above
AND age is 17 or above

Otherwise, print why they are not eligible.

'''

marks = int(input("Enter the marks: "))
age = int(input("Enter your age: "))

if marks >= 60 and age >= 17:
    print("Eligible for admission")
elif marks <60 and age >=17:
    print("Marks are not enough to qualify")
elif marks >=60 and age <17:
    print("Age is not enough to qualify")
else:
    print("both age and marks are not enough to qualify")

''''

16. Bank Loan Eligibility

Ask for:

Age
Monthly salary
Credit score

Rules:

Age must be at least 21.
Salary must be at least ₹25,000.
Credit score must be at least 700.

Use nested if statements and display the appropriate reason when 
the applicant is rejected.


'''

age = int(input("Enter the age: "))
m_sal = float(input("Enter your salary: "))
c_score = float(input("Enter your credit score: "))

if age >= 21 and m_sal >=25000 and c_score >=700:
    print("Eligible for loan")
elif age < 21:
    print("Your eligble age must be atleast 21")
elif m_sal<25000:
    print("Loan elgible salary atleast 25k per month")
else:
    print("Loan eligible credit score atleast 700")
