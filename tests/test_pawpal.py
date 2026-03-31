from pawpal_system import Task, Pet

def test_mark_complete_sets_completed_true():
    task = Task(description="Feed the cat", duration=15, frequency="2")
    assert task.completed is False

    task.mark_complete()

    assert task.completed is True


def test_add_task_increases_task_count():
    pet = Pet(name="Buddy", sex="M", age=3)
    initial_count = pet.getTaskCount()

    task = Task(description="Walk the dog", duration=30, frequency="1")
    pet.addTask(task)

    assert pet.getTaskCount() == initial_count + 1
