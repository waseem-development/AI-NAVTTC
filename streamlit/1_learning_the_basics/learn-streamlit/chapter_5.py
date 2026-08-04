import streamlit as st
import requests

st.title("Live Currency Converter")

amount = st.number_input(
    "Enter the amount in PKR",
    min_value=1
)

url = "https://api.exchangerate-api.com/v4/latest/PKR"

response = requests.get(url)

if response.status_code == 200:

    data = response.json()

    currency = st.selectbox(
        "Convert to:",
        list(data["rates"].keys())
    )

    if st.button("Convert"):

        rate = data["rates"][currency]

        converted = amount * rate

        st.success(
            f"{amount} PKR = {converted:.2f} {currency}"
        )

else:
    st.error("Failed to fetch conversion rate")