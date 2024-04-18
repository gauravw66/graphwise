import pandas as pd
import streamlit as st
import plotly.express as px
from PIL import Image

st.set_page_config(page_title='Survey Results')
st.header('Survey Results 2021')
st.subheader('Was the tutorial helpful?')

# --- UPLOAD EXCEL OR CSV FILE
file_types = ['xlsx', 'xls', 'csv']  # Add 'csv' to the list of accepted file types
excel_file = st.file_uploader("Upload Excel or CSV file", type=file_types)

if excel_file is not None:
    if excel_file.type == 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet' or \
            excel_file.type == 'application/vnd.ms-excel' or \
            excel_file.type == 'text/csv':
        # --- LOAD DATAFRAME
        if excel_file.type == 'text/csv':
            df = pd.read_csv(excel_file)
        else:
            df = pd.read_excel(excel_file)

        # --- STREAMLIT SELECTION
        columns = df.columns.tolist()

        column_selection = st.multiselect('Select columns to use:',
                                          columns)

        # --- FILTER DATAFRAME BASED ON SELECTION
        if column_selection:
            df = df[column_selection]

            st.write(df)  # Display selected data

            st.subheader('Visualization')

            # --- CHOOSE CHART TYPE
            chart_type = st.radio("Select Chart Type:",
                                  ("Pie Chart", "Histogram", "Scatter Plot", "Line Graph", "Box Plot", "Violin Plot"))

            if chart_type == "Pie Chart":
                # --- PLOT PIE CHART
                pie_chart = px.pie(df,
                                    title='Total No. of Participants',
                                    names=column_selection[0],
                                    hole=0.3)
                st.plotly_chart(pie_chart)

            elif chart_type == "Histogram":
                # --- PLOT HISTOGRAM
                histogram = px.histogram(df,
                                          x=column_selection[0],
                                          title='Histogram',
                                          template='plotly_white')
                st.plotly_chart(histogram)

            elif chart_type == "Scatter Plot":
                # --- PLOT SCATTER PLOT
                scatter_plot = px.scatter(df,
                                          x=column_selection[0],
                                          y=column_selection[1],
                                          title='Scatter Plot',
                                          template='plotly_white')
                st.plotly_chart(scatter_plot)
            
            elif chart_type == "Line Graph":
                # --- PLOT LINE GRAPH
                line_graph = px.line(df,
                                     title='Line Graph',
                                     template='plotly_white')
                st.plotly_chart(line_graph)

            elif chart_type == "Box Plot":
                # --- PLOT BOX PLOT
                box_plot = px.box(df,
                                  title='Box Plot',
                                  template='plotly_white')
                st.plotly_chart(box_plot)

            elif chart_type == "Violin Plot":
                # --- PLOT VIOLIN PLOT
                violin_plot = px.violin(df,
                                        title='Violin Plot',
                                        template='plotly_white')
                st.plotly_chart(violin_plot)
    else:
        st.error("Unsupported file format. Please upload an Excel (xlsx, xls) or CSV (csv) file.")
