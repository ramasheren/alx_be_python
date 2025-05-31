task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower() # Convert to lowercase for easier matching
time_bound = input("Is it time-bound? (yes/no): ").lower() # Convert to lowercase

reminder_message = ""

match priority:
    case "high":
        reminder_message = f"'{task}' is a high priority task"
    case "medium":
        reminder_message = f"'{task}' is a medium priority task"
    case "low":
        reminder_message = f"Note: '{task}' is a low priority task. Consider completing it when you have free time."
    case _:
        reminder_message = f"'{task}' has an unrecognized priority level."

if time_bound == "yes" and (priority == "high" or priority == "medium"):
    reminder_message += " that requires immediate attention today!"
elif time_bound == "yes" and priority == "low":
    reminder_message += " but is time-bound, so try to get to it today."
elif time_bound == "no" and (priority == "high" or priority == "medium"):
    reminder_message += "." # Add a period if no time-bound message was added
elif time_bound not in ["yes", "no"]:
    reminder_message += " (Time-bound status was unclear)."
print("\nReminder:", reminder_message)