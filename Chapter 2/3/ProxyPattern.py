
class Employee(object):
    def __init__(self, name):
        self.__name = name
        self.__salary = 1000
        self.working = False
        self.training = False
        self.sick_leave = False

    @property
    def name(self):
        return self.__name

    @property
    def salary(self):
        return self.__salary

    @salary.setter
    def salary(self, increment):
        self.__salary *= increment

    def onWork(self):
        self.working = True
        print(f"I ({self.name}) was sent to WORK!")
        return self.working

    def onTraining(self):
        self.traninig = True
        print(f"I ({self.name}) was sent on a training!")
        return self.traninig

    def onSickLeave(self):
        self.sick_leave = True
        print(f"I ({self.name}) was sent on a sick leave!")
        return self.sick_leave

class Manager(object):
    def __init__(self, employee):
        self.managed_employee = employee
        print(f"The employee we manage is: {employee.name}")

    def send_employee_on(self, state):
        if state in ['work','sickleave','training']:
            print(f"I am sending the employee: {self.managed_employee.name} on {state}")
            if state == 'work':
                self.managed_employee.onWork()
            elif state == 'training':
                self.managed_employee.onTraining()
            else:
                self.managed_employee.onSickLeave()
        else:
            print(f"Cannot send the employee into the state: {state}")
    def give_raise(self, amount):
        print("Send mail to HR about the raise!")
        print(f"Approving the raise of the employee: {self.managed_employee.name}, with amount: {amount}")
        self.managed_employee.salary = amount


Daniel = Employee('Daniel')
print(f"My Current salary is: {Daniel.salary}")
Boss = Manager(Daniel)
Boss.send_employee_on('work')
Boss.send_employee_on('sickleave')
Boss.send_employee_on('training')
Boss.give_raise(1.10)
print(f"My salary after the raise is: {Daniel.salary}")







