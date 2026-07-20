import datetime


# Current date and time
now = datetime.datetime.now()
print(f"Now: {now}")
print(f"Hour: {now.hour}, Minute: {now.minute}")

# # Create a specific date
new_year = datetime.datetime(2027, 1, 1, 0, 0, 0)
print(f"New Year: {new_year}")

# Difference between two dates -> timedelta
diff = new_year - now
print(f"Time until 2027: {diff}")
print(f"Days: {diff.days}")
print(f"Total seconds: {diff.total_seconds()}")