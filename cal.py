import tkinter as tk
from tkinter import ttk
from datetime import datetime
import calendar

class LiveCalendar(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Live Calendar")
        self.geometry("300x400")
        self.configure(bg="#f3f4f6")

        # Header for date and time
        self.date_time_label = tk.Label(self, text="", font=("Helvetica", 16), bg="#f3f4f6")
        self.date_time_label.pack(pady=10)

        # Calendar for current month
        self.calendar_frame = tk.Frame(self, bg="white")
        self.calendar_frame.pack(pady=20)
        
        self.update_calendar()
        self.update_time()

    def update_calendar(self):
        # Clear the previous calendar
        for widget in self.calendar_frame.winfo_children():
            widget.destroy()

        now = datetime.now()
        year, month = now.year, now.month
        month_days = calendar.monthcalendar(year, month)
        month_name = calendar.month_name[month]

        # Display month and year
        month_label = tk.Label(self.calendar_frame, text=f"{month_name} {year}", font=("Helvetica", 14), bg="white")
        month_label.grid(row=0, column=0, columnspan=7, pady=10)

        # Display day names
        days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
        for col, day in enumerate(days):
            day_label = tk.Label(self.calendar_frame, text=day, font=("Helvetica", 10), bg="white")
            day_label.grid(row=1, column=col, padx=5, pady=5)

        # Display days
        for row, week in enumerate(month_days, start=2):
            for col, day in enumerate(week):
                day_text = str(day) if day != 0 else ""
                day_label = tk.Label(self.calendar_frame, text=day_text, font=("Helvetica", 10), bg="white")
                day_label.grid(row=row, column=col, padx=5, pady=5)

    def update_time(self):
        # Update the date and time display
        now = datetime.now()
        self.date_time_label.config(text=now.strftime("%A, %d %B %Y\n%H:%M:%S"))

        # Update every second
        self.date_time_label.after(1000, self.update_time)

# Run the live calendar
app = LiveCalendar()
app.mainloop()
