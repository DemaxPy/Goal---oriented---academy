#2

number =13

if number >= 10:
    print("more than 10")
else:
 print("less than 10")
    

#3
    
number = int(input("Enter a number: "))

if number == 15:
 print("equal to 15")
else:
    print("not equal to 15")


#4

user_input = input("Enter a string: ")

if user_input == "group84":
    print("you are correct")
else:
   print("you are wrong")

#5

for i in range(50, 101, 5):
    print(i)


#6 
name = "Demetre"

for letter in name:
 print(letter)

#7   
num = 20

while num <= 50:
    print(num)
    num += 1


#8

for i in range(0, 101):
    print(i)

while num <= 100:
    print(num)
    num += 1

#9
for i in range(10,21):
  print(i)

#13
number = float(input("Enter a number: "))

if number > 0:
    print("This number is positive")
elif number < 0:
    print("This number is negative")
else:
    print("This number is zero")

#14

age = int(input("Enter your age: "))

if age < 0:
    print("Incorrect information")
elif age <= 12:
    print("You are a child")
elif age <= 19:
    print("You are a teenager")
elif age <= 64:
    print("You are an adult")
elif age <= 120:
    print("You are elderly")
else:
    print("You are a guru or wizard")
    

#15

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))

if num1 >= num2 and num1 >= num3:
    print("Largest number is:", num1)
elif num2 >= num1 and num2 >= num3:
    print("Largest number is:", num2)
else:
    print("Largest number is:", num3)
    


#16

day = int(input("შეიყვანეთ რიცხვი 1-დან 7-მდე: "))

if day == 1:
    print("ორშაბათი")
elif day == 2:
    print("სამშაბათი")
elif day == 3:
    print("ოთხშაბათი")
elif day == 4:
    print("ხუთშაბათი")
elif day == 5:
    print("პარასკევი")
elif day == 6:
    print("შაბათი")
elif day == 7:
    print("კვირა")
else:
    print("არ ვიცი ეგ რა დღეა")    

#17


number = float(input("Enter a number: "))

if number > 50:
    print(number * 5)
else:
    print(number ** 2)




#18


number = float(input("შეიყვანეთ რიცხვი: "))

if number > 50:
    print(number * 5)
else:
    print(number ** 2)

#19

password = input("Enter password: ")

if password == "goa123":
    print("Password is correct!")
else:
    print("Incorrect password!")



#20

number = int(input("Enter a number: "))
sum = 0

for i in range(1, number + 1):
    sum += i

print("Sum:", sum)

