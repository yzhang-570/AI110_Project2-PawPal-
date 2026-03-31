from pawpal_system import Owner, Task, Pet, Scheduler

owner1 = Owner("Yuwen", "F", 20)
pet1 = Pet("Topaz", "F", 1)
pet2 = Pet("Unnamed kitten", "M", 0)
owner1.addPet(pet1)
owner1.addPet(pet2)

task1 = Task("Feed Topaz", 10, 4)
task2 = Task("Open the door for Topaz", 5, 2)
task3 = Task("Feed kitten", 5, 2)

pet1.addTask(task1)
pet1.addTask(task2)
pet2.addTask(task3)

schedule1 = Scheduler(owner1)
print("Today's schedule")
schedule1.generatePlan()
print(schedule1.getPlan())