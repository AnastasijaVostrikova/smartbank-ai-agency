import streamlit as st
import pandas as pd
from datetime import datetime

st.set_page_config(
    page_title="SmartBank AI Agency",
    layout="wide"
)

# -----------------------------------
# Sample data
# -----------------------------------

employees = [
    "Project Manager",
    "Customer Onboarding Specialist",
    "Product Recommendation Advisor",
    "Fraud & Security Monitor",
    "Financial Wellness Coach",
    "Loan & Credit Assistant",
    "Customer Support Triage",
    "Customer Retention Strategist"
]

if "tasks" not in st.session_state:
    st.session_state.tasks = pd.DataFrame([
        {
            "Task ID": "T001",
            "Agent Name": "Customer Onboarding Specialist",
            "Task Description": "Review new account applications",
            "Priority": "High",
            "Status": "Completed",
            "Timestamp": "2026-11-10"
        },
        {
            "Task ID": "T002",
            "Agent Name": "Fraud & Security Monitor",
            "Task Description": "Analyze suspicious transactions",
            "Priority": "High",
            "Status": "In Progress",
            "Timestamp": "2026-11-10"
        }
    ])

# -----------------------------------
# Sidebar
# -----------------------------------

st.sidebar.title("SmartBank AI Agency")

page = st.sidebar.radio(
    "Navigation",
    [
        "Dashboard",
        "Task Assignment",
        "Live Task Board",
        "Employee Overview",
        "Reports",
        "Project Manager Chat"
    ]
)

# -----------------------------------
# Dashboard
# -----------------------------------

if page == "Dashboard":

    st.title("🏦 SmartBank AI Customer Success Agency")

    st.subheader("Boss Command Center")

    col1, col2, col3, col4 = st.columns(4)

    col1.metric(
        "Total Employees",
        "8"
    )

    col2.metric(
        "Active Tasks",
        len(st.session_state.tasks)
    )

    col3.metric(
        "Completed Tasks",
        len(
            st.session_state.tasks[
                st.session_state.tasks["Status"] == "Completed"
            ]
        )
    )

    col4.metric(
        "In Progress",
        len(
            st.session_state.tasks[
                st.session_state.tasks["Status"] == "In Progress"
            ]
        )
    )

    st.divider()

    st.subheader("AI Employees")

    for emp in employees:
        st.success(emp)

# -----------------------------------
# Task Assignment
# -----------------------------------

elif page == "Task Assignment":

    st.title("📌 Assign New Task")

    with st.form("task_form"):

        task_description = st.text_area(
            "Task Description"
        )

        employee = st.selectbox(
            "Assign To",
            employees
        )

        priority = st.selectbox(
            "Priority",
            ["Low", "Medium", "High"]
        )

        submit = st.form_submit_button(
            "Assign Task"
        )

        if submit:

            task_id = f"T{len(st.session_state.tasks)+1:03d}"

            new_task = pd.DataFrame([{
                "Task ID": task_id,
                "Agent Name": employee,
                "Task Description": task_description,
                "Priority": priority,
                "Status": "Queued",
                "Timestamp": datetime.now().strftime("%Y-%m-%d")
            }])

            st.session_state.tasks = pd.concat(
                [st.session_state.tasks, new_task],
                ignore_index=True
            )

            st.success("Task Assigned")

# -----------------------------------
# Live Task Board
# -----------------------------------

elif page == "Live Task Board":

    st.title("📋 Live Task Board")

    status_filter = st.selectbox(
        "Filter by Status",
        [
            "All",
            "Queued",
            "In Progress",
            "Completed",
            "Blocked"
        ]
    )

    data = st.session_state.tasks

    if status_filter != "All":
        data = data[data["Status"] == status_filter]

    st.dataframe(
        data,
        use_container_width=True
    )

# -----------------------------------
# Employee Overview
# -----------------------------------

elif page == "Employee Overview":

    st.title("👥 Employee Overview")

    cols = st.columns(2)

    for i, emp in enumerate(employees):

        with cols[i % 2]:

            st.info(
                f"""
### {emp}

Status: Active

Tasks Today: {len(st.session_state.tasks)}

Availability: Online
"""
            )

# -----------------------------------
# Reports
# -----------------------------------

elif page == "Reports":

    st.title("📊 Agency Reports")

    df = st.session_state.tasks

    st.subheader("Task Status Summary")

    status_counts = (
        df["Status"]
        .value_counts()
        .reset_index()
    )

    status_counts.columns = [
        "Status",
        "Count"
    ]

    st.bar_chart(
        status_counts.set_index("Status")
    )

    st.subheader("Tasks by Employee")

    emp_counts = (
        df["Agent Name"]
        .value_counts()
        .reset_index()
    )

    emp_counts.columns = [
        "Agent",
        "Tasks"
    ]

    st.bar_chart(
        emp_counts.set_index("Agent")
    )

# -----------------------------------
# Project Manager Chat
# -----------------------------------

elif page == "Project Manager Chat":

    st.title("🤖 Project Manager AI")

    question = st.text_input(
        "Ask a question"
    )

    if question:

        q = question.lower()

        if "completed" in q:

            count = len(
                st.session_state.tasks[
                    st.session_state.tasks["Status"] == "Completed"
                ]
            )

            st.success(
                f"{count} tasks are completed."
            )

        elif "in progress" in q:

            count = len(
                st.session_state.tasks[
                    st.session_state.tasks["Status"] == "In Progress"
                ]
            )

            st.success(
                f"{count} tasks are currently in progress."
            )

        elif "employees" in q:

            st.success(
                f"There are {len(employees)} AI employees."
            )

        elif "blocked" in q:

            blocked = st.session_state.tasks[
                st.session_state.tasks["Status"] == "Blocked"
            ]

            if len(blocked) == 0:
                st.success("No blocked tasks.")
            else:
                st.dataframe(blocked)

        else:

            st.info(
                """
I can answer:

• How many tasks are completed?
• How many tasks are in progress?
• Are there blocked tasks?
• How many employees are there?
"""
            )
