#Insert Payroll class
class Payroll:
    def __init__(self, caregivers):
        self.caregivers = caregivers

    def calculate_weekly_pay(self):
        #THis calculate the weekly  pay for the caregiver and returns a dictionary with their names as keys and pay details as values
        payroll_report = {}
        for caregiver in self.caregivers:
            gross_pay = caregiver.hours_worked * caregiver.pay_rate
            payroll_report[caregiver.name] = {
                "hours_worked": caregiver.hours_worked,
                "pay_rate": caregiver.pay_rate,
                "gross_pay": gross_pay
            }
        return payroll_report

    def calculate_monthly_totals(self):
        total_hours = sum(c.hours_worked for c in self.caregivers)
        total_gross_pay = sum(c.hours_worked * c.pay_rate for c in self.caregivers)
        return {"total_hours": total_hours, "total_gross_pay": total_gross_pay}

    def print_payroll(self):
      #this prints the payroll report
        payroll_report = self.calculate_weekly_pay()
        monthly_totals = self.calculate_monthly_totals()

        print("Weekly Payroll Report:")
        for caregiver_name, details in payroll_report.items():
            print(f"{caregiver_name}:")
            print(f"  Hours Worked: {details['hours_worked']} hrs")
            print(f"  Pay Rate: ${details['pay_rate']}/hr")
            print(f"  Gross Pay: ${details['gross_pay']:.2f}")

        print("\nMonthly Totals:")
        print(f"  Total Hours Worked: {monthly_totals['total_hours']} hrs")
        print(f"  Total Gross Pay: ${monthly_totals['total_gross_pay']:.2f}")
