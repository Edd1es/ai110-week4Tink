# PawPal+ System Design

## Core user actions
1. Add a pet
2. Schedule a task for a pet
3. View and organize today's tasks

## Class responsibilities

### Owner
Stores owner information and the list of pets they manage.

### Pet
Stores pet details and that pet's tasks.

### Task
Represents one scheduled pet-care task such as feeding, walking, medication, or an appointment.

### Scheduler
Acts as the coordination layer that collects tasks across pets, sorts them, filters them, detects conflicts, and handles recurring task logic.

## Mermaid UML

```mermaid
classDiagram
    class Owner {
        +name: str
        +pets: list[Pet]
        +add_pet(pet)
        +get_all_tasks()
    }

    class Pet {
        +name: str
        +species: str
        +tasks: list[Task]
        +add_task(task)
    }

    class Task {
        +description: str
        +time: str
        +frequency: str
        +completed: bool
        +pet_name: str
        +mark_complete()
    }

    class Scheduler {
        +owner: Owner
        +get_all_tasks()
        +sort_by_time()
        +filter_tasks(status, pet_name)
        +mark_task_complete(task)
        +detect_conflicts()
    }

    Owner "1" --> "*" Pet
    Pet "1" --> "*" Task
    Scheduler "1" --> "1" Owner