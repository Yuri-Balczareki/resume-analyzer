import os 
import streamlit as st 
import pandas as pd 
from st_aggrid import AgGrid, GridOptionsBuilder, GridUpdateMode 
from database import AnalyzeDatabase 


database = AnalyzeDatabase()

st.set_page_config(
    layout='wide', 
    page_title='Resume Analyzer'
)

option = st.selectbox(
    'Choose your job:', 
    [job.get('name') for job in database.jobs.all()], 
    index=None
)

data = None 

# If user chooses an Job.
if option: 
    job = database.get_job_by_name(option)
    data = database.get_analysis_by_job_id(job.get('id'))

    df = pd.DataFrame(
        data if data else {}, 
        columns=[
            'name', 
            'education', 
            'skills', 
            'language', 
            'score', 
            'resume_id', 
            'id'
        ]
    )

    df.rename(
        columns={
            'name': 'Name', 
            'education': 'Education', 
            'skills': 'Skills', 
            'language': 'Languages',
            'score': 'Score',
            'resume_id': 'Resume ID', 
            'id': 'ID'
        }, 
        inplace=True
    )

    gb = GridOptionsBuilder.from_dataframe(df)
    gb.configure_pagination(paginationAutoPageSize=True) 

    if data: 
        gb.configure_column('Score', header_name='Score', sort='desc')
        gb.configure_selection(selection_mode='multiple', use_checkbox=True)

    # Build Table 
    grid_options = gb.build()

    # Build a bar chart to show which candidate has a higher score. 
    st.subheader('Candidate classification')
    st.bar_chart(df, x='Name', y='Score', color='Name', horizontal=True)

    response = AgGrid(
        df, 
        gridOptions=grid_options, 
        enable_enterprise_modules=True, 
        update_mode=GridUpdateMode.COLUMN_CHANGED, 
        theme='streamlit'
    )

    selected_candidates = response.get('selected_rows', [])
    candidates_df = pd.DataFrame(selected_candidates)

    resumes = database.get_resumes_by_job_id(job.get('id'))