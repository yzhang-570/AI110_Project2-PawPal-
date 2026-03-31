# Assumption: all tasks are daily
class Task:
    """Represents a recurring pet care task."""

    _next_id = 1

    def __init__(
        self,
        description: str,
        duration: int,
        frequency: str,
    ):
        """Initialize task details and assign a unique task_id."""
        self.task_id = Task._next_id
        Task._next_id += 1
        self.description = description
        self.duration = duration            # in minutes
        self.frequency = frequency
        self.completed = False

    def __eq__(self, other: object):
        """Check task equality by task_id."""
        if not isinstance(other, Task):
            return NotImplemented
        return self.task_id == other.task_id
    
    def __str__(self):
        """Return a readable string describing the task."""
        return f"Task: {self.description}, Duration: {self.duration} minutes, Frequency: {self.frequency}x daily\n"

    # Prints formatted string in all contexts - ex. lists
    def __repr__(self):
        """Return the string representation of the task."""
        return self.__str__()

    def setDescription(self, description: str):
        """Update the task description."""
        self.description = description

    def setDuration(self, minutes: int):
        """Set the task duration in minutes, forcing positive values."""
        if minutes > 0:
            self.duration = minutes
        else: 
            self.duration = -1

    def setFrequency(self, frequency: int):
        """Set the repetition frequency daily, forcing positive values."""
        if frequency > 0:
            self.frequency = frequency
        else: 
            self.duration = -1

    def mark_complete(self):
        """Mark the task as completed."""
        self.completed = True

class Pet:
    """Represents a pet with a list of care tasks."""

    _next_id = 1

    def __init__(self, name: str, sex: str, age: int):
        """Initialize pet identity and tasks list."""
        self.pet_id = Pet._next_id
        Pet._next_id += 1
        self.name = name
        self.sex = sex
        self.age = age
        self.tasks: list[Task] = []

    def __eq__(self, other: object) -> bool:
        """Check pet equality by pet_id."""
        if not isinstance(other, Pet):
            return NotImplemented
        return self.pet_id == other.pet_id
    
    def setName(self, name: str):
        """Update the pet's name."""
        self.name = name

    def setSex(self, sex: str):
        """Update the pet's sex."""
        self.sex = sex

    def setAge(self, age: int):
        """Update the pet's age."""
        self.age = age

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

    def __init__(self, name: str, gender: str, age: int):
        """Initialize owner details and empty pet list."""
        self.name = name
        self.gender = gender
        self.age = age
        self.pets: list[Pet] = []

    def setName(self, name: str):
        """Update owner name."""
        self.name = name

    def setGender(self, gender: str):
        """Update owner gender with allowed values."""
        valid_genders = ["F", "M"]
        if gender in valid_genders:
            self.gender = gender

    def setAge(self, age: int):
        """Update owner age."""
        self.age = age

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
        self.schedule: list[Task] = []

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

    def generatePlan(self):
        """Generate schedule from all tasks in owner pets."""
        self.schedule = self.owner.getAllTasks()

    def getPlan(self):
        """Return the generated schedule."""
        return self.schedule
