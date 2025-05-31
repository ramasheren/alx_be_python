task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound  = input("Is it time-bound? (yes/no): ").lower()
if time_bound == 'yes':
    sen = " that requires immediate attention today!"
else:
    sen = ". Consider completing it when you have free time."
    print(f"Note: '{task}' is a {priority} priority task{sen}")
