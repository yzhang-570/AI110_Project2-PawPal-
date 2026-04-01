import streamlit as st
from datetime import datetime
from pawpal_system import Task, Pet, Owner, Scheduler

st.set_page_config(page_title="PawPal+", page_icon="🐾", layout="centered")
st.title("🐾 PawPal+")

# --- Session state init ---
if "owner" not in st.session_state:
    st.session_state.owner = None
if "pet" not in st.session_state:
    st.session_state.pet = None
if "tasks" not in st.session_state:
    st.session_state.tasks = []

# --- Owner & Pet setup ---
st.subheader("Owner & Pet")
col1, col2, col3 = st.columns(3)
with col1:
    owner_name = st.text_input("Owner name")
with col2:
    pet_name = st.text_input("Pet name")
with col3:
    species = st.selectbox("Species", ["dog", "cat", "other"])

if st.button("Add pet"):
    if owner_name and pet_name:
        owner = Owner(owner_name)
        pet = Pet(pet_name, species)
        owner.add_pet(pet)
        st.session_state.owner = owner
        st.session_state.pet = pet
        st.session_state.tasks = []
        st.success(f"Added {pet_name} for {owner_name}!")
    elif not owner_name:
        st.error("Owner name is empty.")
    else:
        st.error("Pet name is empty.")

if st.session_state.owner:
    st.caption(f"Owner: {st.session_state.owner.name} | Pet: {st.session_state.pet.name}")

st.divider()

# --- Task input ---
st.subheader("Tasks")

col1, col2, col3, col4, col5 = st.columns(5)
with col1:
    task_title = st.text_input("Task title", value="Morning walk")
with col2:
    duration = st.number_input("Duration (min)", min_value=1, max_value=240, value=20)
with col3:
    priority = st.selectbox("Priority", ["low", "medium", "high"], index=2)
with col4:
    frequency = st.selectbox("Frequency", ["daily", "weekly"], index=0)
with col5:
    preferred_time = st.time_input("Preferred time (optional)", value=None)

if st.button("Add task"):
    if st.session_state.pet is None:
        st.error("Add a pet first.")
    else:
        preferred_dt = datetime.combine(datetime.today(), preferred_time) if preferred_time else None
        task = Task(title=task_title, duration=duration, priority=priority, frequency=frequency, preferred_time=preferred_dt)
        st.session_state.pet.add_task(task)
        st.session_state.tasks.append(task)
        st.success(f"Added: {task_title}")

if st.session_state.tasks:
    task_rows = [
        {
            "Title": t.title,
            "Duration (min)": t.duration,
            "Priority": t.priority,
            "Frequency": t.frequency,
            "Preferred Time": t.preferred_time.strftime("%H:%M") if t.preferred_time else "—",
        }
        for t in st.session_state.tasks
    ]
    st.table(task_rows)
else:
    st.info("No tasks yet. Add one above.")

st.divider()

# --- Weekly schedule ---
st.subheader("Weekly Schedule")

if st.button("Generate schedule"):
    if st.session_state.owner is None:
        st.error("Add an owner and pet first.")
    elif not st.session_state.tasks:
        st.warning("No tasks to schedule.")
    else:
        scheduler = Scheduler(st.session_state.owner)
        plan = scheduler.generate_plan()

        for day, day_tasks in plan.items():
            st.markdown(f"**{day.strftime('%A, %b %d')}**")
            if not day_tasks:
                st.caption("No tasks scheduled.")
                continue

            rows = []
            for i, task in enumerate(day_tasks):
                end_dt = task.get_end_time()
                start_str = task.scheduled_time.strftime("%H:%M") if task.scheduled_time else "—"
                end_str = end_dt.strftime("%H:%M") if end_dt else "—"

                # check if this task conflicts with any earlier task on this day
                has_conflict = scheduler.has_conflict(day_tasks[:i], task)
                conflict_flag = "⚠️ Conflict" if has_conflict else ""

                rows.append({
                    "Title": task.title,
                    "Priority": task.priority,
                    "Start": start_str,
                    "End": end_str,
                    "Duration (min)": task.duration,
                    "": conflict_flag,
                })

            if any(r[""] for r in rows):
                st.warning("One or more tasks have scheduling conflicts on this day.")
            else:
                st.success(f"{len(rows)} task(s) scheduled with no conflicts.")

            st.table(rows)