import streamlit as st
from pawpal_system import Owner, Pet, Task, Scheduler


st.set_page_config(page_title="PawPal+", layout="wide")
st.title("PawPal+")
st.caption("Smart pet care scheduling system")


def initialize_state():
    if "owner" not in st.session_state:
        st.session_state.owner = Owner("Eddie")
    if "scheduler" not in st.session_state:
        st.session_state.scheduler = Scheduler(st.session_state.owner)


initialize_state()

owner = st.session_state.owner
scheduler = st.session_state.scheduler

st.sidebar.header("Add a Pet")
pet_name = st.sidebar.text_input("Pet name")
pet_species = st.sidebar.selectbox("Species", ["Dog", "Cat", "Bird", "Other"])

if st.sidebar.button("Add Pet"):
    if pet_name.strip():
        owner.add_pet(Pet(pet_name.strip(), pet_species))
        st.sidebar.success(f"Added pet: {pet_name}")
    else:
        st.sidebar.warning("Enter a pet name first.")

st.sidebar.header("Schedule a Task")
pet_options = [pet.name for pet in owner.pets]

if pet_options:
    selected_pet = st.sidebar.selectbox("Choose pet", pet_options)
    task_description = st.sidebar.text_input("Task description")
    task_time = st.sidebar.text_input("Task time (YYYY-MM-DD HH:MM)")
    task_frequency = st.sidebar.selectbox("Frequency", ["once", "daily", "weekly"])

    if st.sidebar.button("Add Task"):
        if task_description.strip() and task_time.strip():
            task = Task(task_description.strip(), task_time.strip(), task_frequency)
            for pet in owner.pets:
                if pet.name == selected_pet:
                    pet.add_task(task)
                    st.sidebar.success(f"Added task for {selected_pet}")
                    break
        else:
            st.sidebar.warning("Fill out both description and time.")
else:
    st.sidebar.info("Add a pet first to schedule tasks.")

st.header("Pets")
if owner.pets:
    for pet in owner.pets:
        st.write(f"- **{pet.name}** ({pet.species})")
else:
    st.write("No pets added yet.")

st.header("All Tasks (Sorted)")
tasks = scheduler.sort_by_time()
if tasks:
    task_rows = [
        {
            "Pet": task.pet_name,
            "Task": task.description,
            "Time": task.time,
            "Frequency": task.frequency,
            "Completed": task.completed,
        }
        for task in tasks
    ]
    st.table(task_rows)
else:
    st.write("No tasks scheduled yet.")

st.header("Conflicts")
conflicts = scheduler.detect_conflicts()
if conflicts:
    for warning in conflicts:
        st.warning(warning)
else:
    st.success("No scheduling conflicts.")