import streamlit as st
import pandas as pd
import plotly.express as px
import os
import requests


st.set_page_config(
    page_title="Data analysis",
    page_icon="📊",
    )

def download_large_file(url, dest_path):
     

    response = requests.get(url, stream=True)
    if response.status_code == 200:
        with open(dest_path, 'wb') as f:
            for chunk in response.iter_content(chunk_size=8192):
                f.write(chunk)
    else:
        raise Exception(f"Failed to download file: {response.status_code}")


@st.cache_resource

# Streamlit
def main():

       # URL tiedostolle (raw URL GitHubista)
    file_url = "https://github.com/Vikke82/St_data_analysis/tree/main/data/openpowerlifting-2024-12-28.csv"
    local_path = "data/openpowerlifting-2024-12-28.csv"
   
    if not os.path.exists(local_path):
        download_large_file(file_url, local_path)
        
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
