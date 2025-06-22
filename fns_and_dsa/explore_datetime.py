from datetime import datetime, timedelta

def display_current_datetime():
    current_date = datetime.now()
    formatted = current_date.strftime("%Y-%m-%d %H:%M:%S")
    return formatted

def calculate_future_date(days):
    current_date = datetime.now()
    future_date = current_date + timedelta(days=days)
    formatted = future_date.strftime("%Y-%m-%d")
    return formatted

def main():
    current = display_current_datetime()
    print(f"Current date and time: {current}")

    try:
        days_input = int(input("Enter the number of days to add to the current date: "))
        future = calculate_future_date(days_input)
        print(f"Date after {days_input} day(s): {future}")
    except ValueError:
        print("Invalid input! Please enter an integer.")

if __name__ == "__main__":
    main()

