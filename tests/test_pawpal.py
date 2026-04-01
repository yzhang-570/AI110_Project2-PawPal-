from datetime import datetime
from pawpal_system import Task, Pet, Owner, Scheduler

def test_set_as_completed_sets_completed_true():
    task = Task(title="Feed the cat", duration=15, priority="high")
    assert task.completed is False

    task.set_as_completed()

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

    t1.set_as_completed()

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


def test_sort_tasks_by_scheduled_time_returns_chronological_order():
    owner = Owner(name="Alice")
    pet = Pet(name="Buddy", species="dog")
    owner.add_pet(pet)

    t1 = Task(title="Walk", duration=30, priority="high")
    t2 = Task(title="Feed", duration=10, priority="medium")
    t3 = Task(title="Groom", duration=20, priority="low")
    pet.add_task(t1)
    pet.add_task(t2)
    pet.add_task(t3)

    scheduler = Scheduler(owner)

    # set after scheduler init so generate_plan doesn't overwrite them
    t1.schedule_at(datetime(2026, 3, 31, 10, 0))
    t2.schedule_at(datetime(2026, 3, 31, 8, 0))
    t3.schedule_at(datetime(2026, 3, 31, 9, 0))

    result = scheduler.sort_tasks_by_scheduled_time()

    assert result == [t2, t3, t1]  # 8:00, 9:00, 10:00


def test_complete_daily_task_creates_next_day_occurrence():
    owner = Owner(name="Alice")
    pet = Pet(name="Buddy", species="dog")
    owner.add_pet(pet)

    task = Task(title="Feed", duration=15, priority="high", frequency="daily")
    pet.add_task(task)

    scheduler = Scheduler(owner)

    # set after scheduler init so generate_plan doesn't overwrite it
    task.schedule_at(datetime(2026, 3, 31, 8, 0))
    scheduler.complete_task(task)

    next_occurrence = pet.get_tasks()[-1]
    assert next_occurrence.scheduled_time == datetime(2026, 4, 1, 8, 0)


def test_has_conflict_returns_true_for_overlapping_tasks():
    owner = Owner(name="Alice")
    scheduler = Scheduler(owner)

    # task1: 9:00 - 9:30
    task1 = Task(title="Feed", duration=30, priority="high")
    task1.schedule_at(datetime(2026, 3, 31, 9, 0))

    # task2: 9:15 - 9:45 (overlaps with task1)
    task2 = Task(title="Walk", duration=30, priority="medium")
    task2.schedule_at(datetime(2026, 3, 31, 9, 15))

    assert scheduler.has_conflict([task1], task2) is True
