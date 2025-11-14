# streamlit_emi_calculator.py
# Streamlit EMI calculator + amortization schedule
# Run: streamlit run streamlit_emi_calculator.py

import streamlit as st
import pandas as pd
import numpy as np
import io
import matplotlib.pyplot as plt

st.set_page_config(page_title="EMI Calculator", layout="centered")

st.title("EMI Calculator")

# Inputs
col1, col2 = st.columns(2)
with col1:
    principal = st.number_input("Loan amount (₹)", min_value=0.0, value=100000.0, step=1000.0, format="%.2f")
    annual_rate = st.number_input("Annual rate of interest (%)", min_value=0.0, value=8.25, step=0.01, format="%.4f")
with col2:
    tenure_months = st.number_input("Tenure (months)", min_value=1, value=36, step=1)
    starting_month = st.date_input("Schedule start date (optional)", value=None)

# Calculations
r = annual_rate / 100.0 / 12.0 # monthly interest rate
n = int(tenure_months)

if principal <= 0 or n <= 0:
    st.error("Enter positive loan amount and tenure.")
    st.stop()

# EMI formula
if r == 0:
    emi = principal / n
else:
    emi = principal * r * (1 + r) ** n / ((1 + r) ** n - 1)

# Build amortization schedule
schedule = []
outstanding = principal
total_interest = 0.0

for m in range(1, n + 1):
    interest = outstanding * r
    principal_component = emi - interest
    # handle final rounding to avoid tiny negative outstanding due to float
    if m == n:
        principal_component = outstanding
        emi_this = principal_component + interest
        closing = 0.0
    else:
        emi_this = emi
        closing = outstanding - principal_component
        # protect against negative zero rounding
        if closing < 1e-8:
            closing = 0.0

    schedule.append(
        {
            "Month": m,
            "Opening Balance": outstanding,
            "Interest": interest,
            "Principal": principal_component,
            "EMI": emi_this,
            "Closing Balance": closing,
        }
    )

    outstanding = closing
    total_interest += interest

df = pd.DataFrame(schedule)
# human-friendly formatting columns for display
display_df = df.copy()
fmt_cols = ["Opening Balance", "Interest", "Principal", "EMI", "Closing Balance"]
for c in fmt_cols:
    display_df[c] = display_df[c].map(lambda x: f"₹{x:,.2f}")

total_payment = emi * n
summary_col1, summary_col2, summary_col3 = st.columns(3)
summary_col1.metric("Monthly EMI (approx)", f"₹{emi:,.2f}")
summary_col2.metric("Total Interest Payable", f"₹{total_interest:,.2f}")
summary_col3.metric("Total Payment (Principal + Interest)", f"₹{total_payment:,.2f}")

st.markdown("### Amortization schedule")
st.dataframe(display_df, use_container_width=True)

# Download CSV
csv = df.to_csv(index=False)
b = io.BytesIO()
b.write(csv.encode())
b.seek(0)
st.download_button(
    label="Download schedule as CSV",
    data=b,
    file_name="amortization_schedule.csv",
    mime="text/csv",
)
