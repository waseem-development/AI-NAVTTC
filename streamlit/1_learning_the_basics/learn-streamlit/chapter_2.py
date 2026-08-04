import streamlit as st

st.title("Chapter 2")

# Widgets

if st.button("Make Chai"): # st.button() is special because it returns a Boolean value. When you click the button: It returns True only for that run. On all other runs, it returns False.
    st.success("Your chai is being brewed")

add_masala = st.checkbox("Add Masala")

if add_masala:
    st.write("# Added *Masala* to your chai")
tea_type = st.radio("Pick your Chai base", ["Milk", "Water", "Almond Milk"])
st.write(f"# Selected base *{tea_type}*")

flavour = st.selectbox("Choose flavour", ["Select", "Masala Chai", "Mint Chai", "Lemon Chai", "Adrak Chai"])

if flavour == "Select":
    st.warning(f"Please select a flavour")
else:     
    st.success(f"Selected {flavour} flavour")

sugar = st.slider("Sugar Level (spoon)", 0, 5, 2)
st.write(f"You selected {sugar} sugar level")

cups = st.number_input("How many cups", min_value=1, max_value=10, step=1)
st.write(f"You selected {cups} cups")

name = st.text_input("Enter your name")
if name: 
    st.write(f"Your name is: {name}")

dob = st.date_input("Select your DoB")
st.write(f"Selected Sugar Level {dob}")
