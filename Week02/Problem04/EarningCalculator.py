class EarningCalculator:
    overtime_rate = 1.5

    def __init__(self, basic_pay_rate=0.0, number_of_regular_hours=0, number_of_overtime_hours=0):
        self.basic_pay_rate = basic_pay_rate
        self.number_of_regular_hours = number_of_regular_hours
        self.number_of_overtime_hours = number_of_overtime_hours

    def calculate_payment(self):
        """Calculate the total payment based on the basic pay rate, the numbers of regular hours and overtime hours."""
        total_payment = round(((self.basic_pay_rate * self.number_of_regular_hours) +
                         (EarningCalculator.overtime_rate * self.basic_pay_rate
                          * self.number_of_overtime_hours)), 2)
        return total_payment
