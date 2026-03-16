# PawPal+

PawPal+ is a pet care management system that helps owners organize daily routines like feedings, walks, medication, and appointments.

## Features

- Object-oriented backend with `Owner`, `Pet`, `Task`, and `Scheduler`
- CLI demo in `main.py`
- Streamlit UI in `app.py`
- Sorting tasks by time
- Filtering tasks by pet and status
- Recurring task support for daily and weekly tasks
- Conflict detection for exact duplicate task times

## Running the CLI demo

```bash
python main.py
```

## Running the Streamlit app

```bash
streamlit run app.py
```

## Testing PawPal+

Run tests with:

```bash
python -m pytest
```

The tests cover sorting, recurring task creation, conflict detection, and task addition behavior.

**Confidence Level:** ⭐⭐⭐⭐☆ (4/5)

## Smarter Scheduling

The scheduler now supports sorting tasks chronologically, filtering tasks by pet or completion status, creating the next occurrence of recurring tasks, and detecting exact-time scheduling conflicts.

## Design Summary

The system is built around four main classes:
- `Owner` manages pets
- `Pet` stores pet details and tasks
- `Task` represents a scheduled activity
- `Scheduler` organizes and evaluates tasks across pets