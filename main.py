import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.title("CSV Data Visualization App")

# Upload the file
uploaded_file = st.file_uploader("Upload your CSV file", type=["csv"])

if uploaded_file:
    try:
        # Read and display the dataset
        df = pd.read_csv(uploaded_file)
        st.write("### Data Preview", df.head())  # Show first 5 rows
        st.write("### Dataset Shape", df.shape)  # Show the shape (rows, columns)
        
        # Ensure only numeric columns are used for visualizations
        numeric_columns = df.select_dtypes(include=["number"]).columns.tolist()
        st.write(f"### Available Numeric Columns: {numeric_columns}")
        
        if numeric_columns:
            st.write("### Descriptive Statistics")
            st.write(df.describe())  # Statistics for numeric columns

            # Choose a Chart Type
            chart_type = st.selectbox("Chart Type", ["Line Chart", "Bar Chart", "Histogram"])

            if chart_type == "Line Chart":
                if len(numeric_columns) >= 2:  # Make sure there are enough columns for a line chart
                    st.line_chart(df[numeric_columns])
                else:
                    st.warning("Not enough numeric data for a line chart")

            elif chart_type == "Bar Chart":
                bar_column = st.selectbox("Select Column for Bar Chart", df.columns)
                if bar_column:
                    bar_data = df[bar_column].value_counts()
                    st.bar_chart(bar_data)

            elif chart_type == "Histogram":
                column = st.selectbox("Select Numeric Column for Histogram", numeric_columns)
                if column:
                    fig, ax = plt.subplots()
                    sns.histplot(df[column], kde=True, ax=ax)
                    st.pyplot(fig)
