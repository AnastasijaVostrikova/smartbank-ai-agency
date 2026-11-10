import streamlit as st

st.set_page_config(page_title="SmartBank AI Agency")

st.title("SmartBank AI Customer Success Agency")

st.write("Boss Command Center")

st.subheader("AI Employees")

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

for employee in employees:
    st.write("✅", employee)
