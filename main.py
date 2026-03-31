from pawpal_system import Owner, Task, Pet, Scheduler

owner1 = Owner("Yuwen")
pet1 = Pet("Topaz", "cat")
pet2 = Pet("Unnamed kitten", "cat")
owner1.addPet(pet1)
owner1.addPet(pet2)

task1 = Task(title="Feed Topaz", duration=10, priority="high")
task2 = Task(title="Open the door for Topaz", duration=5, priority="high")
task3 = Task(title="Feed kitten", duration=5, priority="medium")
task4 = Task(title="Play with Topaz", duration=15, priority="low")

pet1.addTask(task1)
pet1.addTask(task2)
pet2.addTask(task3)
pet1.addTask(task4)

schedule1 = Scheduler(owner1)
print("Original schedule")
print(schedule1)

# --- Sort by duration ---
print("=== Sorted by duration (all tasks) ===")
schedule1.sortTasksByDuration()
print(schedule1)

# --- Filter: Topaz only ---
print("=== Filter: Topaz only ===")
schedule1.filterTasks(completed=None, pet_name="Topaz")
print(schedule1)

# --- Filter: None, None resets to show all tasks ---
print("=== Filter: None, None (reset — all tasks) ===")
schedule1.filterTasks(completed=None, pet_name=None)
print(schedule1)

# --- Filter: Unnamed kitten only ---
print("=== Filter: Unnamed kitten only ===")
schedule1.filterTasks(completed=None, pet_name="Unnamed kitten")
print(schedule1)

# --- Mark some tasks complete, then filter by completed=True ---
task1.mark_complete()
task3.mark_complete()

print("=== Filter: completed=True (no pet filter) ===")
schedule1.filterTasks(completed=True, pet_name=None)
print(schedule1)

# --- Filter: completed=False (no pet filter) ---
print("=== Filter: completed=False (no pet filter) ===")
schedule1.filterTasks(completed=False, pet_name=None)
print(schedule1)

# --- Filter: Topaz + completed=True (only Topaz's completed tasks) ---
print("=== Filter: Topaz + completed=True ===")
schedule1.filterTasks(completed=True, pet_name="Topaz")
print(schedule1)

# --- Filter: Topaz + completed=False (only Topaz's incomplete tasks) ---
print("=== Filter: Topaz + completed=False ===")
schedule1.filterTasks(completed=False, pet_name="Topaz")
print(schedule1)