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

#load xlsx file
df=pd.read_excel('owid-covid-data.xlsx', sheet_name='Sheet1')

#side bar


st.sidebar.header("Please filter")
continent=st.sidebar.multiselect(
    "Select Continent",
     options=df["continent"].unique() +'ALL',
     default=df["continent"].unique(),
)
location=st.sidebar.multiselect(
    "Select Location",
     options=df["location"].unique(),
     default=df["location"].unique(),
)
construction=st.sidebar.multiselect(
    "Select Construction",
     options=df["Construction"].unique(),
     default=df["Construction"].unique(),
)

df_selection=df.query(
    "Continent==@continent& Location==@location & Construction ==@construction"
)


