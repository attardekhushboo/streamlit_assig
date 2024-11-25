import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.title("CSV Data Visualization App")

uploaded_file = st.file_uploader("Upload your CSV file", type=["csv"])
if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.write("### Data Preview", df.head())

    st.write("### Descriptive Statistics")
    st.write(df.describe())

    st.write("### Choose a Chart Type")
    chart_type = st.selectbox("Chart Type", ["Line Chart", "Bar Chart", "Histogram"])

    if chart_type == "Line Chart":
        st.line_chart(df)
    elif chart_type == "Bar Chart":
        st.bar_chart(df)
    elif chart_type == "Histogram":
        column = st.selectbox("Select Column", df.columns)
        fig, ax = plt.subplots()
        sns.histplot(df[column], kde=True, ax=ax)
        st.pyplot(fig)
