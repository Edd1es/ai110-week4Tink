from pawpal_system import Owner, Pet, Task, Scheduler


def build_scheduler():
    owner = Owner("Eddie")
    dog = Pet("Milo", "Dog")
    cat = Pet("Luna", "Cat")

    owner.add_pet(dog)
    owner.add_pet(cat)

    dog.add_task(Task("Walk", "2026-04-01 09:00", "daily"))
    dog.add_task(Task("Breakfast", "2026-04-01 08:00", "once"))
    cat.add_task(Task("Medication", "2026-04-01 09:00", "weekly"))

    return Scheduler(owner), dog, cat


def test_sorting_correctness():
    scheduler, _, _ = build_scheduler()
    tasks = scheduler.sort_by_time()
    assert tasks[0].description == "Breakfast"
    assert tasks[1].time <= tasks[2].time


def test_recurrence_logic_daily_task_creates_new_task():
    scheduler, dog, _ = build_scheduler()
    original_task = dog.tasks[0]
    new_task = scheduler.mark_task_complete(original_task)

    assert original_task.completed is True
    assert new_task is not None
    assert new_task.description == original_task.description
    assert len(dog.tasks) == 3


def test_conflict_detection_flags_duplicate_times():
    scheduler, _, _ = build_scheduler()
    conflicts = scheduler.detect_conflicts()
    assert len(conflicts) >= 1
    assert "Conflict" in conflicts[0]


def test_adding_task_increases_pet_task_count():
    owner = Owner("Eddie")
    pet = Pet("Milo", "Dog")
    owner.add_pet(pet)

    initial_count = len(pet.tasks)
    pet.add_task(Task("Vet visit", "2026-04-01 14:00", "once"))

    assert len(pet.tasks) == initial_count + 1