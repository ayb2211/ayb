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

df_selection=df.query(
    "Region==@region & Location==@location"
)
st.write('You selected:', continent)
st.write('You selected:', location)

def cards():
    #compute top analytics
    total_investment = float(df_selection['Investment'].sum())
    investment_mode = float(df_selection['Investment'].mode())
    investment_mean = float(df_selection['Investment'].mean())
    investment_median= float(df_selection['Investment'].median()) 
    rating = float(df_selection['Rating'].sum())

    total1,total2,total3,total4,total5=st.columns(5,gap='large')
    with total1:
        st.info('Total Investment',icon="📌")
        st.metric(label="sum TZS",value=f"{total_investment:,.0f}")

    with total2:
        st.info('Most frequent',icon="📌")
        st.metric(label="mode TZS",value=f"{investment_mode:,.0f}")

    with total3:
        st.info('Average',icon="📌")
        st.metric(label="average TZS",value=f"{investment_mean:,.0f}")

    with total4:
        st.info('Central Earnings',icon="📌")
        st.metric(label="median TZS",value=f"{investment_median:,.0f}")

    with total5:
        st.info('Ratings',icon="📌")
        st.metric(label="Rating",value=numerize(rating),help=f""" Total Rating: {rating} """)
