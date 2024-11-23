# CAREGIVER/CAREGIVER AVAILABILITY SECTION
import random 

class Caregiver:
    def __init__(self, name, phone, email, pay_rate=20):
        self.name = name
        self.phone = phone
        self.email = email
        self.pay_rate = pay_rate
        self.hours_worked = 0
        self.availability = {}  # Format: {"7:00 AM - 1:00 PM": "available"}

    def update_availability(self, shift, status):
        valid_statuses = {"preferred", "available", "unavailable"}
        status = status.strip()  # Remove leading/trailing spaces
        if status in valid_statuses:
            self.availability[shift] = status

    def add_hours(self, hours):
        self.hours_worked += hours

    def get_contact_info(self):
        return f"{self.name}: {self.phone}, {self.email}"

class Shift:
    def __init__(self, shift_time):
        self.shift_time = shift_time
        self.caregiver = None

    def assign_caregiver(self, caregiver):
        if self.caregiver is None: 
            self.caregiver = caregiver
            caregiver.add_hours(6)  

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

