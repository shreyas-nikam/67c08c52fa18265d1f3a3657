import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(page_title="US Banks' Stress Testing Practices Visualizer", layout="wide")
st.sidebar.image("https://www.quantuniversity.com/assets/img/logo5.jpg")
st.sidebar.divider()
st.title("US Banks' Stress Testing Practices Visualizer")
st.divider()

# Introduction and Context
st.markdown("""
    ## Understanding US Banks' Stress Testing Practices

    This application provides an interactive visualization of stress testing practices at major US banks, 
    including Citigroup, Bank of America, and JP Morgan Chase. 
    Stress testing is a critical component of risk management in financial institutions, 
    designed to evaluate the potential impact of adverse economic scenarios on a bank's financial health.

    **Based on the 'US Banks' Stress Testing Practices' document, this tool helps you explore:**
    - Different types of stress tests conducted by banks.
    - The frequency and focus of stress testing activities.
    - Potential impacts of various stress scenarios.

    **Learning Outcomes:**
    - Understand key insights into US banks' stress testing practices.
    - Learn to visualize financial data using Streamlit.
    - Explore data preprocessing and interactive data exploration.

    **Dataset**: This application uses a synthetic dataset designed to mimic real-world stress testing data. 
    This dataset includes information on banks, types of stress tests, frequency, and hypothetical impact metrics.
""")

st.divider()

# Synthetic Data Generation - Self-sufficient dataset
@st.cache_data
def generate_synthetic_data():
    banks = ['Citigroup', 'Bank of America', 'JP Morgan Chase']
    stress_test_types = ['Credit Risk', 'Market Risk', 'Operational Risk', 'Liquidity Risk']
    years = range(2018, 2024)
    data = []
    for bank in banks:
        for year in years:
            for test_type in stress_test_types:
                frequency = np.random.randint(1, 13) # Monthly to Yearly frequency
                impact_percentage = np.random.uniform(0.01, 0.10) # Impact as percentage of capital
                data.append({
                    'Bank': bank,
                    'Year': year,
                    'Stress Test Type': test_type,
                    'Frequency (per year)': frequency,
                    'Impact (% of Capital)': impact_percentage
                })
    return pd.DataFrame(data)

df = generate_synthetic_data()

# User Interaction Widgets
st.sidebar.header("Filter Data")
selected_banks = st.sidebar.multiselect("Select Banks", options=df['Bank'].unique(), default=df['Bank'].unique())
selected_stress_types = st.sidebar.multiselect("Select Stress Test Types", options=df['Stress Test Type'].unique(), default=df['Stress Test Type'].unique())
selected_years = st.sidebar.slider("Select Year Range", min_value=min(df['Year']), max_value=max(df['Year']), value=(min(df['Year']), max(df['Year'])))

# Filter DataFrame based on user selections
filtered_df = df[
    (df['Bank'].isin(selected_banks)) &
    (df['Stress Test Type'].isin(selected_stress_types)) &
    (df['Year'] >= selected_years[0]) &
    (df['Year'] <= selected_years[1])
]

st.subheader("Interactive Visualizations of Stress Testing Practices")

# Visualization 1: Bar Chart - Frequency of Stress Tests by Bank and Type
st.markdown("### Stress Test Frequency by Bank and Type")
st.markdown("""
    This bar chart illustrates the frequency of different types of stress tests conducted by each bank. 
    Frequency is measured as the number of times a particular stress test is conducted per year. 
    Higher bars indicate more frequent stress testing, suggesting a greater focus on that specific risk type by the bank.
""")
frequency_df = filtered_df.groupby(['Bank', 'Stress Test Type'])['Frequency (per year)'].sum().unstack()
if not frequency_df.empty:
    st.bar_chart(frequency_df)
else:
    st.warning("No data to display for the selected filters in Frequency Chart.")

st.divider()

# Visualization 2: Line Chart - Impact of Stress Scenarios Over Time
st.markdown("### Impact of Stress Scenarios Over Time")
st.markdown("""
    This line chart shows the trend of potential impact from stress scenarios over the selected years. 
    The impact is represented as a percentage of the bank's capital. 
    This visualization helps in understanding how the estimated impact of stress tests has evolved over time for the selected banks and stress test types.
""")
impact_df = filtered_df.groupby(['Year', 'Bank'])['Impact (% of Capital)'].mean().unstack()
if not impact_df.empty:
    st.line_chart(impact_df)
else:
    st.warning("No data to display for the selected filters in Impact Over Time Chart.")

st.divider()

# Visualization 3: Scatter Plot - Correlation between Frequency and Impact
st.markdown("### Correlation between Stress Test Frequency and Impact")
st.markdown("""
    This scatter plot explores the relationship between the frequency of stress tests and their potential impact. 
    Each point represents a combination of a specific stress test type at a bank in a given year. 
    This chart can help identify if there is a correlation between how often a bank conducts stress tests and the magnitude of the potential impact they foresee.
""")
if not filtered_df.empty:
    fig, ax = plt.subplots()
    sns.scatterplot(x='Frequency (per year)', y='Impact (% of Capital)', hue='Bank', style='Stress Test Type', data=filtered_df, ax=ax)
    plt.title('Correlation of Stress Test Frequency and Impact')
    st.pyplot(fig)
else:
    st.warning("No data to display for the selected filters in Correlation Scatter Plot.")

st.divider()

# Additional Information and Explanations
st.markdown("## Key Concepts and Further Exploration")
st.markdown("""
    - **Stress Testing**: A process used by financial institutions to evaluate their potential vulnerability to adverse economic or financial events. It helps in assessing capital adequacy and risk management practices.
    - **Types of Stress Tests**:
        - **Credit Risk**: Assesses potential losses from defaults on loans and other credit exposures.
        - **Market Risk**: Evaluates the impact of changes in market conditions (e.g., interest rates, exchange rates, equity prices) on the bank's portfolio.
        - **Operational Risk**: Examines potential losses from failures in internal processes, systems, or external events.
        - **Liquidity Risk**: Assesses the bank's ability to meet its short-term financial obligations.
    - **Importance of Stress Testing**: Regulatory requirements, internal risk management, and maintaining financial stability.

    **Reference**: This application is inspired by the practices documented in 'US Banks' Stress Testing Practices'. 
    For more detailed information on stress testing methodologies and regulatory frameworks, refer to financial risk management resources and regulatory guidelines.
""")

st.divider()
st.write("© 2025 QuantUniversity. All Rights Reserved.")
st.caption("The purpose of this demonstration is solely for educational use and illustration. "
           "To access the full legal documentation, please visit this link. Any reproduction of this demonstration "
           "requires prior written consent from QuantUniversity.")
