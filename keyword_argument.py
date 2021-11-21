def greet_user(first_name, last_name):
    print(f"Hello, {first_name} {last_name}")
    print("Welcome Abroad.")

print("start")
greet_user("Jhon","Lau")
print("************************************")
greet_user("Lau","Jhon")
print("************************************")
greet_user(last_name="Lau", first_name="Jhon")
print("end")