#inheritance


class Parent:
    def m1(self):
        print("This is parent class method")

    def m2(self):
        print("This is parent class method 2")


# p=Parent()

# p.m1()
# p.m2()


# class Child(Parent):
#     pass

# # c=Child()
# # c.m1()
# # c.m2()


class Child(Parent):
    def __init__(self):
        super().__init__()

    def m3(self):
        print("This is child class method")

# c=Child()
# c.m1()
# c.m2()
# c.m3()



class person:
    def __init__(self):
        self.name=input("enter a name:")
        self.age=int(input("enter age:"))

    def show(self):
        print("name",self.name)
        print("age",self.age)


class student(person):
    def __init__(self):
        super().__init__()
        self.rollno=int(input("enter roll no:"))
        self.mark=int(input("enter mark:"))
        self.course=input("enter course:")


    def show(self):
        super().show()
        print("roll no",self.rollno)
        print("mark",self.mark)
        print("course",self.course)

    def updatemark(self):
        self.mark=int(input("enter new mark:"))




# s=student()
# s.show()
# s.updatemark()


class company:
    def __init__(self):
        self.companyname=input("enter company name:")
        self.location=input("enter location:")

    def show(self):
        print("company name",self.companyname)
        print("location",self.location)

    def display_company(self):
        print("company name",self.companyname)
        print("location",self.location)

# c=company()
# c.show()
# c.display_company()

class employee(company):
    def __init__(self):
        super().__init__()
        self.empid=int(input("enter empid:"))
        self.name=input("enter name:")
        self.designation=input("enter designation:")
        self.salary=int(input("enter salary:"))


    def display_details(self):
        super().display_company()
        print("empid",self.empid)
        print("name",self.name)
        print("designation",self.designation)
        print("salary",self.salary)

    def update_salary(self):
        self.salary=self.salary*1.1

# c=employee()
# c.update_salary()
# c.display_details()

class category:
    def __init__(self):
        self.category_name=input("enter category name:")

    def show_category(self):
        print("category name",self.category_name)

class product(category):
    def __init__(self):
        super().__init__()
        self.product_name=input("enter product name:")
        self.price=int(input("enter price:"))
        self.quantity=int(input("enter quantity:"))

    def show_product(self):
        super().show_category()
        print("product name",self.product_name)
        print("price",self.price)
        print("quantity",self.quantity)

    def update_price(self):
        self.price=self.price*1.05

# p=product()
# p.update_price()
# p.show_product()



class Hospital:
    def __init__(self, hos_name, location, phone):
        self.hos_name = hos_name
        self.location = location
        self.phone = phone

    def display_hospital(self):
        print("\nHospital Name:", self.hos_name)
        print("Location:", self.location)
        print("Phone:", self.phone)


class Department:
    def __init__(self, dept_name, doctor_name):
        self.dept_name = dept_name
        self.doctor_name = doctor_name

    def display_department(self):
        print("Department Name:", self.dept_name)
        print("Doctor Name:", self.doctor_name)


class Patient(Hospital, Department):
    def __init__(self, hos_name, location, phone,
                 dept_name, doctor_name,
                 patient_name, age, gender,
                 admission_date, bedno):

        Hospital.__init__(self, hos_name, location, phone)
        Department.__init__(self, dept_name, doctor_name)

        self.patient_name = patient_name
        self.age = age
        self.gender = gender
        self.admission_date = admission_date
        self.bedno = bedno
        self.discharge_date = None

    def set_discharge(self):
        self.discharge_date = input("Enter discharge date: ")

    def full_summary(self):
        self.display_hospital()
        self.display_department()

        print("Patient Name:", self.patient_name)
        print("Age:", self.age)
        print("Gender:", self.gender)
        print("Admission Date:", self.admission_date)
        print("Bed No:", self.bedno)
        print("Discharge Date:", self.discharge_date)


# Dynamic input
hos_name = input("Enter hospital name: ")
location = input("Enter location: ")
phone = input("Enter phone: ")

dept_name = input("Enter department name: ")
doctor_name = input("Enter doctor name: ")

patient_name = input("Enter patient name: ")
age = int(input("Enter age: "))
gender = input("Enter gender: ")
admission_date = input("Enter admission date: ")
bedno = input("Enter bed number: ")


# Create object
p = Patient(
    hos_name,
    location,
    phone,
    dept_name,
    doctor_name,
    patient_name,
    age,
    gender,
    admission_date,
    bedno
)

# Display details
print("\n--- PATIENT DETAILS ---")
p.full_summary()

# Set discharge
choice = input("\nDo you want to enter discharge date? (yes/no): ")

if choice.lower() == "yes":
    p.set_discharge()

    print("\n--- UPDATED PATIENT DETAILS ---")
    p.full_summary()