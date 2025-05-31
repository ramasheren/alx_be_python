# daily_reminder.py

# Prompt for a Single Task
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower() # Convert to lowercase for easier matching
time_bound = input("Is it time-bound? (yes/no): ").lower() # Convert to lowercase

# Initialize the base reminder message
final_reminder = "" # Use a new variable for the final complete string

# Process the Task Based on Priority using Match Case
match priority:
    case "high":
        final_reminder = f"Reminder: '{task}' is a high priority task"
    case "medium":
        final_reminder = f"Reminder: '{task}' is a medium priority task"
    case "low":
        final_reminder = f"Note: '{task}' is a low priority task. Consider completing it when you have free time."
    case _: # Default case for invalid priority input
        final_reminder = f"Unrecognized priority: '{task}' has an unrecognized priority level."

# Use an if statement to modify the reminder if the task is time-bound
# Ensure this logic correctly appends to `final_reminder` without duplicating "Reminder: " or "Note: "
if time_bound == "yes":
    if priority == "high" or priority == "medium":
        final_reminder += " that requires immediate attention today!"
    elif priority == "low":
        # For low priority but time-bound, it's still good to note it
        # The 'Note:' is already included in the initial assignment for low priority
        if not final_reminder.endswith("."): # Avoid double periods if already there
             final_reminder += "." # Just to ensure proper sentence end
        final_reminder += " It is time-bound, try to get to it today."
elif time_bound == "no":
    if priority == "high" or priority == "medium":
        final_reminder += "." # End the sentence if not time-bound
    # For low priority, the "Consider completing it when you have free time." already ends with a period.
elif time_bound not in ["yes", "no"]:
    # Handle invalid time-bound input by appending to the current message
    final_reminder += " (Time-bound status was unclear)."

# Provide a Customized Reminder
# Print the single string that now contains the full reminder, including "Reminder: " or "Note: "
print(final_reminder)