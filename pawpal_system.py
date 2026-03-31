valid_priorities = ["low", "medium", "high"]
valid_species = ["dog", "cat", "other"]

# Assumption: all tasks are daily
class Task:
    """Represents a recurring pet care task."""

    _next_id = 1

    def __init__(
        self,
        title: str,
        duration: int,
        priority: str
    ):
        """Initialize task details and assign a unique task_id."""
        self.task_id = Task._next_id
        Task._next_id += 1
        self.title = title
        hours = duration // 60
        mins = duration % 60
        self.duration = f"{hours:02d}:{mins:02d}"  # in HH:MM format
        if priority in valid_priorities:
            self.priority = priority            # "low", "medium", "high"
        self.completed = False

    def __eq__(self, other: object):
        """Check task equality by task_id."""
        if not isinstance(other, Task):
            return NotImplemented
        return self.task_id == other.task_id
    
    def __str__(self):
        """Return a readable string describing the task."""
        return f"Task: {self.title}, Priority: {self.priority}, Duration: {self.duration}\n"

    # Prints formatted string in all contexts - ex. lists
    def __repr__(self):
        """Return the string representation of the task."""
        return self.__str__()

    def mark_complete(self):
        """Mark the task as completed."""
        self.completed = True

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
        return f"Pet: {self.name}, Species: {self.species}, Tasks: {self.getTaskCount()}\n"

    def __repr__(self):
        """Return the string representation of the pet."""
        return self.__str__()

    def addTask(self, task: Task):
        """Add a task to the pet's task list."""
        self.tasks.append(task)

    def removeTask(self, task: Task):
        """Remove a task from the pet's task list."""
        self.tasks.remove(task)

    def getTasks(self) -> list[Task]:
        """Return all tasks for the pet."""
        return self.tasks
    
    def getTaskCount(self):
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
        return f"""Name: {self.name}, Pets: {self.pets}"""
    
    def __repr__(self):
        """Return the string representation of the owner."""
        return self.__str__()

    def addPet(self, pet: Pet):
        """Add a pet to the owner's list."""
        self.pets.append(pet)

    def removePet(self, pet: Pet):
        """Remove a pet from the owner's list."""
        self.pets.remove(pet)

    def getPets(self):
        """Return the list of owner's pets."""
        return self.pets

    def getAllTasks(self) -> list[Task]:
        """Aggregate and return all tasks from all pets."""
        all_tasks = []
        for pet in self.pets:
            all_tasks.extend(pet.getTasks())
        return all_tasks


class Scheduler:
    """Coordinates tasks for an owner across all pets."""

    def __init__(self, owner: Owner):
        """Initialize scheduler with an owner and empty schedule."""
        self.owner = owner
        self.schedule: list[Task] = self.owner.getAllTasks()

    def __str__(self):
        """Return a readable string describing the order of scheduled tasks."""
        return "".join(str(task) for task in self.schedule)

    def __repr__(self):
        """Return the string representation of the order of scheduled tasks."""
        return self.__str__()

    def addTask(self, pet: Pet, task: Task):
        """Add a task for a specific pet."""
        pet.addTask(task)

    def removeTask(self, task: Task):
        """Remove a task from all pets that own it (are associated)."""
        for pet in self.owner.getPets():
            pet.removeTask(task)

    def editTask(self, task_id: int, updated_task: Task):
        """Update a task's properties by task_id."""
        for task in self.owner.getAllTasks():
            if task.task_id == task_id:
                task.description = updated_task.description
                task.duration = updated_task.duration
                task.frequency = updated_task.frequency
                task.completed = updated_task.completed
                return

    def sortTasksByDuration(self):
        """Sort the schedule by task duration in ascending order using HH:MM format as key  and updates the order of tasks in the scheduler's current plan."""
        self.schedule = sorted(
            self.schedule,
            key=lambda task: int(task.duration.split(':')[0]) * 60 + int(task.duration.split(':')[1])
        )

    def filterTasks(self, completed: bool | None = None, pet_name: str | None = None) -> list[Task]:
        """Filter tasks by completion status and/or pet name and updates the scheduler's current plan.

        - completed: True for completed tasks, False for incomplete tasks, None for all.
        - pet_name: case-insensitive pet name, None for all pets.
        """
        filtered: list[Task] = []

        for pet in self.owner.getPets():
            if pet_name is not None and pet.name.lower() != pet_name.lower():
                continue

            for task in pet.getTasks():
                if completed is not None and task.completed != completed:
                    continue
                filtered.append(task)

        self.schedule = filtered
