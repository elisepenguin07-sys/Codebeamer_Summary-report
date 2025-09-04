# Codebeamer_Summary-reportd
import streamlit as st
import pandas as pd
from docx import Document
from docx.shared import Pt
from docx.enum.text import WD_PARAGRAPH_ALIGNMENT

plt.rcParams['font.family'] = ['Microsoft JhengHei']  # 微軟正黑體，Windows 預設有
plt.rcParams['axes.unicode_minus'] = False

doc = Document()

#webstie title
st.title("Summary Report")

# File name
st.header("Document Information")
Title = st.text_input("Please enter the file name to export.")
Name = st.text_input("Please enter the document editor's name.")
Project = st.text_input("Please enter the project name")
Date= st.text_input("Please enter the edit date")
Text = st.selectbox("", ["Software Integration Test", "Software Qualification Test", "System Integration Test", "System Qualification Test"])

#Upload file
redmine_df = None
codebeamer_df = None

uploaded_file1 = st.file_uploader("Please upload the data from Redmine.(csv file)", type=["csv"])
uploaded_file2 = st.file_uploader("Please upload the data from Codebeamer.(xlsx file)", type=["xlsx"])

if uploaded_file1 is not None:
  try:
    redmine_df = pd.read_csv(uploaded_file1, encoding = "big5")
    st.success("Redmine file uploaded successfully!")
  except Exception as e:
    st.error(f"Error reading the Redmine file. Please make sure the file is encoded in Big5.\n\n{e}")

if uploaded_file2 is not None:
  try:
    codebeamer_df = pd.read_excel(uploaded_file2)
    st.success("Codebeamer file uploaded successfully!")
  except Exception as e:
    st.error(f"Error reading the file.\n\n{e}")

#Purpose
st.header("Purpose / 目的")
if Project and Text:
  st.write(f"""The purpose of this document is the {Text} summary report of the {Project} project.
本文件目的為{Project}項目的{Text}總結報告""")

#Scope
st.header("Scope / 適用範圍")
if Project and Text and Title:
  st.write(f"""The scope of the software qualification test summary report of the {Project} project is applicable to the {Text}ing performed on the software version defined in the release plan.\n
{Project} 項目專案的{Title}的範圍適用於發布計劃裡定義的軟體版本所進行的{Text}
""")
