from dataclasses import dataclass, field
from datetime import datetime, timedelta
from typing import List, Optional


@dataclass
class Task:
    description: str
    time: str
    frequency: str = "once"   # once, daily, weekly
    completed: bool = False
    pet_name: str = ""

    def mark_complete(self) -> None:
        """Mark the task as completed."""
        self.completed = True


@dataclass
class Pet:
    name: str
    species: str
    tasks: List[Task] = field(default_factory=list)

    def add_task(self, task: Task) -> None:
        """Add a task to this pet."""
        task.pet_name = self.name
        self.tasks.append(task)


@dataclass
class Owner:
    name: str
    pets: List[Pet] = field(default_factory=list)

    def add_pet(self, pet: Pet) -> None:
        """Add a pet to the owner."""
        self.pets.append(pet)

    def get_all_tasks(self) -> List[Task]:
        """Return all tasks across all pets."""
        all_tasks = []
        for pet in self.pets:
            all_tasks.extend(pet.tasks)
        return all_tasks


@dataclass
class Scheduler:
    owner: Owner

    def get_all_tasks(self) -> List[Task]:
        """Return all tasks from the owner's pets."""
        return self.owner.get_all_tasks()

    def sort_by_time(self) -> List[Task]:
        """Return tasks sorted in HH:MM order."""
        return sorted(self.get_all_tasks(), key=lambda task: task.time)

    def filter_tasks(
        self,
        status: Optional[bool] = None,
        pet_name: Optional[str] = None,
    ) -> List[Task]:
        """Filter tasks by completion status and/or pet name."""
        tasks = self.get_all_tasks()

        if status is not None:
            tasks = [task for task in tasks if task.completed == status]

        if pet_name is not None:
            tasks = [task for task in tasks if task.pet_name.lower() == pet_name.lower()]

        return tasks

    def mark_task_complete(self, task: Task) -> Optional[Task]:
        """
        Mark a task complete.
        If it is recurring, create and return the next occurrence.
        """
        task.mark_complete()

        if task.frequency == "daily":
            next_time = self._shift_time(task.time, days=1)
            new_task = Task(
                description=task.description,
                time=next_time,
                frequency=task.frequency,
                completed=False,
                pet_name=task.pet_name,
            )
            self._attach_new_task(task.pet_name, new_task)
            return new_task

        if task.frequency == "weekly":
            next_time = self._shift_time(task.time, days=7)
            new_task = Task(
                description=task.description,
                time=next_time,
                frequency=task.frequency,
                completed=False,
                pet_name=task.pet_name,
            )
            self._attach_new_task(task.pet_name, new_task)
            return new_task

        return None

    def detect_conflicts(self) -> List[str]:
        """
        Return warning messages when two tasks share the exact same time.
        Lightweight conflict detection by exact time match.
        """
        tasks = self.sort_by_time()
        warnings = []

        for i in range(len(tasks)):
            for j in range(i + 1, len(tasks)):
                if tasks[i].time == tasks[j].time:
                    warnings.append(
                        f"Conflict: '{tasks[i].description}' for {tasks[i].pet_name} and "
                        f"'{tasks[j].description}' for {tasks[j].pet_name} are both scheduled at {tasks[i].time}."
                    )

        return warnings

    def _attach_new_task(self, pet_name: str, new_task: Task) -> None:
        """Attach a recurring task instance back to the correct pet."""
        for pet in self.owner.pets:
            if pet.name.lower() == pet_name.lower():
                pet.add_task(new_task)
                return

    def _shift_time(self, time_str: str, days: int = 0) -> str:
        """
        Shift a YYYY-MM-DD HH:MM timestamp by a number of days.
        If only HH:MM is supplied, preserve it as-is.
        """
        try:
            dt = datetime.strptime(time_str, "%Y-%m-%d %H:%M")
            return (dt + timedelta(days=days)).strftime("%Y-%m-%d %H:%M")
        except ValueError:
            return time_str