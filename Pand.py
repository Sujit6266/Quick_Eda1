import streamlit as st
import pandas as pd
import sweetviz as sv
import os
st.set_page_config(layout="wide")


st.title("📊 Sweetviz EDA Web App")

uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write("### Data Preview", df.head())

    if st.button("Generate Sweetviz Report"):
        # Generate Sweetviz report
        report = sv.analyze(df)
        report_path = "sweetviz_report.html"
        report.show_html(report_path, open_browser=False)

        # Display in Streamlit using an iframe
        with open(report_path, "r", encoding="utf-8") as f:
            html_content = f.read()
            st.components.v1.html(html_content, height=1000, scrolling=True)





