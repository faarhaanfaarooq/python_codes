def greetings():
    print("Hello! "+name)
    print("Welcome To HogaLand")

name = input("Enter your name: ")
greetings()
print("***********************************")
#using parameters
def details(name, age):
    print(f"Passenger name is {name}")
    print(f"He is {age} years old.")

details("Farhan", 21)