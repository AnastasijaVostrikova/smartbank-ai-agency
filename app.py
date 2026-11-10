import streamlit as st
import pandas as pd
from datetime import datetime
import plotly.express as px

st.set_page_config(
    page_title="SmartBank AI Agency",
    layout="wide"
)

# ----------------------------------
# LOGIN
# ----------------------------------

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if not st.session_state.logged_in:

    st.title("🏦 SmartBank AI Agency Login")

    username = st.text_input("Username")
    password = st.text_input(
        "Password",
        type="password"
    )

    if st.button("Login"):

        if username == "boss" and password == "smartbank123":

            st.session_state.logged_in = True
            st.rerun()

        else:
            st.error("Invalid credentials")

    st.stop()

# ----------------------------------
# EMPLOYEES
# ----------------------------------

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

    st.session_state.tasks = pd.DataFrame(
        columns=[
            "Task ID",
            "Timestamp",
            "Assigned By",
            "Agent Name",
            "Task Description",
            "Priority",
            "Status",
            "Output Link",
            "Completion Time"
        ]
    )

# ----------------------------------
# SIDEBAR
# ----------------------------------

st.sidebar.title("🏦 SmartBank AI")

page = st.sidebar.radio(
    "Navigation",
    [
        "Dashboard",
        "Task Assignment",
        "Live Task Board",
        "Employee Overview",
        "Reports",
        "Project Manager Chat",
        "Email Report"
    ]
)

# ----------------------------------
# DASHBOARD
# ----------------------------------

if page == "Dashboard":

    st.title("SmartBank AI Customer Success Agency")

    c1,c2,c3,c4 = st.columns(4)

    c1.metric(
        "Employees",
        8
    )

    c2.metric(
        "Total Tasks",
        len(st.session_state.tasks)
    )

    c3.metric(
        "Completed",
        len(
            st.session_state.tasks[
                st.session_state.tasks.Status=="Completed"
            ]
        )
    )

    c4.metric(
        "In Progress",
        len(
            st.session_state.tasks[
                st.session_state.tasks.Status=="In Progress"
            ]
        )
    )

# ----------------------------------
# TASK ASSIGNMENT
# ----------------------------------

elif page == "Task Assignment":

    st.header("Assign New Task")

    with st.form("assign"):

        description = st.text_area(
            "Task Description"
        )

        employee = st.selectbox(
            "Employee",
            employees
        )

        priority = st.selectbox(
            "Priority",
            ["Low","Medium","High"]
        )

        submit = st.form_submit_button(
            "Assign"
        )

        if submit:

            task = {
                "Task ID":f"T{len(st.session_state.tasks)+1:03d}",
                "Timestamp":datetime.now(),
                "Assigned By":"Boss",
                "Agent Name":employee,
                "Task Description":description,
                "Priority":priority,
                "Status":"Queued",
                "Output Link":"",
                "Completion Time":""
            }

            st.session_state.tasks = pd.concat(
                [
                    st.session_state.tasks,
                    pd.DataFrame([task])
                ]
            )

            st.success("Task Assigned")

# ----------------------------------
# LIVE TASK BOARD
# ----------------------------------

elif page == "Live Task Board":

    st.header("Live Task Board")

    status = st.selectbox(
        "Status Filter",
        [
            "All",
            "Queued",
            "In Progress",
            "Blocked",
            "Completed"
        ]
    )

    df = st.session_state.tasks

    if status != "All":
        df = df[df["Status"] == status]

    st.dataframe(
        df,
        use_container_width=True
    )

# ----------------------------------
# EMPLOYEE OVERVIEW
# ----------------------------------

elif page == "Employee Overview":

    st.header("Employee Overview")

    cols = st.columns(2)

    for i, emp in enumerate(employees):

        with cols[i % 2]:

            st.info(
f"""
### {emp}

Status: Active

Tasks Assigned:
{len(st.session_state.tasks)}

Current State:
Operational
"""
            )

# ----------------------------------
# REPORTS
# ----------------------------------

elif page == "Reports":

    st.header("Agency Reports")

    df = st.session_state.tasks

    if len(df) > 0:

        chart = (
            df["Status"]
            .value_counts()
            .reset_index()
        )

        chart.columns = [
            "Status",
            "Count"
        ]

        fig = px.bar(
            chart,
            x="Status",
            y="Count"
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

# ----------------------------------
# PROJECT MANAGER CHAT
# ----------------------------------

elif page == "Project Manager Chat":

    st.header("Project Manager AI")

    question = st.text_input(
        "Ask a question"
    )

    if question:

        q = question.lower()

        if "completed" in q:

            st.success(
                f"""
Completed Tasks:
{
len(st.session_state.tasks[
st.session_state.tasks.Status=="Completed"
])
}
"""
            )

        elif "employees" in q:

            st.success(
                "There are 8 active employees."
            )

        elif "tasks" in q:

            st.success(
                f"""
Current Tasks:
{len(st.session_state.tasks)}
"""
            )

        else:

            st.info(
                """
Try:

How many completed tasks?

How many employees?

How many tasks?
"""
            )

# ----------------------------------
# EMAIL REPORTS
# ----------------------------------

elif page == "Email Report":

    st.header("Daily Report")

    completed = len(
        st.session_state.tasks[
            st.session_state.tasks.Status=="Completed"
        ]
    )

    body = f"""
SmartBank AI Daily Report

Employees Active: 8

Tasks Completed:
{completed}

Tasks In Progress:
{
len(st.session_state.tasks[
st.session_state.tasks.Status=="In Progress"
])
}

Fraud Reviews:
5

Customer Cases:
12

Loan Reviews:
4

Generated By:
Project Manager AI
"""

    st.code(body)

    st.download_button(
        "Download Report",
        body,
        "Daily_Report.txt"
    )
