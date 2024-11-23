

from modules.caregiver import Caregiver, Schedule, Shift
from modules.schedule import CareSchedule
from modules.payroll import Payroll

def main():
    # Caregiver and availability insatnce
    caregivers = [
        Caregiver("Mark", "123-456-7890", "Mark@example.com", 20),
        Caregiver("Ben", "634-326-2130", "Ben@example.com", 20),
        Caregiver("Clara", "764-254-4567", "Clara@example.com", 20),
        Caregiver("Tawi", "856-346-1351", "Tawi@example.com", 20),
        Caregiver("Dumpi", "756-235-6131", "Dumpi@example.com", 20),
        Caregiver("Shay", "555-777-6814", "Shay@example.com", 20),
        Caregiver("Ron", "111-222-3333", "Ron@example.com", 20),
        Caregiver("Wendy", "444-555-6666", "Wendy@example.com", 20),
    ]

# Setting up caregivers' availability

    caregivers[0].update_availability("Monday AM", "preferred")
    caregivers[0].update_availability("Monday PM", "available")
    caregivers[0].update_availability("Wednesday AM", "available")

    caregivers[1].update_availability("Tuesday AM", "preferred")
    caregivers[1].update_availability("Thursday AM", "available")
    caregivers[1].update_availability("Thursday PM", "available")

    caregivers[2].update_availability("Wednesday PM", "preferred")
    caregivers[2].update_availability("Thursday PM", "preferred")
    caregivers[2].update_availability("Friday PM", "available")

    caregivers[3].update_availability("Wednesday AM", "available")
    caregivers[3].update_availability("Friday PM", "preferred")
    caregivers[3].update_availability("Saturday AM", "available")

    caregivers[4].update_availability("Tuesday AM", "available")
    caregivers[4].update_availability("Saturday PM", "preferred")
    caregivers[4].update_availability("Sunday AM", "available")

    caregivers[5].update_availability("Friday AM", "available")
    caregivers[5].update_availability("Friday PM", "available")
    caregivers[5].update_availability("Saturday PM", "available")

    caregivers[6].update_availability("Saturday AM", "preferred")
    caregivers[6].update_availability("Saturday PM", "preferred")
    caregivers[6].update_availability("Sunday PM", "available")

    caregivers[7].update_availability("Sunday AM", "available")
    caregivers[7].update_availability("Sunday PM", "preferred")
    caregivers[7].update_availability("Monday PM", "available")


# Add caregivers to the schedule
    schedule = Schedule()
    for caregiver in caregivers:
        schedule.add_caregiver(caregiver)

    # Add shifts to the availability schedule
    # Update shifts to match availability keys
    schedule.shifts["2024-11-21"] = [Shift("Thursday AM"), Shift("Thursday PM")]
    schedule.shifts["2024-11-22"] = [Shift("Friday AM"), Shift("Friday PM")]
    schedule.shifts["2024-11-23"] = [Shift("Saturday AM"), Shift("Saturday PM")]
    schedule.shifts["2024-11-24"] = [Shift("Sunday AM"), Shift("Sunday PM")]
    schedule.shifts["2024-11-25"] = [Shift("Monday AM"), Shift("Monday PM")]


    for date, shift_list in schedule.shifts.items():
       for shift in shift_list:
           for caregiver in caregivers:
               if caregiver.availability.get(shift.shift_time) in {"preferred", "available"}:
                   shift.assign_caregiver(caregiver)
                   break

    # Generate and view the schedule
    schedule.view_schedule()

    #carescedule/html calendar 

    care_schedule = CareSchedule(caregivers, 2024, 11)

    html_calendar = care_schedule.formatmonth()
    with open("schedule_calendar.html", "w") as file:
        file.write(html_calendar)


    #payroll and report
   
    payroll = Payroll(caregivers)
    payroll.save_to_file()

if __name__ == "__main__":
    main()



<html>
<head>
<style>
table {border-collapse: collapse; width: 100%;}
th, td {border: 1px solid black; padding: 10px; text-align: center;}
.noday {background-color: #f0f0f0;}
</style>
</head>
<body>
<table>
    <tr>
        <th colspan="7">November 2024</th>
    </tr>
    <tr>
        <th>Mon</th>
        <th>Tue</th>
        <th>Wed</th>
        <th>Thu</th>
        <th>Fri</th>
        <th>Sat</th>
        <th>Sun</th>
    </tr>
    <tr>
        <td class="noday">&nbsp;</td>
        <td class="noday">&nbsp;</td>
        <td><strong>1</strong><br>AM: Alice<br>PM: No Caregiver</td>
        <td><strong>2</strong><br>AM: No Caregiver<br>PM: No Caregiver</td>
        <td><strong>3</strong><br>AM: No Caregiver<br>PM: Carol</td>
        <td><strong>4</strong><br>AM: Carol<br>PM: Carol</td>
        <td><strong>5</strong><br>AM: No Caregiver<br>PM: No Caregiver</td>
    </tr>
    <tr>
        <td><strong>6</strong><br>AM: Alice<br>PM: Carol</td>
        <td><strong>7</strong><br>AM: Bob<br>PM: Bob</td>
        <td><strong>8</strong><br>AM: No Caregiver<br>PM: Alice</td>
        <td><strong>9</strong><br>AM: Bob<br>PM: Carol</td>
        <td><strong>10</strong><br>AM: Alice<br>PM: Bob</td>
        <td><strong>11</strong><br>AM: Carol<br>PM: Carol</td>
        <td><strong>12</strong><br>AM: No Caregiver<br>PM: No Caregiver</td>
    </tr>
</table>
</body>
</html>

