# import pandas as pd
# import streamlit as st
# import plotly.express as px
# from PIL import Image

# st.set_page_config(page_title='Survey Results')
# st.header('Survey Results 2021')
# st.subheader('Was the tutorial helpful?')

# ### --- LOAD DATAFRAME
# excel_file = 'Survey_Results.xlsx'
# sheet_name = 'DATA'

# df = pd.read_excel(excel_file,
#                    sheet_name=sheet_name,
#                    usecols='B:D',
#                    header=3)

# df_participants = pd.read_excel(excel_file,
#                                 sheet_name= sheet_name,
#                                 usecols='F:G',
#                                 header=3)
# df_participants.dropna(inplace=True)

# # --- STREAMLIT SELECTION
# department = df['Department'].unique().tolist()
# ages = df['Age'].unique().tolist()

# age_selection = st.slider('Age:',
#                         min_value= min(ages),
#                         max_value= max(ages),
#                         value=(min(ages),max(ages)))

# department_selection = st.multiselect('Department:',
#                                     department,
#                                     default=department)

# # --- FILTER DATAFRAME BASED ON SELECTION
# mask = (df['Age'].between(*age_selection)) & (df['Department'].isin(department_selection))
# number_of_result = df[mask].shape[0]
# st.markdown(f'*Available Results: {number_of_result}*')

# # --- GROUP DATAFRAME AFTER SELECTION
# df_grouped = df[mask].groupby(by=['Rating']).count()[['Age']]
# df_grouped = df_grouped.rename(columns={'Age': 'Votes'})
# df_grouped = df_grouped.reset_index()

# # --- PLOT BAR CHART
# bar_chart = px.bar(df_grouped,
#                    x='Rating',
#                    y='Votes',
#                    text='Votes',
#                    color_discrete_sequence = ['#F63366']*len(df_grouped),
#                    template= 'plotly_white')
# st.plotly_chart(bar_chart)

# # --- DISPLAY IMAGE & DATAFRAME
# col1, col2 = st.columns(2)
# image = Image.open('images/survey.jpg')
# col1.image(image,
#         caption='Designed by slidesgo / Freepik',
#         use_column_width=True)
# col2.dataframe(df[mask])

# # --- PLOT PIE CHART
# pie_chart = px.pie(df_participants,
#                 title='Total No. of Participants',
#                 values='Participants',
#                 names='Departments')

# st.plotly_chart(pie_chart)

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


# import pandas as pd
# import streamlit as st
# import plotly.express as px
# from PIL import Image
# from oauthlib.oauth2 import WebApplicationClient
# import requests

# # Initialize Google OAuth client
# client_id = "975913572837-r0n6h1ur8s6ik3v35ino1noshdn5jtvj.apps.googleusercontent.com"
# client = WebApplicationClient(client_id)

# # Function to fetch Google user info
# def get_google_user_info(token):
#     url = "https://www.googleapis.com/oauth2/v3/userinfo"
#     headers = {"Authorization": f"Bearer {token}"}
#     response = requests.get(url, headers=headers)
#     return response.json()

# # Google login button
# def google_login_button():
#     auth_url = f"https://accounts.google.com/o/oauth2/auth?client_id={client_id}&redirect_uri={st.secrets['oauth.google.redirect_uri']}&response_type=code&scope=openid%20email%20profile"
#     return f'<a href="{auth_url}"><button>Login with Google</button></a>'

# # Streamlit page configuration
# st.set_page_config(page_title='Survey Results')
# st.header('Survey Results 2021')

# # Check if user is logged in
# if "user" not in st.session_state:
#     if st.secrets["oauth.google.logged_in"] == "true":
#         user_info = get_google_user_info(st.secrets["oauth.google.token"])
#         st.session_state.user = user_info
#     else:
#         st.write("Please log in to continue.")
#         code = st.experimental_get_query_params().get("code", None)
#         if code:
#             token_url, headers, body = client.prepare_token_request("https://oauth2.googleapis.com/token",
#                                                                     authorization_response=request.url,
#                                                                     redirect_url=request.base_url,
#                                                                     code=code)
#             token_response = requests.post(token_url, headers=headers, data=body, auth=(client_id, st.secrets["oauth.google.client_secret"]))
#             token_response.raise_for_status()
#             token = client.parse_request_body_response(token_response.json())
#             user_info = get_google_user_info(token["access_token"])
#             st.session_state.user = user_info
#             st.session_state.token = token["access_token"]
#             st.secrets["oauth.google.logged_in"] = "true"
#             st.secrets["oauth.google.token"] = token["access_token"]
#         else:
#             st.markdown(google_login_button(), unsafe_allow_html=True)
# else:
#     st.write(f"Logged in as: {st.session_state.user['name']}")

# st.subheader('Was the tutorial helpful?')

# # --- UPLOAD EXCEL OR CSV FILE
# file_types = ['xlsx', 'xls', 'csv']  # Add 'csv' to the list of accepted file types
# excel_file = st.file_uploader("Upload Excel or CSV file", type=file_types)

# if excel_file is not None:
#     if excel_file.type == 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet' or \
#             excel_file.type == 'application/vnd.ms-excel' or \
#             excel_file.type == 'text/csv':
#         # --- LOAD DATAFRAME
#         if excel_file.type == 'text/csv':
#             df = pd.read_csv(excel_file)
#         else:
#             df = pd.read_excel(excel_file)

#         # --- STREAMLIT SELECTION
#         columns = df.columns.tolist()

#         column_selection = st.multiselect('Select columns to use:',
#                                           columns)

#         # --- FILTER DATAFRAME BASED ON SELECTION
#         if column_selection:
#             df = df[column_selection]

#             st.write(df)  # Display selected data

#             st.subheader('Visualization')

#             # --- CHOOSE CHART TYPE
#             chart_type = st.radio("Select Chart Type:",
#                                   ("Pie Chart", "Histogram", "Scatter Plot", "Line Graph", "Box Plot", "Violin Plot"))

#             if chart_type == "Pie Chart":
#                 # --- PLOT PIE CHART
#                 pie_chart = px.pie(df,
#                                     title='Total No. of Participants',
#                                     names=column_selection[0],
#                                     hole=0.3)
#                 st.plotly_chart(pie_chart)

#             elif chart_type == "Histogram":
#                 # --- PLOT HISTOGRAM
#                 histogram = px.histogram(df,
#                                           x=column_selection[0],
#                                           title='Histogram',
#                                           template='plotly_white')
#                 st.plotly_chart(histogram)

#             elif chart_type == "Scatter Plot":
#                 # --- PLOT SCATTER PLOT
#                 scatter_plot = px.scatter(df,
#                                           x=column_selection[0],
#                                           y=column_selection[1],
#                                           title='Scatter Plot',
#                                           template='plotly_white')
#                 st.plotly_chart(scatter_plot)
            
#             elif chart_type == "Line Graph":
#                 # --- PLOT LINE GRAPH
#                 line_graph = px.line(df,
#                                      title='Line Graph',
#                                      template='plotly_white')
#                 st.plotly_chart(line_graph)

#             elif chart_type == "Box Plot":
#                 # --- PLOT BOX PLOT
#                 box_plot = px.box(df,
#                                   title='Box Plot',
#                                   template='plotly_white')
#                 st.plotly_chart(box_plot)

#             elif chart_type == "Violin Plot":
#                 # --- PLOT VIOLIN PLOT
#                 violin_plot = px.violin(df,
#                                         title='Violin Plot',
#                                         template='plotly_white')
#                 st.plotly_chart(violin_plot)
#     else:
#         st.error("Unsupported file format. Please upload an Excel (xlsx, xls) or CSV (csv) file.")
