#1 )
number = int(input("enter number: "))

if number % 2 == 0:
    print("even")
else:
    print("Odd")


 # 2)   

num = int(input("enter your number: "))

if num > 0:
    print("Positive")
else:
    print("negative")


#3)

age = int(input("enter your age: "))

if age >= 18:
    print("you can vote")
else:
    print("you are young and you cant vote")



#4)

score = int(input("enter your score (from 0 to 10): "))

if score >= 50:
    print("you passed")
else:
    print("you failed")

#5)

password = "1234"

user_input = input("enter your password: ")

if user_input == password:
    print(" password is correct")
else:
    print("password is incorrect")    