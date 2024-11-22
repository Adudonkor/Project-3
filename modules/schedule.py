#insert Schedule Class
import calendar
from collections import defaultdict

class CareSchedule(calendar.HTMLCalendar):
    def __init__(self, caregivers, year, month):
        super().__init__()
        self.caregivers = caregivers
        self.year = year
        self.month = month
        self.schedule = self.generate_schedule()

    def generate_schedule(self):
        """Generates a weekly schedule from caregivers' availability."""
        schedule = {day: {"AM": None, "PM": None} for day in ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]}

        for caregiver in self.caregivers:
            for day, shifts in caregiver["availability"].items():
                for shift in shifts:
                    if schedule[day][shift] is None:
                        schedule[day][shift] = caregiver["name"]

        return schedule

    def formatday(self, day, weekday):
        """Formats a single day's cell in the HTML calendar."""
        if day == 0:
            return '<td class="noday">&nbsp;</td>'  # Empty cell
        else:
            day_name = calendar.day_name[weekday]

            am_shift = self.schedule.get(day_name, {}).get("AM", "No Caregiver")
            pm_shift = self.schedule.get(day_name, {}).get("PM", "No Caregiver")

            return f'<td><strong>{day}</strong><br>AM: {am_shift}<br>PM: {pm_shift}</td>'

    def formatweek(self, theweek):
        """Formats a week's worth of data (7 days)."""
        return '<tr>' + ''.join(self.formatday(d, wd) for (d, wd) in theweek) + '</tr>'

    def formatmonth(self):
        """Creates the complete month table in HTML format."""
        html = []
        html.append('<table border="1" cellpadding="5" cellspacing="0" class="month">')
        html.append(f'<tr><th colspan="7">{calendar.month_name[self.month]} {self.year}</th></tr>')
        html.append('<tr>' + ''.join(f'<th>{day}</th>' for day in calendar.day_abbr) + '</tr>')
        for week in self.monthdays2calendar(self.year, self.month):
            html.append(self.formatweek(week))
        html.append('</table>')
        return ''.join(html)

caregivers = [
    {
        "name": "Alice",
        "availability": {
            "Monday": ["AM", "PM"],
            "Wednesday": ["AM"],
            "Friday": ["PM"]
        }
    },
    {
        "name": "Bob",
        "availability": {
            "Tuesday": ["AM"],
            "Wednesday": ["PM"],
            "Thursday": ["AM", "PM"]
        }
    },
    {
        "name": "Carol",
        "availability": {
            "Monday": ["PM"],
            "Thursday": ["AM"],
            "Saturday": ["AM", "PM"]
        }
    }
]

care_schedule = CareSchedule(caregivers, 2024, 11)

html_calendar = care_schedule.formatmonth()
with open("schedule_calendar.html", "w") as file:
    file.write(html_calendar)
