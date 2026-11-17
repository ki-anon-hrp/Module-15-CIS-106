# Kirill M15P1 11/16/2026

# Define a class Employee
class Employee:

# Define first method of defindning email, rate, and pay
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@comapny.com'

# Define second method of finding bonus by using rate and pay 
    def bonus(self, rate):
        b = float(rate) * float(self.pay)
        return b

# Define third method of finding final pay by additing bonus rate and intinial pay
    def compute_bonus(self, rate):
        a = float(self.pay) + self.bonus(rate)
        return a

# Define a class Manager as a inheritance for Employee class
class Manager(Employee):

# Define first method, for finding manager bonus with 40%
    def long_term(self):
        c = 0.40 * float(self.pay)
        return c

# Define second method, for finding compute pay with bonus
    def compute_long_term(self):
        d = float(self.pay) + self.long_term() 
        return d

# Define what data we use in Employee and Manager classes
empl1 = Employee('Frank', 'Alvino', 60000.00)
empl2 = Employee('Tom', 'White', 45000.00)

mng1 = Manager('Bob', 'Bobovich', 100000)
mng2 = Manager('Will', 'Ramos', 200000)

print()

# Printing first employee
print(empl1.email)
print(empl1.first)
print(empl1.last)
print(empl1.pay)

# Asking for entering bonus rate
rate = float(input("Enter bonus rate: "))

# Using bonus method for showing rate
print("Bonus:", empl1.bonus(rate))

# Using compute_bonus method for showing final pay
print("Final pay:", empl1.compute_bonus(rate))

print()

# Printing second employee
print(empl2.email)
print(empl2.first)
print(empl2.last)
print(empl2.pay)

rate = float(input("Enter bonus rate: "))

# Using bonus method for showing rate
print("Bonus:", empl2.bonus(rate))

# Using compute_bonus method for showing final pay
print("Final pay:", empl2.compute_bonus(rate))

print()

# Printing first manager
print(mng1.email)
print(mng1.first)
print(mng1.last)
print(mng1.pay)
print("Manager bonus:", mng1.long_term())
print("Final pay:", mng1.compute_long_term())

print()

# Printing second manager
print(mng2.email)
print(mng2.first)
print(mng2.last)
print(mng2.pay)
print(f"Manager bonus:", mng2.long_term())
print("Final pay:", mng2.compute_long_term())