

import random 

# CAREGIVER class

class Caregiver:
    def __init__(self, name, phone, email, pay_rate=20):

#Insert Caregiver Class
class Caregiver:
    def __init__(self, name, phone, email, pay_rate):

        self.name = name
        self.phone = phone
        self.email = email
        self.pay_rate = pay_rate
        self.hours_worked = 0

        self.availability = {}  # Format: {"7:00 AM - 1:00 PM": "available"}

        self.availability = {}


    def update_availability(self, shift, status):
        valid_statuses = {"preferred", "available", "unavailable"}
        status = status.strip()  # Remove leading/trailing spaces

        if status in valid_statuses:
            self.availability[shift] = status

        if status not in valid_statuses:
        self.availability = {}  # Format: {"7:00 AM - 1:00 PM": "available"}

    def update_availability(self, shift, status):
        self.availability[shift] = status

    def add_hours(self, hours):
        self.hours_worked += hours

    def get_contact_info(self):
        return f"{self.name}: {self.phone}, {self.email}"

    def calculate_pay(self):
        return self.hours_worked * self.pay_rate

class Shift:
    def __init__(self, shift_time):
        self.shift_time = shift_time
        self.caregiver = None

    def assign_caregiver(self, caregiver):
        self.caregiver = caregiver
        caregiver.add_hours(6)  # Each shift is 6 hours

    def clear_assignment(self):
        self.caregiver = None


class Schedule:
    def __init__(self):
        self.shifts = {}  # Format: {"YYYY-MM-DD": [Shift("7:00 AM - 1:00 PM"), ...]}
        self.caregivers = []

    def add_caregiver(self, caregiver):
        self.caregivers.append(caregiver)


    def assign_shifts(self):
        previous_day_assigned = set()  # Keep track of assigned caregivers from the previous day

        for date, shift_list in sorted(self.shifts.items()):
            random.shuffle(self.caregivers)  # Randomize caregiver order each day
            assigned_caregivers = set()  # Track assignments for the current day

            for shift in shift_list:

                # Prioritize 'preferred' caregivers who haven't been assigned today or the previous day
                preferred_caregivers = [
                    c for c in self.caregivers
                    if c.availability.get(shift.shift_time) == "preferred" and 
                    c.name not in assigned_caregivers and
                    c.name not in previous_day_assigned
                ]
                available_caregivers = [
                    c for c in self.caregivers
                    if c.availability.get(shift.shift_time) == "available" and 
                    c.name not in assigned_caregivers and
                    c.name not in previous_day_assigned
                ]

                # Randomly select from preferred or available caregivers
                if preferred_caregivers:
                    caregiver = random.choice(preferred_caregivers)
                elif available_caregivers:
                    caregiver = random.choice(available_caregivers)
                else:
                    caregiver = None  # No caregiver available for this shift

                if caregiver:
                    shift.assign_caregiver(caregiver)
                    assigned_caregivers.add(caregiver.name)

            previous_day_assigned = assigned_caregivers  # Update for the next day's shifts

                for caregiver in self.caregivers:
                    if caregiver.availability.get(shift.shift_time) == "preferred":
                        shift.assign_caregiver(caregiver)
                        break
                else:  # If no 'preferred', assign an 'available' caregiver
                    for caregiver in self.caregivers:
                        if caregiver.availability.get(shift.shift_time) == "available":

    def generate_schedule(self):
        # Logic to assign caregivers based on availability and preferences
        for date, shift_list in self.shifts.items():
            for shift in shift_list:
                for caregiver in self.caregivers:
                    if caregiver.availability.get(shift.shift_time) == 'preferred':
                        shift.assign_caregiver(caregiver)
                        break
                else:
                    # Assign 'available' caregiver if no 'preferred' found
                    for caregiver in self.caregivers:
                        if caregiver.availability.get(shift.shift_time) == 'available':

                            shift.assign_caregiver(caregiver)
                            break

    def view_schedule(self):
        for date, shift_list in self.shifts.items():
            print(f"{date}:")
            for shift in shift_list:
                caregiver_name = shift.caregiver.name if shift.caregiver else "Unassigned"
                print(f"  {shift.shift_time}: {caregiver_name}")


    def convert_to_schedule_format(caregivers):
        formatted = []
        for caregiver in caregivers:
            formatted.append({
                "name": caregiver.name,
                "availability": caregiver.availability  # Ensure day-based data transformation
            })
        return formatted

# Example usage
schedule = Schedule()

# Caregivers and pay rates
caregivers = [
    Caregiver("Alice", "123-456-7890", "Alice@example.com", 20),
    Caregiver("Bob", "634-326-2130", "Bob@example.com", 20),
    Caregiver("Carol", "764-254-4567", "Carol@example.com"),
    Caregiver("Dom", "856-346-1351", "Dom@example.com", 20),
    Caregiver("Eve", "756-235-6131", "Eve@example.com"),
    Caregiver("Finn", "555-777-6814", "Finn@example.com"),
    Caregiver("Gale", "111-222-3333", "Gale@example.com"),
    Caregiver("Holly", "444-555-6666", "Holly@example.com", 20),
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
   


# Example usage:
schedule = Schedule()
caregiver1 = Caregiver("Alice", "123-456-7890", "alice@example.com", 20)
caregiver1.update_availability("7:00 AM - 1:00 PM", "preferred")

schedule.add_caregiver(caregiver1)
schedule.shifts["2024-11-17"] = [Shift("7:00 AM - 1:00 PM"), Shift("1:00 PM - 7:00 PM")]

schedule.generate_schedule()
schedule.view_schedule()

