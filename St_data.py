import streamlit as st
import pandas as pd
import plotly.express as px


st.set_page_config(
    page_title="Data analysis",
    page_icon="📊",
    )

@st.cache_resource

# Streamlit
def main():
   

    st.sidebar.success("Sidebar")

    st.title("Interactive Data Viewer for MySQL")

    st.markdown(
    """
    This app shows how to interact with data from a MySQL database. This app runs in Virtual Machine (VM) 
    and connects to a MySQL database (running on the same VM).
    The data is fetched from the database and displayed in a table. 
    You can select a column to visualize and see the descriptive statistics, line plot, histogram, and box plot of the selected column.
    """
    )

    data = pd.read_csv(r"data\openpowerlifting-2024-12-28.csv", low_memory=False)
    st.write(data.columns)
    st.session_state['data'] = data  # Store in session state





if __name__ == "__main__":
    main()
