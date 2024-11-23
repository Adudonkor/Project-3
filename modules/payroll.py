#Insert Payroll class
class Payroll:
    def __init__(self, caregivers):
        #this initializes the system using caregiver objects
        self.caregivers = caregivers

        #payroll report code and pay calculation

    def generate_report(self):
       
        report = "Payroll Report\n"
        report += "==============\n\n"

        total_hours = 0
        total_gross_pay = 0

        for caregiver in self.caregivers:
            hours_worked = caregiver.hours_worked
            pay_rate = caregiver.pay_rate
            gross_pay = hours_worked * pay_rate

            report += f"Caregiver: {caregiver.name}\n"
            report += f"  Hours Worked: {hours_worked} hrs\n"
            report += f"  Pay Rate: ${pay_rate}/hr\n"
            report += f"  Gross Pay: ${gross_pay:.2f}\n\n"

            total_hours += hours_worked
            total_gross_pay += gross_pay

        report += "Total Hours Worked: {} hrs\n".format(total_hours)
        report += "Total Gross Pay: ${:.2f}\n".format(total_gross_pay)

        return report

    def save_to_file(self, filename="payroll_report.txt"):
      #this saves the payroll report as a text file
        report = self.generate_report()
        with open(filename, "w") as file:
            file.write(report)
        print(f"Payroll report saved to {filename}")


