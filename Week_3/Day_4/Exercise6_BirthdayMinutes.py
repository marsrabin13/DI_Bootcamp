import datetime

birthday_str = "21/03/1991"
birthday = datetime.datetime.strptime(birthday_str, "%d/%m/%Y")
print(f"Parsed birthday: {birthday}")

# strptime vs strftime
# strptime = Parsed time (string to datetime)

# strftime = string format time (datetime to string)

# Current date and time
now = datetime.datetime.now()
print(f"Now: {now}")
print(f"Hour: {now.hour}, Minute: {now.minute}")


# Difference between two dates -> timedelta
diff = now - birthday
print(f"Time since birthday: {diff}")
print(f"Days: {diff.days}")
print(f"Total seconds: {diff.total_seconds()}")