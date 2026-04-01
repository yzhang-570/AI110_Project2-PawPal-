from datetime import datetime, timedelta, date

valid_priorities = ["low", "medium", "high"]
valid_species = ["dog", "cat", "other"]
valid_frequencies = ["daily", "weekly"]

class Task:
    """Represents a recurring pet care task."""

    _next_id = 1

    """int id, str title, bool completed, int duration, str priority, str frequency, time preferred_time, time scheduled_time"""
    def __init__(self, title: str, duration: int, priority: str, frequency: str = "daily", preferred_time: datetime | None = None):
                 
        """Initialize task details and assign a unique task_id."""

        self.task_id = Task._next_id
        Task._next_id += 1
        self.title = title

        if frequency in valid_frequencies:
            self.frequency = frequency         # "daily", "weekly"

        self.duration = duration               # minutes

        if priority in valid_priorities:
            self.priority = priority            # "low", "medium", "high"

        self.preferred_time = preferred_time    # preferred start time
        self.scheduled_time = None
        self.completed = False

    def __eq__(self, other: object):
        """Check task equality by task_id."""
        if not isinstance(other, Task):
            return NotImplemented
        return self.task_id == other.task_id

    # TODO: update to print all properties
    def __str__(self):
        """Return a readable string describing the task."""
        return f"Task: {self.title}, Priority: {self.priority}, Duration: {self.get_duration()}\n"

    # Prints formatted string in all contexts - ex. lists
    def __repr__(self):
        """Return the string representation of the task."""
        return self.__str__()

    # TODO: update to update all properties
    def edit_task(self, updated_task: "Task"):
        """Update a task's properties."""
        self.description = updated_task.description
        self.duration = updated_task.duration
        self.frequency = updated_task.frequency
        self.scheduled_time = updated_task.scheduled_time
        self.completed = updated_task.completed

    def get_duration(self) -> str:
        """Return duration as a formatted HH:MM string."""
        hours = self.duration // 60
        mins = self.duration % 60
        return f"{hours:02d}:{mins:02d}"

    # TODO: create a method to schedule tasks on generate_schedule
        # for all tasks - if complete and weekly

    # TODO: extract detect conflict as a separate/outside function ->
        # return false if conflicts with existing schedule

    def schedule_at(self, scheduled_time: datetime):
        """Schedule this task at specified start time"""
        self.scheduled_time = scheduled_time

    def set_as_completed(self) -> None:
        """Mark the task as completed and returns next occurrence."""
        self.completed = True

    def get_end_time(self) -> datetime | None:
        """Return the end time derived from scheduled_time + duration. Returns None if not scheduled."""
        
        # end time only exists is task has been scheduled
        if self.scheduled_time is None:
            return None
        
        # temporarily converts to full date(datetime) object to use timedelta
        start_dt = self.scheduled_time
        return (start_dt + timedelta(minutes=self.duration))


class Pet:
    """Represents a pet with a list of care tasks."""

    _next_id = 1

    def __init__(self, name: str, species: str):
        """Initialize pet identity and tasks list."""
        self.pet_id = Pet._next_id
        Pet._next_id += 1
        self.name = name
        if species in valid_species:
            self.species = species # "dog", "cat", "other"
        self.tasks: list[Task] = []

    def __eq__(self, other: object) -> bool:
        """Check pet equality by pet_id."""
        if not isinstance(other, Pet):
            return NotImplemented
        return self.pet_id == other.pet_id

    def __str__(self):
        """Return a readable string describing the pet."""
        return f"Pet: {self.name}, Species: {self.species}, Tasks: {self.get_task_count()}\n"

    def __repr__(self):
        """Return the string representation of the pet."""
        return self.__str__()

    def add_task(self, task: Task):
        """Add a task to the pet's task list."""
        self.tasks.append(task)

    def remove_task(self, task: Task):
        """Remove a task from the pet's task list."""
        self.tasks.remove(task)

    def get_tasks(self) -> list[Task]:
        """Return all tasks for the pet."""
        return self.tasks

    def get_task_count(self):
        """Return the number of tasks assigned to the pet."""
        return len(self.tasks)


class Owner:
    """Represents a pet owner with one or more pets."""

    def __init__(self, name: str):
        """Initialize owner details and empty pet list."""
        self.name = name
        self.pets: list[Pet] = []

    def __str__(self):
        """Return a readable string describing the owner."""
        return f"Name: {self.name}, Pets: {self.pets}"

    def __repr__(self):
        """Return the string representation of the owner."""
        return self.__str__()

    def add_pet(self, pet: Pet):
        """Add a pet to the owner's list."""
        self.pets.append(pet)

    # def remove_pet(self, pet: Pet):
    #     """Remove a pet from the owner's list."""
    #     self.pets.remove(pet)

    def get_pets(self):
        """Return the list of owner's pets."""
        return self.pets

    def get_all_tasks(self) -> list[Task]:
        """Aggregate and return all tasks from all pets."""
        all_tasks = []
        for pet in self.pets:
            all_tasks.extend(pet.get_tasks())
        return all_tasks


class Scheduler:
    """Coordinates tasks for an owner across all pets for display."""

    # TODO: make source of truth - filtering returns new to display, but doesn't overwrite data

    def __init__(self, owner: Owner):
        """Initialize scheduler with an owner and empty schedule."""
        self.owner = owner
        self.schedule: list[Task] = self.generate_plan()

    def __str__(self):
        """Return a readable string describing the order of scheduled tasks."""
        return "".join(str(task) for task in self.schedule)

    def __repr__(self):
        """Return the string representation of the order of scheduled tasks."""
        return self.__str__()

    # TODO: understand why this works
    """
    Collect all tasks from all pets via owner.get_all_tasks()
    Filter to compelted is false
    Sort: high → medium → low, with preferred_time tasks first within each group
    For each task, assign to day(s) based on frequency
    Return the dict[date, list[Task]]
    """
    def generate_plan(self) -> dict[date, list[Task]]:
        """Returns a weekly schedule as a dictionary - key=date, value=tasks."""
        tasks_to_schedule = self.filter_tasks(completed=False)

        priority_order = {"high": 0, "medium": 1, "low": 2}
        sorted_tasks = sorted(tasks_to_schedule,
                              key=lambda t: (priority_order[t.priority], t.preferred_time is None))

        today = datetime.today().date()
        schedule: dict[date, list[Task]] = {today + timedelta(days=i): [] for i in range(7)}

        DEFAULT_START_HOUR = 8

        for task in sorted_tasks:
            days = list(schedule.keys()) if task.frequency == "daily" else [list(schedule.keys())[0]]

            for day in days:
                if task.preferred_time is not None:
                    candidate = datetime.combine(day, task.preferred_time.time())
                else:
                    candidate = datetime(day.year, day.month, day.day, DEFAULT_START_HOUR, 0)

                task.schedule_at(candidate)
                if not self.has_conflict(schedule[day], task):
                    schedule[day].append(task)

        return schedule

    def complete_task(self, task: Task):
        task.set_as_completed()
        new_occurrence = Task(task.title, task.duration, task.priority, task.frequency, task.preferred_time)

        if task.frequency == "daily":
            new_occurrence.schedule_at(task.scheduled_time + timedelta(hours=24))
        elif task.frequency == "weekly":
            new_occurrence.schedule_at(task.scheduled_time + timedelta(days=7))

        owner_pet = next((pet for pet in self.owner.get_pets() if task in pet.get_tasks()), None)
        if owner_pet is None:
            return

        # not necessary next day, but scheduled day
        next_day_tasks = [t for t in owner_pet.get_tasks() if t.scheduled_time and t.scheduled_time.date() == new_occurrence.scheduled_time.date()]
        if not self.has_conflict(next_day_tasks, new_occurrence):
            owner_pet.add_task(new_occurrence)

    def sort_tasks_by_scheduled_time(self):
        """Sort all tasks by scheduled time in ascending order."""
        self.schedule = sorted(self.owner.get_all_tasks(), key=lambda task: task.scheduled_time)
        return self.schedule

    def filter_tasks(self, completed: bool | None = None, pet_name: str | None = None) -> list[Task]:
        """Filter and returns all tasks by completion status and/or pet name."""

        """
        inputs: 
        - completed: True for completed tasks, False for incomplete tasks, None for all tasks.
        - pet_name: case-insensitive pet name, None for all pets.
        """

        filtered: list[Task] = []

        for pet in self.owner.get_pets():
            if pet_name is not None and pet.name.lower() != pet_name.lower():
                continue

            for task in pet.get_tasks():
                if completed is not None and task.completed != completed:
                    continue
                filtered.append(task)

        return filtered


    # TODO: understand why this works
    def has_conflict(self, day_tasks: list[Task], task: Task) -> bool:
        """Return True if task overlaps with any already-scheduled task in day_tasks.
        
        precondition: Task must have a candidate scheduled_time set
        """
        for existing in day_tasks:
            if task.scheduled_time < existing.get_end_time() and task.get_end_time() > existing.scheduled_time:
                return True
        return False

