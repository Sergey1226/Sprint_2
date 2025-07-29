class EmployeeSalary:
    hourly_payment = 400
    
    def __init__(self, name, hours, rest_days, email):
        self.name = name
        self.hours = hours
        self.rest_days = rest_days
        self.email = email
    
    @classmethod
    def get_hours(cls, name, hours=None, rest_days=0, email=None):
        if hours is None:
            hours = (7 - rest_days) * 8
        return cls(name, hours, rest_days, email)
    
    @classmethod
    def get_email(cls, name, hours=None, rest_days=0, email=None):
        if email is None:
            email = f"{name}@email.com"
        return cls(name, hours, rest_days, email)
    
    @classmethod
    def set_hourly_payment(cls, new_hourly_payment):
        cls.hourly_payment = new_hourly_payment
        
    def salary(self):
        return self.hours * self.hourly_payment
        
# В задании не указано что либо выводить. Не знаю или нужно было это делать.
employee1 = EmployeeSalary.get_hours("Ivan", rest_days=2)
employee1 = EmployeeSalary.get_email(employee1.name, hours=employee1.hours,
                                     rest_days=employee1.rest_days)
print(f"Name: {employee1.name}")
print(f"Hours: {employee1.hours}")
print(f"Email: {employee1.email}")
print(f"Salary: {employee1.salary()}")

EmployeeSalary.set_hourly_payment(500)
