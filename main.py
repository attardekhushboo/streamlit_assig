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
        
        # Log the data types and columns for debugging
        st.write("### Data Types", df.dtypes)
        
        # Ensure only numeric columns are used for visualizations
        numeric_columns = df.select_dtypes(include=["number"]).columns.tolist()
        st.write(f"### Available Numeric Columns: {numeric_columns}")
        
        if numeric_columns:
            st.write("### Descriptive Statistics")
            st.write(df.describe())  # Statistics for numeric columns

            # Choose a Chart Type
            chart_type = st.selectbox("Chart Type", ["Line Chart", "Bar Chart", "Histogram"])

            if chart_type == "Line Chart":
                if len(numeric_columns) >= 2:  # Ensure there are enough numeric columns for a line chart
                    st.write("### Line Chart")
                    st.line_chart(df[numeric_columns])  # Plot the numeric columns as a line chart
                else:
                    st.warning("Not enough numeric data for a line chart")

            elif chart_type == "Bar Chart":
                bar_column = st.selectbox("Select Column for Bar Chart", df.columns)
                if bar_column:
                    # Ensure the column is categorical or has a limited number of unique values
                    bar_data = df[bar_column].value_counts()
                    st.write("### Bar Chart")
                    st.bar_chart(bar_data)  # Plot bar chart for selected column

            elif chart_type == "Histogram":
                column = st.selectbox("Select Numeric Column for Histogram", numeric_columns)
                if column:
                    st.write(f"### Histogram for {column}")
                    fig, ax = plt.subplots()
                    sns.histplot(df[column], kde=True, ax=ax)
                    st.pyplot(fig)  # Show histogram with KDE plot
        else:
            st.warning("No numeric columns available for visualizations.")
    except Exception as e:
        st.error(f"Error reading file: {e}")  # Handle errors and show a message to the user
else:
    st.info("Please upload a CSV file.")
