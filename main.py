

from modules.caregiver import Caregiver, Schedule, Shift
from modules.schedule import CareSchedule
from modules.payroll import Payroll

def main():
    # Caregiver and availability insatnce
    caregivers = [
        Caregiver("Mark", "123-456-7890", "Mark@example.com", 20),
        Caregiver("Ben", "634-326-2130", "Ben@example.com", 20),
        Caregiver("Clara", "764-254-4567", "Clara@example.com"),
        Caregiver("Tawi", "856-346-1351", "Tawi@example.com", 20),
        Caregiver("Dumpi", "756-235-6131", "Dumpi@example.com"),
        Caregiver("Shay", "555-777-6814", "Shay@example.com"),
        Caregiver("Ron", "111-222-3333", "Ron@example.com"),
        Caregiver("Wendy", "444-555-6666", "Wendy@example.com", 20),
    ]

# Setting up caregivers' availability
    caregivers[0].update_availability("7:00 AM - 1:00 PM", "preferred")
    caregivers[0].update_availability("1:00 PM - 7:00 PM", "available")

    caregivers[1].update_availability("7:00 AM - 1:00 PM", "available")
    caregivers[1].update_availability("1:00 PM - 7:00 PM", "unavailable")

    caregivers[2].update_availability("7:00 AM - 1:00 PM", "unavailable")
    caregivers[2].update_availability("1:00 PM - 7:00 PM", "preferred")

    caregivers[3].update_availability("7:00 AM - 1:00 PM", "unavailable")
    caregivers[3].update_availability("1:00 PM - 7:00 PM", "available")

    caregivers[4].update_availability("7:00 AM - 1:00 PM", "available")
    caregivers[4].update_availability("1:00 PM - 7:00 PM", "unavailable")

    caregivers[5].update_availability("7:00 AM - 1:00 PM", "unavailable")
    caregivers[5].update_availability("1:00 PM - 7:00 PM", "available")

    caregivers[6].update_availability("7:00 AM - 1:00 PM", "preferred")
    caregivers[6].update_availability("1:00 PM - 7:00 PM", "unavailable")

    caregivers[7].update_availability("7:00 AM - 1:00 PM", "available")
    caregivers[7].update_availability("1:00 PM - 7:00 PM", "available")

# Add caregivers to the schedule
    schedule = Schedule()
    for caregiver in caregivers:
        schedule.add_caregiver(caregiver)

    # Add shifts to the availability schedule
    schedule.shifts["2024-11-21"] = [Shift("7:00 AM - 1:00 PM"), Shift("1:00 PM - 7:00 PM")]
    schedule.shifts["2024-11-22"] = [Shift("7:00 AM - 1:00 PM"), Shift("1:00 PM - 7:00 PM")]
    schedule.shifts["2024-11-23"] = [Shift("7:00 AM - 1:00 PM"), Shift("1:00 PM - 7:00 PM")]
    schedule.shifts["2024-11-24"] = [Shift("7:00 AM - 1:00 PM"), Shift("1:00 PM - 7:00 PM")]
    schedule.shifts["2024-11-25"] = [Shift("7:00 AM - 1:00 PM"), Shift("1:00 PM - 7:00 PM")]


    # Generate and view the schedule
    schedule.assign_shifts()
    schedule.view_schedule()



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
