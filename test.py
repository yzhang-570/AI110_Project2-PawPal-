from datetime import datetime, time

# Get the current date and time as a datetime object
now = datetime.now()
print(f"Full datetime: {now}")

# Extract the time part using the .time() method
time_only = now.time()
print(f"Time only:     {time_only}")

time1 = datetime.combine(datetime.now(), time(hour=20, minute=30))
time2 = datetime.combine(datetime.now(), time(hour=20, minute=30))
print(time1)
print(time2)
print("time1 < time2: " + str(time1 == time2))