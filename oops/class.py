class Person:
    def __init__(self, person_name, date_of_birth, height):
        self.name = person_name
        self.date_of_birth = date_of_birth
        self.height = height

    def get_name(self):
        return self.name

    def get_summary(self):
        return f"Name: {self.name} DOB: {self.date_of_birth} Height: {self.height}"

    def set_name(self, new_name):
        self.name = new_name


a_person = Person("Babul", "2000, Jun 03", "5 Feet 2 Inch")
print(a_person.get_summary())

a_person.set_name("Farhan Farooq")
print(a_person.get_summary())