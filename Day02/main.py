# This is a sample Python script.

number = int(input("Enter a number: "))
if number > 0:
    print("positive number.")
elif number < 0:
    print("negative number.")
else:
    print("The number is zero.")


age = int(input("Enter your age:"))
if age >=18:
    print("you are old enough to vote.")
else :
    print("you are not old enough to vote.")

num = int(input("Enter a number:"))
if num > 0 and  num % 2 == 0:
    print("the number is positive and even")
else :
    print("the condition is not met.")

for i in range(1, 11):
    print(i)

num = 1
while num <= 10:
    print(num)
    num += 1

for i in range(1, 6):
    if i == 3:
        break
    print(i)

for i in range(1, 6):
     if i == 4:
         continue
     print(i)

# Write a Python program to check if a number is divisible by 5.
num = int(input("Enter a number:"))
if num % 5 == 0:
    print("The number is divisible by 5.")
else:
    print("The number is not divisible by 5.")

# Write a loop that prints only even numbers from 1 to 20.
for i in range (1,21):
    if i % 2 == 0:
        print(i)

# Create a program that asks for a password and keeps asking until the correct password "python123" is entered.
password = input("Enter your password:")
if password == "python123":
    print("Access granted.")
else:
    print("Access denied.")

num = 10
while num >= 1 :
    print(num)
    num -= 1