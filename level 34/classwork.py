#List არის მონაცემების სია, სადაც რამდენიმე მნიშვნელობას ერთად ვინახავთ. სიაში თითოეულ ელემენტს აქვს თავისი Index , 
# რომელიც Python-ში 0-დან იწყება. Indexing კი ნიშნავს სიიდან ელემენტის ამოღებას მისი ინდექსის გამოყენებით.


fruits = ["apple", "banana", "orange"]

print(fruits[0])  # apple
print(fruits[1])  # banana
print(fruits[2])  # orange



fruits = ["Apple", "Banana", "Peach", "Watermelon", "Melon", "Kiwi", "Strawberry"]

# First element
print(fruits[0])

# Last element (using a negative index)
print(fruits[-1])

# Slice the middle part
print(fruits[2:5])

# Print every second fruit
print(fruits[::2])