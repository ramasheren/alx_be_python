# daily_reminder.py

# Prompt for a Single Task
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower() # Convert to lowercase for easier matching
time_bound = input("Is it time-bound? (yes/no): ").lower() # Convert to lowercase

# Initialize the core message part (without "Reminder: " or "Note: ")
core_message = ""
prefix = "" # To store "Reminder: " or "Note: "

# Process the Task Based on Priority using Match Case
match priority:
    case "high":
        core_message = f"'{task}' is a high priority task"
        prefix = "Reminder: "
    case "medium":
        core_message = f"'{task}' is a medium priority task"
        prefix = "Reminder: "
    case "low":
        core_message = f"'{task}' is a low priority task. Consider completing it when you have free time."
        prefix = "Note: " # For low priority, the prefix is "Note: "
    case _: # Default case for invalid priority input
        core_message = f"'{task}' has an unrecognized priority level."
        prefix = "Reminder: " # Default prefix for unrecognized priority

# Use an if statement to modify the reminder if the task is time-bound
if time_bound == "yes":
    if priority == "high" or priority == "medium":
        core_message += " that requires immediate attention today!"
    elif priority == "low":
        # For low priority time-bound, it's already structured to end with a period.
        # We need to ensure the immediate attention part is added appropriately.
        # Let's add a more specific clause for low time-bound.
        core_message = f"'{task}' is a low priority task. It is time-bound, try to get to it today."
    # If priority is unrecognized and time_bound is 'yes', just append a general note.
    elif priority not in ["high", "medium", "low"]:
        core_message += " (It is time-bound)."
elif time_bound == "no":
    # For high/medium non-time-bound, ensure it ends with a period if it doesn't already
    if (priority == "high" or priority == "medium") and not core_message.endswith("."):
        core_message += "."
    # Low priority non-time-bound message already handles its ending.
elif time_bound not in ["yes", "no"]:
    # Handle invalid time-bound input by appending to the current message
    core_message += " (Time-bound status was unclear)."

# Provide a Customized Reminder
# Print the final message by concatenating the determined prefix and the core message
print(prefix + core_message)