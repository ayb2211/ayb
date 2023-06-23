import streamlit as st
import pandas as pd
import plotly.express as px
from streamlit_option_menu import option_menu
from numerize.numerize import numerize
import time

st.set_page_config(page_title="Dashboard",page_icon="🌍",layout="wide")
st.subheader("🔔  Analytics Dashboard")
st.markdown("##")
theme_plotly = None

with open('style.css')as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html = True)

@st.cache_data
def load_model(model_name):
    df= pd.read_excel(model_name, sheet_name='Sheet1')
    return (df)


#load xlsx file
df=load_model("owid-covid-data.xlsx")

#side bar
st.sidebar.header("Please filter")
continent=st.sidebar.selectbox(
    "Select Continent",
    df["continent"].unique()  
)
all_options_con = st.sidebar.checkbox("Select all options", value=True)
if all_options_con:
    continent = df["continent"].unique()

location=st.sidebar.selectbox(
    "Select Location",
    df["location"].unique()  
)
all_options_loc = st.sidebar.checkbox("Select all options", value=True, key='ch2')
if all_options_loc:
    location = df["location"].unique()

def cards():
    #compute top analytics
    total_cases = int(df_selection['total_cases'].sum())
    total1=st.columns(1,gap='large')
    with total1:
        st.info('Total Investment',icon="📌")
        st.metric(label="sum TZS",value=f'{total_cases}')

   
