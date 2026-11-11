import streamlit as st
import pandas as pd
from datetime import datetime
import plotly.express as px

# =====================================================
# PAGE CONFIG
# =====================================================

st.set_page_config(
    page_title="SmartBank AI Agency",
    page_icon="🏦",
    layout="wide"
)

# =====================================================
# STYLING
# =====================================================

st.markdown("""
<style>

.stApp{
    background: linear-gradient(135deg,#f7fbff,#e9f5ff);
}

h1,h2,h3{
    color:#003366;
}

[data-testid="stSidebar"]{
    background:linear-gradient(180deg,#003366,#0059b3);
}

[data-testid="stSidebar"] *{
    color:white;
}

.stButton > button{
    background:linear-gradient(90deg,#0078D4,#00AEEF);
    color:white;
    border:none;
    border-radius:12px;
    font-weight:bold;
}

div[data-testid="metric-container"]{
    background:white;
    border-radius:15px;
    border:1px solid #d9eaf7;
    padding:15px;
    box-shadow:0 3px 8px rgba(0,0,0,0.08);
}

</style>
""", unsafe_allow_html=True)

# =====================================================
# LOGIN
# =====================================================

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if not st.session_state.logged_in:

    st.title("🏦 SmartBank AI Agency")
    st.subheader("Boss Command Center Login")

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

# =====================================================
# DATA
# =====================================================

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

partner_banks = pd.DataFrame([
    {
        "Bank": "Swedbank",
        "Country": "Latvia",
        "Open Requests": 3,
        "Priority": "High"
    },
    {
        "Bank": "SEB Bank",
        "Country": "Latvia",
        "Open Requests": 2,
        "Priority": "Medium"
    },
    {
        "Bank": "Indexo Bank",
        "Country": "Latvia",
        "Open Requests": 1,
        "Priority": "Low"
    },
    {
        "Bank": "Luminor",
        "Country": "Latvia",
        "Open Requests": 4,
        "Priority": "High"
    }
])

if "tasks" not in st.session_state:

    st.session_state.tasks = pd.DataFrame([
        {
            "Task ID": "T001",
            "Timestamp": "2026-11-10",
            "Assigned By": "Boss",
            "Agent Name": "Fraud & Security Monitor",
            "Task Description": "Analyze suspicious transactions",
            "Priority": "High",
            "Status": "Completed",
            "Output Link": "fraud_report.pdf",
            "Completion Time": "25 min"
        },
        {
            "Task ID": "T002",
            "Timestamp": "2026-11-10",
            "Assigned By": "Boss",
            "Agent Name": "Customer Onboarding Specialist",
            "Task Description": "Review new customer applications",
            "Priority": "Medium",
            "Status": "In Progress",
            "Output Link": "",
            "Completion Time": ""
        }
    ])

# =====================================================
# SIDEBAR
# =====================================================

st.sidebar.title("🏦 SmartBank AI")

page = st.sidebar.radio(
    "Navigation",
    [
        "Dashboard",
        "Executive Overview",
        "Task Assignment",
        "Live Task Board",
        "Employee Overview",
        "Employee Performance",
        "Reports",
        "Project Manager Chat",
        "External Bank Assistance",
        "Email Report",
        "Audit Log"
    ]
)

# =====================================================
# DASHBOARD
# =====================================================

if page == "Dashboard":

    st.title("🏦 SmartBank AI Customer Success Agency")

    st.markdown("""
### Autonomous Banking Operations & Partner Bank Support Platform

✅ Customer Onboarding

✅ Fraud Monitoring

✅ Product Recommendations

✅ Loan Assistance

✅ Customer Retention

✅ External Bank Assistance
""")

    c1, c2, c3, c4 = st.columns(4)

    c1.metric("Employees", 8)

    c2.metric(
        "Total Tasks",
        len(st.session_state.tasks)
    )

    c3.metric(
        "Completed",
        len(
            st.session_state.tasks[
                st.session_state.tasks["Status"] == "Completed"
            ]
        )
    )

    c4.metric(
        "In Progress",
        len(
            st.session_state.tasks[
                st.session_state.tasks["Status"] == "In Progress"
            ]
        )
    )

    st.divider()

    st.subheader("🏦 Banking Network Status")

    b1, b2, b3, b4 = st.columns(4)

    b1.metric("Partner Banks", 4)

    b2.metric(
        "Open Requests",
        partner_banks["Open Requests"].sum()
    )

    b3.metric(
        "Active Assistance Cases",
        6
    )

    b4.metric(
        "Resolved Today",
        11
    )

# =====================================================
# EXECUTIVE OVERVIEW
# =====================================================

elif page == "Executive Overview":

    st.title("📈 Executive Overview")

    st.success("""
Today's Operations Summary

✅ 42 Tasks Processed

✅ 15 Customer Cases Closed

✅ 5 Fraud Alerts Reviewed

✅ 4 Loan Reviews Completed

✅ 3 Churn Risks Identified

✅ 4 Partner Banks Monitored

✅ 100% Employee Availability
""")

# =====================================================
# TASK ASSIGNMENT
# =====================================================

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
            ["Low", "Medium", "High"]
        )

        submit = st.form_submit_button("Assign")

        if submit:

            task = {
                "Task ID": f"T{len(st.session_state.tasks)+1:03d}",
                "Timestamp": datetime.now(),
                "Assigned By": "Boss",
                "Agent Name": employee,
                "Task Description": description,
                "Priority": priority,
                "Status": "Queued",
                "Output Link": "",
                "Completion Time": ""
            }

            st.session_state.tasks = pd.concat(
                [
                    st.session_state.tasks,
                    pd.DataFrame([task])
                ],
                ignore_index=True
            )

            st.success("Task Assigned")

# =====================================================
# LIVE TASK BOARD
# =====================================================

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

    df = st.session_state.tasks.copy()

    if status != "All":
        df = df[df["Status"] == status]

    st.dataframe(
        df,
        use_container_width=True
    )

# =====================================================
# EMPLOYEE OVERVIEW
# =====================================================

elif page == "Employee Overview":

    st.header("Employee Overview")

    cols = st.columns(2)

    for i, emp in enumerate(employees):

        with cols[i % 2]:

            st.info(f"""
### {emp}

✅ Status: Active

⚡ Availability: Online

📋 Assigned Tasks: {len(st.session_state.tasks)}

📈 Productivity Score: 95%

🏦 Department: Banking Operations
""")

# =====================================================
# EMPLOYEE PERFORMANCE
# =====================================================

elif page == "Employee Performance":

    st.header("🏆 Employee Performance")

    performance = pd.DataFrame({
        "Employee": employees,
        "Score": [98,95,93,97,91,89,94,92]
    })

    st.bar_chart(
        performance.set_index("Employee")
    )

# =====================================================
# REPORTS
# =====================================================

elif page == "Reports":

    st.header("📊 Agency Reports")

    df = st.session_state.tasks

    if len(df) > 0:

        chart = (
            df["Status"]
            .value_counts()
            .reset_index()
        )

        chart.columns = ["Status", "Count"]

        fig = px.bar(
            chart,
            x="Status",
            y="Count",
            color="Status"
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

        csv = df.to_csv(index=False)

        st.download_button(
            "Download Report",
            csv,
            "SmartBank_Report.csv"
        )

# =====================================================
# PROJECT MANAGER CHAT
# =====================================================

elif page == "Project Manager Chat":

    st.header("🤖 Project Manager AI")

    question = st.text_input(
        "Ask a question"
    )

    if question:

        q = question.lower()

        if "completed" in q:

            st.success(
                f"Completed tasks: {len(st.session_state.tasks[st.session_state.tasks.Status == 'Completed'])}"
            )

        elif "employees" in q:

            st.success(
                "There are 8 active employees."
            )

        elif "tasks" in q:

            st.success(
                f"Current tasks: {len(st.session_state.tasks)}"
            )

        elif "swedbank" in q:

            st.success(
                "Swedbank currently has 3 open support requests."
            )

        elif "seb" in q:

            st.success(
                "SEB Bank currently has 2 open support requests."
            )

        elif "indexo" in q:

            st.success(
                "Indexo Bank currently has 1 open support request."
            )

        elif "luminor" in q:

            st.success(
                "Luminor currently has 4 open support requests."
            )

        elif "banks" in q or "partner" in q:

            st.success(
                "SmartBank AI currently supports Swedbank, SEB Bank, Indexo Bank and Luminor."
            )

        elif "fraud" in q:

            st.success(
                "Fraud Monitor reviewed 5 alerts today."
            )

        elif "loan" in q:

            st.success(
                "Loan Assistant reviewed 4 applications today."
            )

        else:

            st.info(
                "Try asking about tasks, employees, fraud, loans or partner banks."
            )

# =====================================================
# EXTERNAL BANK ASSISTANCE
# =====================================================

elif page == "External Bank Assistance":

    st.title("🤝 External Bank Assistance Center")

    st.success(
        "SmartBank AI supports other banks when assistance is required."
    )

    st.dataframe(
        partner_banks,
        use_container_width=True
    )

    selected_bank = st.selectbox(
        "Select Bank",
        partner_banks["Bank"]
    )

    support_type = st.selectbox(
        "Support Type",
        [
            "Customer Support",
            "Fraud Monitoring",
            "Loan Assessment",
            "Compliance Review",
            "Financial Advisory"
        ]
    )

    if st.button("Provide Assistance"):

        st.success(
            f"""
Support Assigned

Bank: {selected_bank}

Service: {support_type}

Status: In Progress
"""
        )

# =====================================================
# EMAIL REPORT
# =====================================================

elif page == "Email Report":

    st.header("Daily Report")

    completed = len(
        st.session_state.tasks[
            st.session_state.tasks.Status == "Completed"
        ]
    )

    body = f"""
SmartBank AI Daily Report

Employees Active: 8

Tasks Completed: {completed}

Tasks In Progress:
{len(st.session_state.tasks[st.session_state.tasks.Status=='In Progress'])}

Fraud Reviews: 5

Customer Cases: 12

Loan Reviews: 4

Generated By:
Project Manager AI
"""

    st.code(body)

    st.download_button(
        "Download Report",
        body,
        "Daily_Report.txt"
    )

# =====================================================
# AUDIT LOG
# =====================================================

elif page == "Audit Log":

    st.header("📜 Audit Log")

    st.dataframe(
        st.session_state.tasks,
        use_container_width=True
    )
