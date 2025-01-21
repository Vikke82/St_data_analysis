import streamlit as st
import pandas as pd
import plotly.express as px
from scipy.stats import norm
import scipy.stats as stats
import numpy as np

st.set_page_config(page_title="Descriptive Statistics", page_icon="bar-chart")

st.markdown('''In statistics, a central tendency (or measure of central tendency) is a central or typical value for a probability distribution.[1]

Colloquially, measures of central tendency are often called averages. The term central tendency dates from the late 1920s.[2]

The most common measures of central tendency are the arithmetic mean, the median, and the mode. A middle tendency can be calculated for either a finite set of values or for a theoretical distribution, such as the normal distribution. Occasionally authors use central tendency to denote "the tendency of quantitative data to cluster around some central value."[2][3]

The central tendency of a distribution is typically contrasted with its dispersion or variability; dispersion and central tendency are the often characterized properties of distributions. Analysis may judge whether data has a strong or a weak central tendency based on its dispersion.
https://en.wikipedia.org/wiki/Central_tendency
            ''')

if 'data' in st.session_state:
        
        data = st.session_state['data']
        column = "TotalKg"
        # Plot data
    
        st.write(f"Visualizing descriptive statistics data for column: {column}")
         # Plot data
        df2 = pd.DataFrame(data, columns=[column]).dropna()
        line_plot = px.line(df2, x=df2.index, y=column, title=f"Line Plot of {column}")
        st.plotly_chart(line_plot, use_container_width=True)
        
        # Calculate descriptive statistics
        desc_stats = data[column].describe().to_frame(name='Value')
        
        # Display descriptive statistics
        st.write("Descriptive Statistics")
        st.table(desc_stats)
        
        st.markdown('''Variance and Standard Deviation:
        Variance: Measures how much the data values deviate from the mean.
        Standard Deviation: Square root of the variance''')

        bin_size = 100  # Number of bins for the histogram
        # Histogram
        st.write(f"Histogram of {column}")
        histogram = px.histogram(data, x=column, nbins=bin_size, title=f"Histogram of {column}")

        # Compute histogram data manually
        counts, bins = np.histogram(data[column], bins=np.arange(bin_size), density=True)  # Match the bins and normalization in plotly
        max_value = np.max(counts[0])

        # Compute ideal standard normal distribution
        x = np.linspace(np.min(data[column]), np.max(data[column]), 500)  # X-axis range for the normal curve
        y = norm.pdf(x, loc=np.mean(data[column]), scale=np.std(data[column]))*max_value # Y-axis values for the normal curve

        

        histogram.add_scatter(x=x, y=y, mode='lines', name='Normal Distribution')
        st.plotly_chart(histogram, use_container_width=True)

        st.markdown('''Testing is the data normally distributed? 
                    https://en.wikipedia.org/wiki/Shapiro%E2%80%93Wilk_test
                    ''')
        # Shapiro-Wilk test
        st.write("Shapiro-Wilk Test")
        shapiro_test = stats.shapiro(data[column].dropna())
        
        st.write(f"Test Statistic: {shapiro_test.statistic}")
        st.write(f"P-value: {shapiro_test.pvalue}")
        st.write(f"Is the data normally distributed? {shapiro_test.pvalue > 0.05}")

        st.write("Skewness Test")
        skew_test = stats.skewtest(data[column].dropna())

        st.write(f"Test Statistic: {skew_test.statistic}")
        st.write(f"P-value: {skew_test.pvalue}")
        st.write(f"Is the data skewed? {skew_test.pvalue < 0.05}")
        
        # Box Plot
        st.write(f"Box Plot of {column}")
        box_plot = px.box(data, y=column, title=f"Box Plot of {column}")
        st.plotly_chart(box_plot, use_container_width=True)

st.markdown('''Variance and Standard Deviation:
Variance: Measures how much the data values deviate from the mean.
Standard Deviation: Square root of the variance''')