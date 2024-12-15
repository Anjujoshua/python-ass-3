#1, Name your file: MonthNames.py Write a program that reads an integer value between 1 and 12 from the user and prints
# output the corresponding month of the year.
from math import factorial

month_number = int(input("Enter a month number (1-12): "))
months = {1: "January", 2: "February", 3: "March", 4: "April",
    5: "May", 6: "June", 7: "July", 8: "August",
    9: "September", 10: "October", 11: "November", 12: "December"}
if 1 <= month_number <= 12:
    print(f"Month {month_number} is {months[month_number]}")
else:
    print("Invalid input! Please enter a number between 1 and 12.")

#2. A certain cinema currently sells tickets for a full price of 6 pounds, but always sells tickets for half price to people who
# are less than 16 years old, and for a third of the price for people who are 60 years old or more.
age = int(input("Enter your age: "))
if age < 16:
    print('Your ticket rate','\u00A33.00')
elif age >= 60:
    print('Your ticket rate','\u00A34.00')
else:
    print('Your ticket rate', '\u00A36.00')

#3.

weight = float(input("Enter your weight in (kg): "))
height = float(input("Enter your height in (m): "))
Bmi = weight / (height**2)
if Bmi < 18.5:
 print('you are "underweight"')
elif 18.5 <= Bmi <= 24.9:
    print('you are "normalweight"')
elif 25 <= Bmi <= 29.9:
    print('you are "overweight"')
else:
    print('you are "Above obese"')

#4.

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))
greatest = max(num1, num2, num3)
print(f"The greatest number is: {greatest}")

#5.

num=int(input('enter a number:'))
factorial=1
if num==0 or num==1:
    print('factorial is1')
elif num<0:
    print('enter a positive number')
else:
 for i in range(1,num+1):
     factorial=factorial*i
     print('factorial of the number is',factorial)


#6.
num = int(input("Enter a number: "))
reversed_num = 0
while num > 0:
    last_digit = num % 10
    reversed_num = reversed_num * 10 + last_digit
    num = num // 10
    print(f"The reversed number is: {reversed_num}")


#7.
num = int(input("Enter a number: "))
n = int(input("How many multiples would you like to see? "))
print(f"The first {n} multiples of {num} are:")
for i in range(1, n + 1):
    print(num * i)

#8.

while True:
 user_input = input("Enter a value: ")
 if user_input.lower() == 'done':

    print(user_input)
    print("Loop has been terminated.")

#9.

 for i in range(1, 16):
  if 1%3==0 and i%5==0:
     print('FizzBuzz')
  elif i%5==0:
      print('Buzz')
  elif i%3==0:
      print('Fizz')
  else:
      print(i)

#10.

    for i in range(5, 0, -1):
    for j in range(i, 0, -1):
     print(j, end=" ")
     print()






































































