import pandas as pd
import streamlit as st
import plotly.express as px
from PIL import Image

st.set_page_config(page_title='U.S. Imports for consumption of Cobalt, by country or locality - September 2022')
st.header('U.S. Imports for consumption of Cobalt, by country or locality - September 2022')
st.subheader('Source U.S. Geological Survey')

### --- LOAD DATAFRAME
excel_file = 'Cobalt-202209.xlsx'
sheet_name = 'DATA'

df = pd.read_excel(excel_file,
                    sheet_name=sheet_name,
                    usecols='A:C',
                    header=1)
            
df_participants = pd.read_excel(excel_file,
                                sheet_name= sheet_name,
                                usecols='A:C',
                                header=1)
df_participants.dropna(inplace=True)

# - - - STREAMLIT SELECTION
Countries = df['Cobalt Producing Countries:'].unique().tolist()
Metals_GW = df['Metals GW:'].unique().tolist()

weight_selection = st.slider('Metals_Value:',
                        min_value= min(Metals_GW),
                        max_value= max(Metals_GW),
                        value= (min(Metals_GW), max(Metals_GW)))










st.dataframe(df)
st.dataframe(df_participants)

pie_chart = px.pie(df_participants,
                    title='Countries Imported',
                    values='Metals_Value',
                    names='Countries')
st.plotly_chart(pie_chart)

image = Image.open('images/pres-image.jpg')
st.image(image,
        caption='Designed by Design Pickle',
        use_column_width=True)

