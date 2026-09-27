import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(
    page_title="Student Marks Analyzer",
    page_icon="📊",
    layout="wide"
)

st.title("Student Marks Analyzer")
st.write("Analyze student performance using marks data.")

uploaded_file = st.file_uploader(
    "Upload student CSV file",
    type=["csv"]
)

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
else:
    st.info("Upload a CSV file to begin.")
    st.stop()

subjects = ["Python", "DBMS", "Maths"]

if not all(col in df.columns for col in ["Name"] + subjects):
    st.error("CSV must contain Name, Python, DBMS, and Maths columns.")
    st.stop()

for subject in subjects:
    df[subject] = pd.to_numeric(df[subject], errors="coerce")

df = df.dropna(subset=subjects)

if df.empty:
    st.error("No valid student marks found.")
    st.stop()

df["Total"] = df[subjects].sum(axis=1)
df["Average"] = (df["Total"] / len(subjects)).round(2)

df["Result"] = df[subjects].ge(40).all(axis=1).map(
    {True: "Pass", False: "Fail"}
)

st.subheader("Class Statistics")

col1, col2, col3, col4 = st.columns(4)

col1.metric("Total Students", len(df))
col2.metric("Class Average", round(df["Average"].mean(), 2))
col3.metric("Highest Total", df["Total"].max())
col4.metric("Pass Percentage", 
            f"{(df['Result'].eq('Pass').mean() * 100):.1f}%")

st.subheader("Student Results")
st.dataframe(df, use_container_width=True)

st.subheader("Student Performance Chart")

fig, ax = plt.subplots(figsize=(12, 5))
ax.bar(df["Name"], df["Total"])
ax.set_xlabel("Student Name")
ax.set_ylabel("Total Marks (Out of 300)")
ax.set_title("Total Marks by Student")
plt.xticks(rotation=90)
fig.tight_layout()

st.pyplot(fig)
plt.close(fig)

st.subheader("Subject-wise Comparison")

st.bar_chart(df.set_index("Name")[subjects])

csv = df.to_csv(index=False).encode("utf-8")

st.download_button(
    "Download Analyzed Results",
    data=csv,
    file_name="analyzed_student_results.csv",
    mime="text/csv"
)
