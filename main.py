

from modules.caregiver import Caregiver
from modules.schedule import CareSchedule
from modules.payroll import Payroll

def main():
    # Caregiver and availability insatnce




    #carescedule/html calendar 

    care_schedule = CareSchedule(caregivers, 2024, 11)

    html_calendar = care_schedule.formatmonth()
    with open("schedule_calendar.html", "w") as file:
        file.write(html_calendar)



    #simulated hours so we can return the payroll report and the calendar 





    #payroll and report
   
    payroll = Payroll(caregivers)
    payroll.save_to_file()

if __name__ == "__main__":
    main()
