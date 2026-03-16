from pawpal_system import Owner, Pet, Task, Scheduler


def main():
    owner = Owner("Eddie")

    dog = Pet("Milo", "Dog")
    cat = Pet("Luna", "Cat")

    owner.add_pet(dog)
    owner.add_pet(cat)

    dog.add_task(Task("Morning walk", "2026-04-01 08:00", "daily"))
    dog.add_task(Task("Feed breakfast", "2026-04-01 08:00", "once"))
    cat.add_task(Task("Medication", "2026-04-01 09:00", "weekly"))

    scheduler = Scheduler(owner)

    print("=== Today's Schedule ===")
    for task in scheduler.sort_by_time():
        status = "Done" if task.completed else "Pending"
        print(f"{task.time} | {task.pet_name} | {task.description} | {task.frequency} | {status}")

    print("\n=== Conflicts ===")
    conflicts = scheduler.detect_conflicts()
    if conflicts:
        for warning in conflicts:
            print(warning)
    else:
        print("No conflicts found.")

    print("\n=== Marking first task complete ===")
    new_task = scheduler.mark_task_complete(dog.tasks[0])
    if new_task:
        print(f"Recurring task created: {new_task.description} at {new_task.time}")

    print("\n=== Updated Schedule ===")
    for task in scheduler.sort_by_time():
        status = "Done" if task.completed else "Pending"
        print(f"{task.time} | {task.pet_name} | {task.description} | {task.frequency} | {status}")


if __name__ == "__main__":
    main()