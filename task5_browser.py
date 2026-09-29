import streamlit as st

st.set_page_config(
    page_title="Data Analyst Internship Portfolio",
    layout="wide"
)

st.title("📊 Data Analyst Internship Portfolio")
st.write("Complete Internship Portfolio - Task 1 to Task 5")

st.divider()

st.header("👩‍💻 About My Internship")

st.write(
    "This portfolio contains my complete Data Analyst Internship work, "
    "including data cleaning, analysis, visualization, dashboards, "
    "statistical validation and data storytelling."
)

st.header("📚 Internship Tasks")

col1, col2 = st.columns(2)

with col1:
    st.subheader("Task 1 - Data Cleaning")
    st.write("• Data loading")
    st.write("• Data cleaning")
    st.write("• Data exploration")
    st.write("• Data dictionary")

    st.subheader("Task 3 - Interactive Dashboard")
    st.write("• Streamlit dashboard")
    st.write("• KPI analysis")
    st.write("• Interactive charts")
    st.write("• Filters")

with col2:
    st.subheader("Task 2 - Data Analysis")
    st.write("• Sales analysis")
    st.write("• Business analysis")
    st.write("• Data visualization")
    st.write("• Correlation analysis")

    st.subheader("Task 4 - Data Storytelling")
    st.write("• Business insights")
    st.write("• Statistical validation")
    st.write("• Data storytelling")
    st.write("• Final presentation")

st.divider()

st.header("🛠️ Technical Skills")

st.write(
    "Python | Pandas | Matplotlib | Seaborn | Plotly | "
    "Streamlit | SciPy | Excel | Data Visualization | GitHub"
)

st.header("🎯 Key Learnings")

st.write("1. Data cleaning and preparation")
st.write("2. Business data analysis")
st.write("3. Data visualization")
st.write("4. Interactive dashboard development")
st.write("5. Statistical analysis")
st.write("6. Professional data presentation")

st.success("Task 5 Portfolio Preview Completed Successfully!")
