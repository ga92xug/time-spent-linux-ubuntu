# time-spent-linux-ubuntu
## User Usage Tracker

This simple script tracks the daily usage of a given user on a Linux system and displays the information in a bar chart. I found it nice to track my working hours like that.

## Prerequisites

This script requires Python 3 and the following libraries:
    subprocess
    datetime
    matplotlib

## How to Use

    Clone the repository or download the user_usage_tracker.py file.
    Open a terminal window and navigate to the directory where the file is located.
    Run the command python3 user_usage_tracker.py to start the script.
    Enter the username of the user you want to track.
    Enter the date range for which you want to track the usage. You can select either "last week" or "last month", or you can enter a specific start and end date.
    The script will generate a bar chart of the user's daily usage during the specified date range.

## Example Usage
Enter username: johndoe
Enter date range (last week/last month): last week

## Limitations

This script only works on Linux systems and requires root access to run the last command. It also assumes that the user logs out of the system when they are finished using it.