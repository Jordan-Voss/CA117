class Employee:
    next_employee_number = 0

    def __init__(self, name, hourly_rate=9.25, hours_worked=0):
        self.name = name
        self.hourly_rate = hourly_rate
        self.hours_worked = hours_worked

        self.employee_number = Employee.next_employee_number
        Employee.next_employee_number += 1

    def __str__(self):
        return "Name: {}\nID: {}\nHours: {:.2f}\nRate: {:.2f}\nWages: {:.2f}".format(
            self.name, self.employee_number, self.hours_worked, self.hourly_rate, self.get_wages())

    def get_wages(self):
        return self.hourly_rate * self.hours_worked

    def add_hours(self, h):
    	self.hours_worked += h