import streamlit as st 
import pandas as pd

uploaded_file = st.file_uploader(label='Upload a csv, json or parquet file',
                                 type=['csv', 'json', 'parquet'])
tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs(['Dataframe', 
                            'Data Profiler',
                            'Modify Data', 
                            'Filter Data',
                            'Create Charts',
                            'Do you have an Excel file?'
                            ])

if uploaded_file is not None:
    if uploaded_file.name.endswith('csv'):
        df = pd.read_csv(uploaded_file)
    elif uploaded_file.name.endswith('json'):
        df = pd.read_json(uploaded_file)
    elif uploaded_file.name.endswith('parquet'):
        df = pd.read_parquet(uploaded_file)
    else:
        print("ERROR: Not csv, json, parquet file provided an program pass")


with tab1:
    if uploaded_file is not None:
        st.markdown('### Original Dataframe')
        st.dataframe(df)
        st.markdown('### Modified Dataframe')
        st.dataframe(df)
