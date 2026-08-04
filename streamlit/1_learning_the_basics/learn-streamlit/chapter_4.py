import streamlit as st
import pandas as pd

st.title(" Dashboard")

file = st.file_uploader("Upload your SCV file", type=["csv"])

if not file:
    st.warning("### Please upload a file")
else: 
    df = pd.read_csv("./datasets/1_career_dataset_cleaned.csv")
    st.subheader("Data Preview")
    st.dataframe(df)

if file:
    st.subheader("Statistical Summary")
    st.write(df.describe())
if file: 
    df["Certifications"].unique()
    selected_certification = st.selectbox(
    "Filter By Certifications",
    df["Certifications"].unique()
    )
    filtered_data = df[df["Certifications"] == selected_certification]
    st.dataframe(filtered_data)

