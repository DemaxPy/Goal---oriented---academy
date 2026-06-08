#ლოგიკური ოპერატორები არის ოპერატორები რომლებიც ჩვენ გვეუბნებიან მართალია (true) თუ ტყუილი(false)

#for loop ვხმარობთ მაშინ როცა წინასწარ ვიცით რამდენჯერ უნდა განმეორდეს მოქმედება ხოლო while loop 


name = "Demetre"

name = input("Enter your name: ")

while name != name:
    print("Name is incorrect")
    name = input("Enter your name again: ")

print("Name is correct")









my_list = [10, "Hello", 3.14, True, [1, 2, 3]]
del my_list[1]
my_list += ["Goa Best"]
print(my_list)





#def გამოიყენება ფუნქციის შესაქმნელად. ეს ფუნქცია საშუალებას გვაძლევს რომ ერთი და იგივე კოდი გამოვიყენოთ რამდენჯერაც ჩვენ გვინდა





def person_info(name, surname, age):
    print("My name is", name, ", my surname is", surname, "and I am", age, "years old.")

person_info("Demetre", "Beridze", 15)