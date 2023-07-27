
# from datetime import datetime as dt

class Staff:
    population = 0
    staff_info = []
    positions = ["scientist", "technicians", "molecular-scientist", "accountant", "HR", "sales"
                 "tech", "facility-manager", "phlebotomy", "cleaner", "driver"]
    max_population = 100
    tax_rate = 0.05
    pension = 0.1
    attendance = 0
    clock_in = False
    resumption_time = [8.00, 8.30, 9.00]

    def __init__(self, name: str, profession: str, qualification: str, experience: int, work_days=25):
        self.name = name
        self.profession = profession
        self.qualification = qualification
        self.experience = experience
        self.__pathner_requirement = 5
        self.__work_days = work_days
        print("all these information are very important please ensure you input the correct information")
        Staff.staff_info.append(self)

    @classmethod
    def show_population(cls):
        for instance in Staff.staff_info:
            instance.Staff.population += 1
            return Staff.population

    @classmethod
    def staff_names(cls):
        for i in Staff.staff_info:
            print(i.self.name)

    def __repr__(self):
        return f"Staff('{self.name}, {self.profession}, {self.qualification}, {self.experience}')"

    @classmethod
    def employ_staff(cls):
        if Staff.population < Staff.max_population:
            return True
        return False

    @classmethod
    def days_present(cls):
        if Staff.clock_in:
            Staff.attendance += 1
        else:
            Staff.attendance += -1
            return Staff.attendance

    @classmethod
    def late_days(cls):
        lateness = 0
        if cls.clock_in not in Staff.resumption_time:
            lateness += 1
        else:
            lateness = 0
        return lateness


class Scientist(Staff):
    max_scientist = 4
    num_scientist = 0
    all_scientists = []
    basic_salary = 150000
    max_experience = 10
    min_experience = 2

    def __init__(self, name: str, profession: str, qualification: str, experience: int):
        super().__init__(name, profession, qualification, experience)
        Scientist.all_scientists.append(self)
        print(f"scientist{self.name} successfully added")

    @classmethod
    def employ_scientist(cls):
        if Scientist.num_scientist < Scientist.max_scientist:
            return True
        return False

    @staticmethod
    def job_description():
        job_description = ["sample analysis", "calibration", "sop  validation", "Q.C setup and validation"]
        return job_description

    def get_salary(self):
        salary = 0
        if self.experience == 1:
            salary = Scientist.basic_salary + (Scientist.basic_salary * 0.1)
        elif self.experience == 2:
            salary = Scientist.basic_salary + (Scientist.basic_salary * 0.2)
        elif self.experience == 3:
            salary = Scientist.basic_salary + (Scientist.basic_salary * 0.3)
        elif self.experience == 4:
            salary = Scientist.basic_salary + (Scientist.basic_salary * 0.4)
        elif self.experience == 5:
            salary = Scientist.basic_salary + (Scientist.basic_salary * 0.5)
        elif self.experience == 6:
            salary = Scientist.basic_salary + (Scientist.basic_salary * 0.6)
        elif self.experience == 7:
            salary = Scientist.basic_salary + (Scientist.basic_salary * 0.7)
        else:
            print("exceeded the maximum required years of experience")
        return salary

    def net_salary(self):
        net_salary = self.get_salary() - ((Staff.pension * self.get_salary()) + (Staff.tax_rate * self.get_salary()))
        return net_salary

    @classmethod
    def late_charges(cls):
        late_charges = 500 * (Staff.late_days())
        return late_charges

    def take_home_pay(self):
        take_home = self.net_salary() - self.late_charges()
        return take_home

    def take_leave(self):
        pass


class Technician:
    max_technician = 6
    num_of_technician = 0
    technicians = []
    basic_salary = 125000
    min_experience = 1
    max_experience = 8

    def __init__(self, name: str, experience: int, qualification="HND"):
        self.name = name
        self.experience = experience
        self.__qualification = qualification

    @classmethod
    def employ_technician(cls):
        if Technician.num_of_technician < Technician.max_technician:
            return True
        return False

    @classmethod
    def is_eligible(cls):
        if experience < Technician.min_experience and self.experience > Technician.max_technician:
            return True


