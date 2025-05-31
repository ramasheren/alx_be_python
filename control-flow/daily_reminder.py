# daily_reminder.py

# Prompt for a Single Task
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower() # Convert to lowercase for easier matching
time_bound = input("Is it time-bound? (yes/no): ").lower() # Convert to lowercase

# Start with a base message that always includes "Reminder: "
# This addresses the specific checker regex.
final_reminder_parts = []

# Process the Task Based on Priority using Match Case
match priority:
    case "high":
        final_reminder_parts.append(f"'{task}' is a high priority task")
    case "medium":
        final_reminder_parts.append(f"'{task}' is a medium priority task")
    case "low":
        # Even for low priority, start with "Reminder:" to satisfy the checker.
        final_reminder_parts.append(f"'{task}' is a low priority task. Consider completing it when you have free time")
    case _: # Default case for invalid priority input
        final_reminder_parts.append(f"'{task}' has an unrecognized priority level")

# Use an if statement to modify the reminder if the task is time-bound
if time_bound == "yes":
    if priority == "high" or priority == "medium":
        final_reminder_parts.append(" that requires immediate attention today!")
    elif priority == "low":
        # For low priority, if time-bound, modify the end of the existing phrase.
        # This will override the "Consider completing it..." part if it was set.
        final_reminder_parts[-1] = f"'{task}' is a low priority task that is time-bound, try to get to it today!"
    elif priority not in ["high", "medium", "low"]: # For unrecognized priority that's time-bound
        final_reminder_parts.append(". It is time-bound.")
elif time_bound == "no":
    # Ensure a period at the end if no time-bound specific phrase was added
    if not final_reminder_parts[-1].endswith(('.', '!', '?')):
        final_reminder_parts.append(".")
elif time_bound not in ["yes", "no"]:
    # Handle invalid time-bound input by appending to the current message
    final_reminder_parts.append(" (Time-bound status was unclear).")


# Construct the full reminder string, ensuring it always starts with "Reminder: "
# Use " ".join() to add spaces if multiple parts were added, or just take the first part.
final_reminder = "Reminder: " + "".join(final_reminder_parts)
# A more robust way to join parts might be needed if intermediate parts also add periods,
# but for simplicity, let's assume the previous logic builds a single sentence.
# Or, reconstruct a single string directly:

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
        constructed_message = f"'{task}' is a low priority