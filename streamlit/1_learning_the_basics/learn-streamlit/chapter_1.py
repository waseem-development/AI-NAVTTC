import streamlit as st

st.title("Hello World 👋")
st.subheader("Brewed with Streamlit")
st.text("Welcome to your first Streamlit app")
st.write("Choose your favorite variety of chai")

chai = st.selectbox(
    "Your Favorite Chai:",
    ["Select", "Masala Chai", "Mint Chai", "Lemon Chai", "Adrak Chai"]
)

if chai == "Select":
    st.warning("Please select a chai.")
else:
    st.success(f"You selected: {chai}")