# PawPal+ Reflection

## 1a. Initial design
I chose four core classes: Owner, Pet, Task, and Scheduler. Owner stores the pets, Pet stores each pet's tasks, Task represents one scheduled activity, and Scheduler acts as the coordination layer that collects and organizes tasks. This matched the project prompt closely and kept the system modular.

## 1b. Design changes
One change I made during implementation was letting Task store `pet_name` so task displays and filters would be easier across the scheduler and UI. I also kept conflict detection lightweight by checking exact matching times instead of overlapping durations.

## 2b. Tradeoffs
The scheduler currently checks only exact time matches for conflicts. That makes the logic simpler and easier to explain, but it will not catch longer overlapping appointments unless they share the same exact timestamp.

## AI strategy
Copilot-style suggestions are most useful when scaffolding class structures and test ideas, but they sometimes overcomplicate the system. I would reject any suggestion that added extra classes or hidden abstractions not required by the prompt. Separate chat sessions for design, implementation, and testing help keep the workflow organized and reduce context drift.

## What I learned
This project reinforced that the human still has to act as the architect. AI can speed up drafting, but I still have to verify relationships, state flow, and algorithm choices carefully.