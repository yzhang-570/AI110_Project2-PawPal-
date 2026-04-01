from pawpal_system import Owner, Task, Pet, Scheduler
from datetime import datetime, time

owner1 = Owner("Yuwen")
pet1 = Pet("Topaz", "cat")
pet2 = Pet("Unnamed kitten", "cat")
owner1.add_pet(pet1)
owner1.add_pet(pet2)

task1 = Task(title="Feed Topaz", duration=10, priority="high", frequency = "daily")
task2 = Task(title="Open the door for Topaz", duration=5, priority="high", frequency = "daily")
task3 = Task(title="Feed kitten", duration=5, priority="medium", frequency = "daily")
task4 = Task(title="Play with Topaz", duration=15, priority="low", frequency = "daily")

pet1.add_task(task1)
pet1.add_task(task2)
pet2.add_task(task3)
pet1.add_task(task4)

schedule1 = Scheduler(owner1)
print("Original schedule")
print(schedule1)

# --- Sort by duration ---
print("=== Sorted by duration (all tasks) ===")
schedule1.sort_tasks_by_duration()
print(schedule1)

# --- Filter: Topaz only ---
print("=== Filter: Topaz only ===")
schedule1.filter_tasks(completed=None, pet_name="Topaz")
print(schedule1)

# --- Filter: None, None resets to show all tasks ---
print("=== Filter: None, None (reset — all tasks) ===")
schedule1.filter_tasks(completed=None, pet_name=None)
print(schedule1)

# --- Filter: Unnamed kitten only ---
print("=== Filter: Unnamed kitten only ===")
schedule1.filter_tasks(completed=None, pet_name="Unnamed kitten")
print(schedule1)

# --- Mark some tasks complete, then filter by completed=True ---
task1.set_as_completed()
task3.set_as_completed()

print("=== Filter: completed=True (no pet filter) ===")
print(schedule1.filter_tasks(completed=True, pet_name=None))

# --- Filter: completed=False (no pet filter) ---
print("=== Filter: completed=False (no pet filter) ===")
print(schedule1.filter_tasks(completed=False, pet_name=None))

# --- Filter: Topaz + completed=True (only Topaz's completed tasks) ---
print("=== Filter: Topaz + completed=True ===")
print(schedule1.filter_tasks(completed=True, pet_name="Topaz"))

# --- Filter: Topaz + completed=False (only Topaz's incomplete tasks) ---
print("=== Filter: Topaz + completed=False ===")
print(schedule1.filter_tasks(completed=False, pet_name="Topaz"))


# --- Schedule tasks + get end time: scheduled_time=9:45, duration=10 ===
print("=== Schedule tasks + get end time: scheduled_time=9:45, duration=10 ===")
print(task1.scheduled_time) # None
print(task1.get_end_time()) # None
task1.schedule_at(datetime.today().combine(datetime.today(), time(hour=9, minute=45)))
print(task1.scheduled_time) # 09:45
print(task1.get_end_time()) # 09:55

# --- Schedule tasks + get end time: scheduled_time=9:45, duration=10 ===
print("=== Schedule tasks + get end time: scheduled_time=23:55, duration=10 ===")
task1.schedule_at(datetime.combine(datetime.today(), time(hour=23, minute=55)))
print(task1.scheduled_time) # 23:55
print(task1.get_end_time()) # 00:05


owner = Owner(name="Alice")
scheduler = Scheduler(owner)

# task1: 9:00 - 9:30
task1 = Task(title="Feed", duration=30, priority="high")
task1.schedule_at(datetime(2026, 3, 31, 9, 0))

# task2: 9:15 - 9:45 (overlaps with task1)
task2 = Task(title="Walk", duration=30, priority="medium")
task2.schedule_at(datetime(2026, 3, 31, 9, 15))

print(scheduler.has_conflict([task1], task2)) # True