# Student-Marks-Analyzer

A simple data analysis web application built using Python, Pandas, Matplotlib, and Streamlit. This project helps users analyze student marks, calculate performance statistics, visualize results, and download the analyzed data.

## Features

- Upload student marks through a CSV file.
- Validate and clean the uploaded data.
- Calculate total marks and average marks for each student.
- Determine whether each student has passed or failed.
- Display class statistics, including total students, class average, highest total, and pass percentage.
- Visualize student performance using bar charts.
- Compare marks across Python, DBMS, and Maths.
- Download the analyzed results as a CSV file.

## Technologies Used

- **Python** – Core programming language
- **Pandas** – Data manipulation and analysis
- **Matplotlib** – Data visualization
- **Streamlit** – Interactive web application

## Project Structure

```text
student-marks-analyzer/
├── app.py
├── student_marks.csv
└── README.md
```

## Installation

1. Make sure Python is installed on your system.
2. Download or clone this repository.
3. Open a terminal in the project folder.
4. Install the required libraries:

```bash
python -m pip install streamlit pandas matplotlib
```

## Run the Application

Run the following command in your terminal:

```bash
python -m streamlit run app.py
```

Open the local URL displayed in the terminal, usually:

```text
http://localhost:8501
```

## How to Use

1. Open the Student Marks Analyzer web app.
2. Upload a CSV file containing student names and marks.
3. View the calculated totals, averages, and Pass/Fail results.
4. Explore the class statistics and performance charts.
5. Download the analyzed results as a CSV file.

## CSV File Format

The uploaded CSV must contain these columns:

- `Name`
- `Python`
- `DBMS`
- `Maths`

A student is considered to have passed if they score at least 40 marks in **each subject**.

## What I Learned

- Working with CSV files using Pandas
- Data cleaning and validation
- Calculating statistics using Python
- Creating visualizations with Matplotlib
- Building interactive web applications using Streamlit
- Debugging and running a Python project

## Future Improvements

- Add student search functionality.
- Add filters for Pass and Fail results.
- Support additional subjects.
- Deploy the application online.

---

**Note:** The included student dataset contains sample records for demonstration purposes.
