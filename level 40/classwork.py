def greet():
    print("Hello!")

# ფუნქცია არის კოდის ნაწილი, რომელიც რაღაც მოქმედებას ასრულებს. მისი გამოყენება რამდენჯერმე შეგვიძლია, რომ ერთი და იგივე კოდი თავიდან არ ვწეროთ.


def greet(name):
  print("hello" , name)

greet("demetre")
greet("luka")



def number(num):
    if num % 2 == 0:
        print("even")
    else:
        print("Odd")

number(8)
number(5)