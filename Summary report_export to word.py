# Codebeamer_Summary-reportd
import streamlit as st
import pandas as pd
from docx import Document
from docx.shared import Pt
from docx.enum.text import WD_PARAGRAPH_ALIGNMENT

#webstie title
st.title("Summary Report")

# Doc Info
st.header("Document Information")
Title = st.text_input("Please enter the file name to export.")
Name = st.text_input("Please enter the document editor's name.")
Project = st.text_input("Please enter the project name")
Date= st.text_input("Please enter the edit date")
Test_en = st.selectbox("Please select the test type(EN)", ["Software Integration Test", "Software Qualification Test", "System Integration Test", "System Qualification Test"])
Test_cn = st.selectbox("Please select the test type(CN)", ["軟體整合測試", "軟體合格測試", "系統整合測試", "系統合格測試"])
Test_version = st.text_input("Please enter the text version")

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
st.header("1. Purpose / 目的")
if Project and Test_en and Test_cn:
  st.write(f"""The purpose of this document is the {Test_en} summary report of the {Project} project.\n
本文件目的為{Project}項目的{Test_cn}總結報告""")
else:
   st.info("Please fill in project name and test type.")

#Scope
st.header("2. Scope / 適用範圍")
if Project and Test_en and Test_cn and Title:
  st.write(f"""The scope of the software qualification test summary report of the {Project} project is applicable to the {Test_en}ing performed on the software version defined in the release plan.\n
{Project} 項目專案的{Title}的範圍適用於發布計劃裡定義的軟體版本所進行的{Test_cn}
""")
else:
  st.info("Please fill in project name, test type and file name.")

#Overview
st.header(f"3. {Test_en} Summary Report Overview / {Test_cn}總結報告概述")
st.subheader("3.1 Test Information Overview / 測試資訊概述 ")
if Test_en and Test_cn and Test_version:
  st.write(f"""This information is for {Test_version} version to fully test the {Test_en}.\n此資訊為{Test_version}版本進行的{Test_cn} (全量)""")
else:
  st.info("Please fill in Test type and Test version")

st.subheader("3.2 Overall Status / 總體狀態")
st.markdown("3.2.1Progress And Criteria / 進度和標準")
if Project and Test_en and Test_cn:
  st.wrtie(f"""The table below is the progress of {Test_en} for {Project}.\n下表是{Project}項目的{Text_cn}的進度和標準。""")
else:
   st.info("Please fill in Test type and Project")





