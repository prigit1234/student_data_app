#streamlit app that anlyzes student marks and generate insights
#content of csv file=
#upload a csv file, display the dataset ,show avg marks,highest marks,lowest marks,filter data by subject,display a bar chart of student marks
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("📊 Student Marks Analysis App")

# Upload CSV file
uploaded_file = st.file_uploader("Upload CSV file", type=["csv"])

if uploaded_file is not None:
    # Read CSV
    df = pd.read_csv(uploaded_file)

    st.subheader("📄 Dataset")
    st.dataframe(df)

    # Basic statistics
    st.subheader("📈 Marks Insights")

    avg_marks = df["Marks"].mean()
    max_marks = df["Marks"].max()
    min_marks = df["Marks"].min()

    col1, col2, col3 = st.columns(3)
    col1.metric("Average Marks", round(avg_marks, 2))
    col2.metric("Highest Marks", max_marks)
    col3.metric("Lowest Marks", min_marks)

    # Filter by subject
    st.subheader("📚 Filter by Subject")
    subjects = df["Subject"].unique()
    selected_subject = st.selectbox("Select Subject", subjects)

    filtered_df = df[df["Subject"] == selected_subject]
    st.dataframe(filtered_df)

    # Bar chart
    st.subheader("📊 Student Marks Bar Chart")
    fig, ax = plt.subplots()
    ax.bar(filtered_df["Name"], filtered_df["Marks"])
    ax.set_xlabel("Name")
    ax.set_ylabel("Marks")
    ax.set_title(f"Marks in {selected_subject}")
    plt.xticks(rotation=45)

    st.pyplot(fig)

else:
    st.info("Please upload a CSV file to continue.")
