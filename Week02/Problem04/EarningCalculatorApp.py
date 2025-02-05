from EarningCalculator import EarningCalculator

basic_pay_rate = float(input("Enter your basic pay rate: "))
number_of_regular_hours = int(input("Enter your number of regular hours: "))
number_of_overtime_hours = int(input("Enter your number of overtime hours: "))

job01= EarningCalculator(basic_pay_rate, number_of_regular_hours, number_of_overtime_hours)

# job01= EarningCalculator(13.50, 20, 8)
# job02 = EarningCalculator(14.44, 18, 4)
# job03 = EarningCalculator(16.78, 19, 7)

print(job01.calculate_payment())
# print(job02.calculate_payment())
# print(job03.calculate_payment())