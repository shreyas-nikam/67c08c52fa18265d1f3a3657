```
```
# US Banks' Stress Testing Practices Visualizer

## Description

This Streamlit application provides an interactive visualization tool to explore stress testing practices of major US banks, including Citigroup, Bank of America, and JP Morgan Chase. Stress testing is a crucial risk management technique used by financial institutions to assess their resilience to adverse economic scenarios.

**Key Features:**

- **Interactive Visualizations:** Explore different types of stress tests, their frequency, and potential financial impacts through interactive bar charts, line charts, and scatter plots.
- **Data Filtering:** Easily filter data by bank, stress test type, and year range using intuitive sidebar controls.
- **Synthetic Dataset:** Utilizes a synthetic dataset designed to mimic real-world stress testing data, ensuring a self-contained and educational experience.
- **Educational Focus:**  Designed to enhance understanding of stress testing concepts, data visualization with Streamlit, and interactive data exploration.

**Learning Outcomes:**

- Gain insights into the stress testing practices of US banks.
- Learn to visualize financial data effectively using Streamlit.
- Understand basic data preprocessing and interactive data filtering techniques.

This application is inspired by the document 'US Banks' Stress Testing Practices' and serves as an educational tool to visualize and understand the concepts discussed within it.

## Installation

To run this Streamlit application, you need to have Python installed on your system. It is recommended to use Python 3.8 or higher. Follow these steps to install and set up the application:

1.  **Clone the repository (if applicable):**
    ```bash
    git clone [repository URL]
    cd [repository directory]
    ```
    *(If you are provided with a repository, otherwise skip this step and just save the provided Python code into a file.)*

2.  **Install required Python packages:**
    Use pip to install the necessary libraries. It is recommended to create a virtual environment to avoid conflicts with other Python projects.
    ```bash
    pip install streamlit pandas numpy matplotlib seaborn
    ```
    Alternatively, if you are using a virtual environment:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Linux/macOS
    venv\Scripts\activate  # On Windows
    pip install streamlit pandas numpy matplotlib seaborn
    ```

## Usage

1.  **Save the Python script:**
    If you haven't already, save the provided Python code as a Python file (e.g., `stress_test_app.py`).

2.  **Navigate to the application directory:**
    Open your terminal or command prompt and navigate to the directory where you saved the `stress_test_app.py` file.

3.  **Run the Streamlit application:**
    Execute the following command in your terminal:
    ```bash
    streamlit run stress_test_app.py
    ```

4.  **Access the application in your browser:**
    Streamlit will automatically open your default web browser and load the application. If it doesn't open automatically, you can access it by navigating to the URL provided in the terminal (usually `http://localhost:8501`).

5.  **Interact with the application:**
    - **Sidebar Filters:** Use the sidebar on the left to filter the data by:
        - **Select Banks:** Choose specific banks (Citigroup, Bank of America, JP Morgan Chase) to analyze.
        - **Select Stress Test Types:** Select the types of stress tests (Credit Risk, Market Risk, Operational Risk, Liquidity Risk) you are interested in.
        - **Select Year Range:**  Use the slider to choose the range of years for your analysis.
    - **Visualizations:** Explore the interactive charts displayed in the main area of the application:
        - **Stress Test Frequency by Bank and Type (Bar Chart):**  Shows the frequency of different stress tests for each bank.
        - **Impact of Stress Scenarios Over Time (Line Chart):**  Displays the trend of stress test impact over the selected years.
        - **Correlation between Stress Test Frequency and Impact (Scatter Plot):**  Illustrates the relationship between the frequency and impact of stress tests.

    The visualizations will dynamically update based on the filters you apply in the sidebar, allowing you to explore the data and gain insights into US banks' stress testing practices.

## Credits

Developed by QuantUniversity.

-   **Logo:**  The application uses the QuantUniversity logo as displayed in the sidebar.
-   **Copyright:** © 2025 QuantUniversity. All Rights Reserved.

## License

**Proprietary License - All Rights Reserved**

This Streamlit application is provided for educational use and illustration purposes only. All rights are reserved by QuantUniversity.

**Restrictions:**

-   **No Commercial Use:** This application is intended for non-commercial, educational use only.
-   **No Reproduction without Consent:**  Any reproduction, distribution, or modification of this application, in whole or in part, is strictly prohibited without prior written consent from QuantUniversity.

For inquiries regarding commercial use, licensing, or further information, please contact QuantUniversity through their official website.

**Disclaimer:**

This application uses synthetic data and is intended for educational demonstration. It should not be used for actual financial decision-making. For real-world financial analysis and regulatory compliance, refer to official sources and consult with qualified professionals.
```
```