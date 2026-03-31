"""
Classes:
1. Owner
- Attributes: name, gender, age, pets
- Methods: setName, setGender, setAge, addPet, removePet, getAllTasks

2. Pet
- Attributes: name, sex, age, tasks
- Methods: setName, setSex, setAge, addTask, removeTask, getTasks

3. Task
- Attributes: task_id, name, duration, priority_level, repeat, task_type, time_preference, completed
- Methods: setName, setDuration, setFrequency, setType, setPriority, setTimePreference, setCompleted

4. Scheduler
- Attributes: owner
- Methods: addTask, removeTask, editTask, generatePlan
"""

"""
Classes (current):
1. Owner
- Attributes: name, gender, age, pets
- Methods: setName, setGender, setAge, addPet, removePet, getAllTasks

2. Pet
- Attributes: name, sex, age, tasks
- Methods: setName, setSex, setAge, addTask, removeTask, getTasks

3. Task
- Attributes: task_id (auto-incremented), description, duration, frequency, completed
- Methods: setName, setDuration, setFrequency, setCompleted

4. Scheduler
- Attributes: owner
- Methods: addTask, removeTask, editTask, generatePlan
"""


class Task:
    _next_id = 1

    def __init__(
        self,
        description: str,
        duration: int,
        frequency: str,
        # priority_level: int,
        # repeat: str,
        # task_type: str,
        # time_preference: str,
    ):
        self.task_id = Task._next_id
        Task._next_id += 1
        self.description = description
        self.duration = duration            # in minutes
        self.frequency = frequency # "daily", "twice_daily", "weekly", etc.
        # self.priority_level = priority_level  # 1 (low) to 5 (high)
        # self.task_type = task_type          # "pet_care" or "constraint"
        # self.time_preference = time_preference  # "morning", "noon", "evening"
        self.completed = False

    def setName(self, name: str):
        pass

    def setDuration(self, minutes: int):
        pass

    def setFrequency(self, repeat: str):
        # TODO: validate repeat is one of: "x_times_daily", "twice_daily", "daily", "weekly", "biweekly", "monthly", "yearly"
        pass

    def setType(self, task_type: str):
        # TODO: validate task_type is one of: "pet_care", "constraint"
        pass

    def setPriority(self, level: int):
        pass

    def setTimePreference(self, slot: str):
        # TODO: validate slot is one of: "morning", "noon", "evening"
        pass

    def setCompleted(self, status: bool):
        pass


class Pet:
    def __init__(self, name: str, sex: str, age: int):
        self.name = name
        self.sex = sex
        self.age = age
        self.tasks: list[Task] = []

    def setName(self, name: str):
        pass

    def setSex(self, sex: str):
        pass

    def setAge(self, age: int):
        pass

    def addTask(self, task: Task):
        pass

    def removeTask(self, task_id: int):
        pass

    def getTasks(self) -> list[Task]:
        pass


class Owner:
    def __init__(self, name: str, gender: str, age: int):
        self.name = name
        self.gender = gender
        self.age = age
        self.pets: list[Pet] = []

    def setName(self, name: str):
        pass

    def setGender(self, gender: str):
        pass

    def setAge(self, age: int):
        pass

    def addPet(self, pet: Pet):
        pass

    def removePet(self, pet: Pet):
        pass

    def getAllTasks(self) -> list[Task]:
        # aggregate and return all tasks across all pets
        pass


class Scheduler:
    def __init__(self, owner: Owner):
        self.owner = owner

    def addTask(self, pet: Pet, task: Task):
        pass

    def removeTask(self, task_id: int):
        # search across all pets via owner.getAllTasks()
        pass

    def editTask(self, task_id: int, updated_task: Task):
        # search across all pets via owner.getAllTasks()
        pass

    def generatePlan(self):
        # TODO: retrieve all tasks via owner.getAllTasks()
        # sort/filter by priority_level, time_preference, and repeat
        # return an ordered list of tasks representing the daily schedule
        pass