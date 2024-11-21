class Caregiver:
    def __init__(self, name, phone, email, pay_rate):
        self.name = name
        self.phone = phone
        self.email = email
        self.pay_rate = pay_rate
        self.hours_worked = 0
        self.availability = {}  # Format: {"7:00 AM - 1:00 PM": "available"}

    def update_availability(self, shift, status):
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
        # Display the schedule
        for date, shift_list in self.shifts.items():
            print(f"{date}:")
            for shift in shift_list:
                caregiver_name = shift.caregiver.name if shift.caregiver else "Unassigned"
                print(f"  {shift.shift_time}: {caregiver_name}")
                


# Example usage:
schedule = Schedule()
caregiver1 = Caregiver("Alice", "123-456-7890", "alice@example.com", 20)
caregiver1.update_availability("7:00 AM - 1:00 PM", "preferred")

schedule.add_caregiver(caregiver1)
schedule.shifts["2024-11-17"] = [Shift("7:00 AM - 1:00 PM"), Shift("1:00 PM - 7:00 PM")]

schedule.generate_schedule()
schedule.view_schedule()