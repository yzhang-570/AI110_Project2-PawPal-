from pawpal_system import Task, Pet, Owner, Scheduler

def test_mark_complete_sets_completed_true():
    task = Task(title="Feed the cat", duration=15, priority="high")
    assert task.completed is False

    task.mark_complete()

    assert task.completed is True


def test_add_task_increases_task_count():
    pet = Pet(name="Buddy", species="dog")
    initial_count = pet.getTaskCount()

    task = Task(title="Walk the dog", duration=30, priority="high")
    pet.addTask(task)

    assert pet.getTaskCount() == initial_count + 1


def test_filter_tasks_by_completion_and_pet():
    owner = Owner(name="Alice")
    dog = Pet(name="Buddy", species="dog")
    cat = Pet(name="Mochi", species="cat")
    owner.addPet(dog)
    owner.addPet(cat)

    t1 = Task(title="Walk", duration=30, priority="high")
    t2 = Task(title="Feed", duration=10, priority="medium")
    t3 = Task(title="Groom", duration=20, priority="low")
    dog.addTask(t1)
    dog.addTask(t2)
    cat.addTask(t3)

    t1.mark_complete()

    scheduler = Scheduler(owner)

    assert len(scheduler.filterTasks(completed=False)) == 2
    assert len(scheduler.filterTasks(pet_name="Buddy")) == 2
    assert len(scheduler.filterTasks(completed=False, pet_name="Buddy")) == 1