class Owner:
    def __init__(self, name: str, gender: str, age: int):
        self.name = name
        self.gender = gender
        self.age = age

    def setName(self, name: str):
        pass

    def setGender(self, gender: str):
        pass

    def setAge(self, age: int):
        pass


class Pet:
    def __init__(self, name: str, sex: str, age: int):
        self.name = name
        self.sex = sex
        self.age = age

    def setName(self, name: str):
        pass

    def setSex(self, sex: str):
        pass

    def setAge(self, age: int):
        pass


class Task:
    def __init__(
        self,
        name: str,
        duration: int,
        priority_level: int,
        repeat: str,
        task_type: str,
        time_preference: str,
    ):
        self.name = name
        self.duration = duration          # in minutes
        self.priority_level = priority_level  # e.g. 1 (low) to 5 (high)
        self.repeat = repeat              # e.g. "daily", "twice_daily", "weekly"
        self.task_type = task_type        # "pet_care" or "constraint"
        self.time_preference = time_preference  # "morning", "noon", "evening"

    def setName(self, name: str):
        pass

    def setDuration(self, minutes: int):
        pass

    def setFrequency(self, repeat: str):
        pass

    def setType(self, task_type: str):
        pass

    def setPriority(self, level: int):
        pass

    def setTimePreference(self, slot: str):
        pass


class Scheduler:
    def __init__(self):
        self.task_list: list[Task] = []

    def addTask(self, task: Task):
        pass

    def removeTask(self, task: Task):
        pass

    def editTask(self, task: Task):
        pass
