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
continent=st.sidebar.multiselect(
    "Select Continent",
    df["continent"].unique(),
    default=None,
)
all_options_con = st.sidebar.checkbox("Select all options", value=True)
if all_options_con:
    continent = df["continent"].unique()

location=st.sidebar.multiselect(
    "Select Location",
    df["location"].unique(),
    default=None,
)
all_options_loc = st.sidebar.checkbox("Select all options", value=True, key='ch2')
if all_options_loc:
    location = df["location"].unique()
df_filter=df.query(
    "continent in @continent & location in @location"
)

def home() :
    s1 = int(df[(df['location'].isin(location)) & (df['continent'].isin(continent))].groupby('location').max()['total_cases'].sum())
    s2 = int(df[(df['location'].isin(location)) & (df['continent'].isin(continent))].groupby('location').max()['total_deaths'].sum())
    s3 = int(df[(df['location'].isin(location)) & (df['continent'].isin(continent))].groupby('location').max()['total_vaccinations'].sum())
    s4 = int(df[(df['location'].isin(location)) & (df['continent'].isin(continent))].groupby('location').max()['people_vaccinated'].sum())

    dates = pd.to_datetime(df_filter['date'], format='%Y-%m-%d').dt.date
    #1st Row
    col1, col2, col3, col4 = st.columns(4)
    col1.metric(label="Total Cases", value=f"{s1}")
    col2.metric(label="Total Deaths", value=f"{s2}")
    col3.metric(label="Total Vaccinations", value=f"{s3}")
    col3.metric(label="People Vaccinated", value=f"{s4}")
    
    
    #2d row
    col5, col6 = st.columns(2)



    

home()
   
