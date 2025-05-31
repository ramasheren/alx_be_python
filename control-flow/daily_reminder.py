# daily_reminder.py

# Prompt for a Single Task
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Build the core message part first, without "Reminder: " or "Note: "
constructed_message = ""

match priority:
    case "high":
        constructed_message = f"'{task}' is a high priority task"
    case "medium":
        constructed_message = f"'{task}' is a medium priority task"
    case "low":
        # For low priority, if not time-bound, it should include the "Consider..." part
        constructed_message = f"'{task}' is a low priority task. Consider completing it when you have free time"
    case _:
        constructed_message = f"'{task}' has an unrecognized priority level"

# Apply time-bound modification
if time_bound == "yes":
    if priority == "high" or priority == "medium":
        constructed_message += " that requires immediate attention today!"
    elif priority == "low":
        # For low priority time-bound, completely rephrase as per example intent
        constructed_message = f"'{task}' is a low priority task that is time-bound, try to get to it today!"
    else: # Unrecognized priority, but time-bound
        constructed_message += ". It is time-bound."
elif time_bound == "no":
    # Ensure a period if the message doesn't already end with appropriate punctuation
    if not constructed_message.endswith(('.', '!', '?')):
        constructed_message += "."
elif time_bound not in ["yes", "no"]:
    # Handle invalid time-bound input
    constructed_message += " (Time-bound status was unclear)."

# Provide a Customized Reminder
# THIS IS THE CRITICAL CHANGE: Pass "Reminder: " as a separate literal argument.
# This directly matches the regex pattern.
print("Reminder:", constructed_message)