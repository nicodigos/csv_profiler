import streamlit as st 
import pandas as pd
from src.dataframe_class import dataframe


st.title("Dataframe Profiler")

st.markdown('''
This app generates a detailed profile of your DataFrame. Just upload your dataset, and the app will automatically analyze each column—showing key statistics, data types, missing values, unique counts, and distributions—similar to what you see when previewing datasets on Kaggle.
''')

st.markdown('''
Don’t have a dataset? No problem, just click below to download a sample dataset and try it out!
''')

with open("data/pokemon.csv", "rb") as file:
    btn = st.download_button(
        label="Download Sample Dataset",
        data=file,
        file_name="pokemon.csv",
        mime="text/csv"
    )

uploaded_file = st.file_uploader(label='Upload a csv, json or parquet file',
                                 type=['csv', 'json', 'parquet'])
tab1, tab2, tab3 = st.tabs(['Dataframe', 
                            'Data Profiler',
                            # 'Modify Data', 
                            # 'Filter Data',
                            # 'Create Charts',
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
        st.dataframe(df)
with tab2:
    if uploaded_file is not None:
        data_profiler = dataframe.DataFrameGeneral(df)
        data_profiler.profiler_start()
        for key in data_profiler.profiler.keys():
            st.markdown(f'### {key}')
            final_text = ""
            col1, col2 = st.columns(2)
            if data_profiler.profiler[key].get('histogram') is not None:
                with col1:
                    st.plotly_chart(data_profiler.profiler[key]['histogram'])
            else:
                with col1:
                    st.markdown(f'# {data_profiler.profiler[key]["unique_values"]}')
                    st.markdown(f'#### Unique Values')

            with col2:
                for k in data_profiler.profiler[key].keys():
                    if k != 'histogram':
                        final_text += f'**{k}:** {data_profiler.profiler[key][k]}  \n'
                    else:
                        continue
                st.write(final_text)
           
            # else:
            #     for k in data_profiler.profiler[key].keys():
            #         final_text += f'**{k}:** {data_profiler.profiler[key][k]}  \n'
            #     st.write(final_text)
            st.divider()

with tab3:
    st.markdown("""## Converting Excel Files to CSV

### Requirements for the Excel File

To ensure effective conversion from Excel to CSV, the Excel file must meet the following criteria:

- **Tabular Data**: The file should contain data in a clear table format with defined rows and columns.
- **Granular Data**: The data should be detailed and specific, not summaries or aggregates.
- **No Dashboards**: Avoid using files with dashboards, charts, complex formulas, or conditional formatting, as these elements will not translate correctly to CSV.

### Using Microsoft Excel

1. **Open the Excel file**:
   - Launch Microsoft Excel and open the file you want to convert to CSV.

2. **Verify the data format**:
   - Ensure that the data is organized in a simple table format and not a dashboard or complex formatting.

3. **Select "Save As"**:
   - Click on "File" in the menu bar.
   - Select "Save As".
   - Choose the location where you want to save the file.

4. **Choose the CSV format**:
   - In the "Save as type" dropdown, select "CSV (Comma delimited) (*.csv)".
   - Enter a name for the file and click "Save".

5. **Handle the prompts**:
   - Excel may display some prompts about compatibility and data loss. Click "Yes" to confirm and proceed.

### Considerations

- **Data Format**: Make sure the data in the Excel file is properly formatted before conversion.
- **Delimiters**: The CSV format uses commas to separate values. Ensure that the data does not contain unwanted commas.

""")
