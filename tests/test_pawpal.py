from datetime import datetime
from pawpal_system import Task, Pet, Owner, Scheduler

def test_set_as_complete_sets_completed_true():
    task = Task(title="Feed the cat", duration=15, priority="high")
    assert task.completed is False

    task.set_as_complete()

    assert task.completed is True


def test_add_task_increases_task_count():
    pet = Pet(name="Buddy", species="dog")
    initial_count = pet.get_task_count()

    task = Task(title="Walk the dog", duration=30, priority="high")
    pet.add_task(task)

    assert pet.get_task_count() == initial_count + 1


def test_filter_tasks_by_completion_and_pet():
    owner = Owner(name="Alice")
    dog = Pet(name="Buddy", species="dog")
    cat = Pet(name="Mochi", species="cat")
    owner.add_pet(dog)
    owner.add_pet(cat)

    t1 = Task(title="Walk", duration=30, priority="high")
    t2 = Task(title="Feed", duration=10, priority="medium")
    t3 = Task(title="Groom", duration=20, priority="low")
    dog.add_task(t1)
    dog.add_task(t2)
    cat.add_task(t3)

    t1.set_as_complete()

    scheduler = Scheduler(owner)

    assert len(scheduler.filter_tasks(completed=False)) == 2
    assert len(scheduler.filter_tasks(pet_name="Buddy")) == 2
    assert len(scheduler.filter_tasks(completed=False, pet_name="Buddy")) == 1


def test_task_frequency_defaults_to_daily():
    task = Task(title="Morning walk", duration=30, priority="high")
    assert task.frequency == "daily"


def test_task_frequency_weekly():
    task = Task(title="Bath time", duration=45, priority="medium", frequency="weekly")
    assert task.frequency == "weekly"


def test_task_frequency_invalid_falls_back_to_daily():
    task = Task(title="Grooming", duration=20, priority="low", frequency="daily")
    assert task.frequency == "daily"
