import os
import shutil
from datetime import date

# Current project folder
base_folder = os.path.dirname(os.path.abspath(__file__))

# Task 5 portfolio folder
portfolio_folder = os.path.join(base_folder, "Task5_Portfolio")
os.makedirs(portfolio_folder, exist_ok=True)

# Check previous task files
files_to_check = [
    "sales.csv",
    "cleaned_sales.csv",
    "data_dictionary.xlsx",
    "task1.py",
    "task2.py",
    "task3.py",
    "task4.py"
]

print("\n========== TASK 5 PORTFOLIO CHECK ==========\n")

found = []
missing = []

for file in files_to_check:
    path = os.path.join(base_folder, file)

    if os.path.exists(path):
        found.append(file)
        print("FOUND  :", file)
    else:
        missing.append(file)
        print("MISSING:", file)

# Copy Task 4 presentation if available
presentation = os.path.join(
    base_folder,
    "task4_outputs",
    "Task4_Presentation.pptx"
)

if os.path.exists(presentation):
    destination = os.path.join(
        portfolio_folder,
        "Task4_Presentation.pptx"
    )
    shutil.copy2(presentation, destination)
    print("\nTask 4 presentation copied successfully.")

# Create README
readme_content = f"""# Data Analyst Internship Portfolio

## About This Portfolio

This repository contains my complete Data Analyst Internship work.

I worked on data cleaning, data analysis, visualization,
interactive dashboards, statistical validation and
final data storytelling.

## Internship Tasks

### Task 1 - Data Cleaning and Exploration
- Data loading
- Data cleaning
- Data exploration
- Data dictionary
- Cleaned dataset

### Task 2 - Data Analysis and Visualization
- Sales analysis
- Business analysis
- Charts and visualizations
- Correlation analysis
- Dashboard outputs

### Task 3 - Interactive Dashboard
- Interactive dashboard
- KPI analysis
- Filters
- Interactive charts
- Streamlit

### Task 4 - Data Storytelling and Statistical Validation
- Business insights
- Category analysis
- Product analysis
- Statistical testing
- Data storytelling
- Final presentation

## Technical Skills

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Plotly
- Streamlit
- SciPy
- Excel
- Data Cleaning
- Data Visualization
- Statistical Analysis
- GitHub

## Previous Task Repositories

Replace the links below with your actual GitHub repository links.

- Task 1: ADD_YOUR_TASK_1_GITHUB_LINK
- Task 2: ADD_YOUR_TASK_2_GITHUB_LINK
- Task 3: ADD_YOUR_TASK_3_GITHUB_LINK
- Task 4: ADD_YOUR_TASK_4_GITHUB_LINK

## Final Presentation

Task 4 final presentation is included in this portfolio.

## Key Learnings

During this internship, I learned how to:

1. Clean and prepare data.
2. Analyze business data using Python.
3. Create meaningful visualizations.
4. Build interactive dashboards.
5. Apply basic statistical methods.
6. Present data-driven insights.
7. Organize projects professionally using GitHub.

## Completion Date

{date.today().strftime("%d-%m-%Y")}

---
Data Analyst Internship Portfolio
"""

readme_path = os.path.join(portfolio_folder, "README.md")

with open(readme_path, "w", encoding="utf-8") as file:
    file.write(readme_content)

# Create checklist
checklist = f"""TASK 5 - PORTFOLIO CHECKLIST

Date: {date.today().strftime("%d-%m-%Y")}

Files found:
{chr(10).join("- " + f for f in found)}

Missing files:
{chr(10).join("- " + f for f in missing) if missing else "- None"}

NEXT STEPS:

1. Create GitHub repository:
   YourName-DataAnalyst-Internship-Portfolio

2. Upload README.md

3. Add Task 1 GitHub link

4. Add Task 2 GitHub link

5. Add Task 3 GitHub link

6. Add Task 4 GitHub link

7. Upload final presentation

8. Review the complete portfolio

9. Prepare 3-5 minute LinkedIn portfolio walkthrough
"""

checklist_path = os.path.join(
    portfolio_folder,
    "portfolio_checklist.txt"
)

with open(checklist_path, "w", encoding="utf-8") as file:
    file.write(checklist)

print("\n============================================")
print("TASK 5 PORTFOLIO CREATED SUCCESSFULLY")
print("============================================")
print("\nOpen this folder:")
print("Task5_Portfolio")
print("\nFiles created:")
print("- README.md")
print("- portfolio_checklist.txt")

if os.path.exists(
    os.path.join(portfolio_folder, "Task4_Presentation.pptx")
):
    print("- Task4_Presentation.pptx")

print("\nNext: Upload the Task5_Portfolio files to GitHub.")