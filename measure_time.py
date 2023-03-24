import subprocess
from datetime import datetime, timedelta
import matplotlib.pyplot as plt

import subprocess
from datetime import datetime, timedelta

def get_user_usage(username, start_date, end_date):
    output = subprocess.check_output(f"last -R {username} -s {start_date} -t {end_date}", shell=True)
    lines = output.decode().strip().split('\n')

    work_days = {}
    for i, line in enumerate(lines):
        fields = line.split()
        if username in line and 'still' not in line:
            login_str = f"{fields[3]} {fields[4]}"
            login_day = datetime.strptime(login_str + f" {end_date.year}", "%b %d %Y")
            duration_str = fields[8].strip('()')
            hours, minutes = map(int, duration_str.split(':'))
            duration = timedelta(hours=hours, minutes=minutes)
            if login_day in work_days:
                work_days[login_day.strftime("%d-%m-%Y")] += duration
            else:
                work_days[login_day.strftime("%d-%m-%Y")] = duration
    return work_days


def plot_user_usage(data):
    durations = []
    dates = []
    for date, duration in data.items():
        dates.append(date[0:5])
        durations.append(duration)
    total_duration = sum(durations, timedelta())
    num_days = len(durations)
    average_duration = total_duration / num_days

    fig, axs = plt.subplots(figsize=(4, 3))

    # Bar plot of daily durations
    axs.bar(dates, [d.total_seconds() / 3600 for d in data.values()])
    axs.set_title('Daily Time Spent')
    axs.set_xlabel('Date')
    axs.set_ylabel('Hours')
    axs.axhline(y=average_duration.total_seconds() / 3600, \
                linestyle='--', color='r', label='Average')
    # Display total duration
    total_hours = total_duration.total_seconds() / 3600
    average_hours = total_hours / num_days
    total_str = f"{int(total_hours):02d}:{int(total_hours % 1 * 60):02d}"
    axs.text(0.01, -0.4, \
             f'Total duration: {total_str}\nNumber of days: {num_days}\nAverage: {round(average_hours, 2)}'\
                , transform=axs.transAxes)

    plt.show()

if __name__ == '__main__':
    username = input("Enter username: ")
    date_range = input("Enter date range (last week/last month): ")
    today = datetime.today()
    if date_range == "last week":
        start_date = today - timedelta(days=7)
    elif date_range == "last month":
        start_date = today - timedelta(days=30)
    else:
        start_date_str = input("Enter start date (YYYY-MM-DD): ")
        end_date_str = input("Enter end date (YYYY-MM-DD): ")
        start_date = datetime.strptime(start_date_str, "%Y-%m-%d")
        end_date = datetime.strptime(end_date_str, "%Y-%m-%d")
    end_date = today + timedelta(days=1)
    user_usage_data = get_user_usage(username, start_date, end_date)
    plot_user_usage(user_usage_data)
