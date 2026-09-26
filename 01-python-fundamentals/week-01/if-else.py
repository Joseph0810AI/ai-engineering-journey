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

signal_colr = str(input("Enter the signal colr: ")).strip().lower()

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

u_name = input("Enter the username: ").strip().lower()
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

'''
17. Exam Eligibility

Ask for:

Attendance percentage
Internal marks

Rules:

Attendance must be at least 75%.
Internal marks must be at least 40.

If both conditions are satisfied:

Eligible for exam

Otherwise, display the reason.


'''

att_per = float(input("Enter the attendance Percentage: "))
int_mark = float(input("Enter the internal marks"))

if att_per >= 75 and int_mark >= 40:
    print("Eligible for exam")
elif att_per < 75 and int_mark < 40:
    print("Both attendance per and internal marks are not enough to qualify the exam")
elif att_per >=75 and int_mark < 40:
    print("Internal mark is not enugh")
else:
    print("Attendance is not enough")
"""

18. Online Shopping

Ask for:

Product price
Membership status (yes/no)

Rules:

Members get 20% discount if purchase is ₹2,000 or more.
Members get 10% discount otherwise.
Non-members get 5% discount if purchase is ₹3,000 or more.
Otherwise, no discount.

Calculate the final price.

"""
p_price = float(input("Enter the product price: "))
m_status = input("Select Membership stats yes or no: ").strip().lower()

if m_status == 'yes' and p_price >= 2000:
    discount = p_price *.20
    print("20% discount")
elif m_status == 'yes' and p_price < 2000:
    discount = p_price *.10
    print("10% discount")
elif m_status == 'no' and p_price >=3000:
    discount = p_price *.05
    print("5% discount")
else:
    discount = 0
    print("no discount", p_price)

final_price = p_price - discount
print("Final Price", final_price)

19. Driving Eligibility

Ask for:

Age
Whether the person has a learner's license (yes/no)

Rules:

Below 18 → "Not eligible"
18 or above + license → "Eligible to drive"
18 or above + no license → "Get a learner's license first"

'''

age = int(input("Enter your age: "))
llr = input("Do you have LLR yes/no: ").strip().lower()

if age <18:
    print("Not Eligble")
elif age >=18 and llr == 'yes':
    print("Elgible to drive")
else:
    print("Get a learner's license first")

20. Restaurant Billing

Ask for:

Total bill
Number of people

Rules:

If bill is above ₹5,000, apply 10% discount.
If there are 5 or more people, apply an additional 5% discount.
Display the final bill and amount each person should pay.

'''

total_bill = float(input("Enter your total bill: "))
num_ppl = int(input("Enter the no.of people: "))

if total_bill > 5000 and num_ppl <5:
    discount = total_bill * .10 
    print("10% discount")
elif total_bill > 5000 and num_ppl >=5:
    discount = total_bill * .15
    print("Additional 5% discount")

final_bill = total_bill - discount
avg_bill = final_bill/num_ppl

print("Final Bill", final_bill)
print("Avg bill per person", avg_bill)


'''

21. Leap Year

Ask the user for a year.

Determine whether it is a leap year using:

A year is a leap year if:
- divisible by 400
OR
- divisible by 4 but not divisible by 100

'''

yr = int(input("Enter the year: "))

if yr % 400 == 0 or (yr % 4 == 0 and  yr%100 != 0):
    print("leap year")
else:
    print("no leap year")

'''

22. Triangle Validator

Ask for three side lengths.

Determine:

Whether the sides can form a triangle.
If they can, determine whether it is:
Equilateral
Isosceles
Scalene

'''

s_1 = int(input("Enter the value of side1: "))
s_2 = int(input("Enter the value of side2: "))
s_3 = int(input("Enter the value of side3: "))

if s_1 == s_2 == s_3:
    print("The sides can form Equilateral")
elif s_1 == s_2 or s_2 == s_3 or s_1 == s_3:
    print("The sides can form Isosceles")
else:
    print("The sides can form scalene")

'''

23. Salary Calculator

Ask for an employee's salary.

Calculate tax:

Salary ≤ ₹2,50,000 → No tax
₹2,50,001–₹5,00,000 → 5%
₹5,00,001–₹10,00,000 → 20%
Above ₹10,00,000 → 30%

Display the tax and final salary.

'''

salary = int(input("Enter your salary: "))

if salary <= 250000:
    tax = 0
    print("0% tax", tax)
elif salary > 250000 and salary < 500000:
    tax = salary *.05
    print("5% tax", tax)
elif salary > 500000 and salary < 1000000:
    tax = salary *.20
    print("20% tax", tax)
else:
    tax = salary *.30
    print("30% salary", tax)

final_salary = salary - tax

print("Final salary",final_salary)
    
