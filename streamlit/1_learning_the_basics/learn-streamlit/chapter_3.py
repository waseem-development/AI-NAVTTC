import streamlit as st

st.title("Chai Taste Poll")

col1, col2 = st.columns(2)
with col1:
    st.header("Masala Chai")
    st.image("./images/chilli tea.jpg", width=300)
    vote1 = st.button("Vote Masala Chai")

with col2:
    st.header("Adrak Chai")
    st.image("./images/Ginger Tea.jpg", width=300)
    vote2 = st.button("Vote Adrak Chai")

if vote1:
    st.success("Thanks for voting Masala Chai")
elif vote2: 
    st.success("Thanks for voting Adrak Chai")
else: 
    st.error("You did not select a chai")

name = st.sidebar.text_input("Enter your name: ")
tea = st.sidebar.selectbox(
    "Select Your Chai:",
    ["Select", "Masala", "Mint", "Lemon", "Adrak"]
)

if tea == "Select":
    st.warning("Please select a chai.")
else:
    st.success(f"You selected: {tea}")

st.write(f"### Welcome `{name}` and your `{tea} Chai` is getting ready")

with st.expander("Show chai making Instructions"):
    st.write("""
    1. Boil Water with Tea leaves
    2. Add milk and spices
    3. Serve
    """)