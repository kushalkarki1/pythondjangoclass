# child class name "IS A" parent class name

# class Bird:
#     def __init__(self, name, color):
#         self.name = name
#         self.color = color

#     def fly(self):
#         print(f"{self.name} is flying.")

# class Pigeon(Bird):
#     def __init__(self, name, color):
#         # Bird.__init__(self, name)
#         super().__init__(name, color)

#     def fly(self):
#         super().fly()
#         print(f"{self.name} of {self.color} color is flying above.")

# class Ostrich(Bird):
#     def __init__(self, name, color):
#         super().__init__(name, color)

#     def fly(self):
#         print(f"{self.name} could not fly.")

# p = Pigeon("Saugat", "white")
# p.fly()
# # print("Pigeon", p.name, p.color)
# o = Ostrich("Chetan", "grey")
# # print("Ostrich", o.name, o.color)
# o.fly()

class User:
    def __init__(self, _id, username, password):
        self._id = _id
        self.username = username
        self.password = password

    def login(self, username, password): # student and teacher should be able to login
        return self.username == username and self.password == password

class Person(User):
    def __init__(self, _id, username, password, name, contact, address):
        super().__init__(_id, username, password)
        self.name = name
        self.contact = contact
        self.address = address

    def display_profile(self):
        """
            Doc String
            _id, username, name, contact, address
            if object is student -> also print course
            if object is teacher -> also print designation
        """
        print(f"Id: {self._id}")
        print(f"username: {self.username}")
        print(f"name: {self.name}")
        print(f"contact: {self.contact}")
        print(f"address: {self.address}")

class Student(Person):
    def __init__(self, _id, username, password, name, contact, address, course):
        super().__init__(_id, username, password, name, contact, address)
        self.course = course

    def display_profile(self):
        super().display_profile()
        print(f"course: {self.course}")

class Teacher(Person):
    def __init__(self, _id, username, password, name, contact, address, designation):
        super().__init__(_id, username, password, name, contact, address)
        self.designation = designation

    def display_profile(self):
        super().display_profile()
        print(f"designation: {self.designation}")


st = Student("001", "ram", "ram123", "Ram", "93232", "Ktm", "Python")
st1 = Student("002", "shyam", "shyam12", "Shyam", "88", "sa", "Python")
student_list = [st, st1]
te = Teacher("004", "hari", "hari123", "Hari", "873", "Bkt", "co-ordinator")
uname = input("Enter username: ")
pwd = input("Enter password: ")
for student in student_list:
    if student.login(uname, pwd):
        st.display_profile()
        break
    else:
        print("Invalid username or password")
# te.login(uname, pwd)
# te.display_profile()

class Company(User):
    def __init__(self, _id, username, password, name, contact):
        super().__init__(_id, username, password)
        self.company_name = name
        self.company_contact = contact