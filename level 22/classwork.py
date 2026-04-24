password = "ilovegoa"   

user_input = input("type your password here: ")

while user_input != password:
    print(" wrong password! try again")
    user_input = input( "type your password:" )

print(" password correct. welcome user!")




lol = 0

for i in range(5):
    num = int(input("enter your number: "))
    lol += num

print("equals:", lol)


for i in range(20, -1, -1):
    print(i)
