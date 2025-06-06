
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

constructed_message = ""

match priority:
    case "high":
        constructed_message = f"'{task}' is a high priority task"
    case "medium":
        constructed_message = f"'{task}' is a medium priority task"
    case "low":
        constructed_message = f"'{task}' is a low priority task. Consider completing it when you have free time"
    case _:
        constructed_message = f"'{task}' has an unrecognized priority level"

if time_bound == "yes":
    if priority == "high" or priority == "medium":
        constructed_message += " that requires immediate attention today!"
    elif priority == "low":
        constructed_message = f"'{task}' is a low priority task that is time-bound, try to get to it today!"
    else: 
        constructed_message += ". It is time-bound."
elif time_bound == "no":
    if not constructed_message.endswith(('.', '!', '?')):
        constructed_message += "."
elif time_bound not in ["yes", "no"]:
    constructed_message += " (Time-bound status was unclear)."

print("Reminder:", constructed_message)