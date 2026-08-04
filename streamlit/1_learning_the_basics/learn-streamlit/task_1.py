from datetime import date
from dateutil.relativedelta import relativedelta
import streamlit as st


st.title("Age Calculator")
st.subheader("Using Streamlit")

today = date.today()

st.write(f"# *`Today\'s Date:`* {today}")

dob = st.date_input(
    "Select your DoB",
    value=date(2000, 1, 1),
    min_value=date(1900, 1, 1),
    max_value=today
)
st.write(f"# *`Date of Birth:`* {dob}")


age = relativedelta(today, dob)

st.write(
    f"## 🎂 You are **{age.years} years, {age.months} months, and {age.days} days** old."
)