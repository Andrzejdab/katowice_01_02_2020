class Employee:
    def __init__(self, f_name: str, l_name: str, rph: int):
        self.first_name = f_name
        self.last_name = l_name
        self.rate_per_hour = rph
        self._worked_normal_hours=0
        self._worked_overhours = 0

    def register_time(self, hours):
        if hours > 8:
            self._worked_normal_hours +=8
            self._worked_overhoursc+= hours -8
        else:
            self._worked_normal_hours += 8

    def pay_solary(self):
        to_pay = (self._worked_normal_hours *self.rate_per_hour +
        self._worked_overhours *2* self.rate_per_hour
        )
        self._worked_normal_hours = 0
        self._worked_overhours = 0
        return to_pay




class TestEmployee:
    def test_init(self):
        employee = Employee("Jan", "Nowak", 100.0)
        assert employee.first_name == "Jan"
        assert employee.last_name == "Nowak"
        assert employee.rate_per_hour == 100.0

    def test_register_time(self):
        employee = Employee("Jan", "Nowak", 100.0)
        employee.register_time()
        assert  employee._worked_normal_hours ==5

    def test_pay_solary_when_no_worked_hour(self):
        employee = Employee("Jan", "Nowak", 100.0)
        assert employee.pay_solary()==0

    def test_pay_solary_with_worked_hour(self):
        employee = Employee("Jan", "Nowak", 100.0)
        employee.register_time(5)
        assert employee.pay_solary()==5*100
        assert employee.pay_solary() == 0

    def test_pay_solary_over_hours(self):
        employee = Employee("Jan", "Nowak", 50.0)
        employee.register_time(10)
        assert employee.pay_solary()== 8*50 + 2*100
        assert employee.pay_solary() == 0

    def test_pay_solary_many_day(self):
        employee = Employee("Jan", "Nowak", 100.0)
        employee.register_time(10)
        employee.register_time(10)
        employee.register_time(10)
        assert employee.pay_solary()== 24*100 + 6*200