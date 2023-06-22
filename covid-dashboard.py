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
continent=st.sidebar.selectbox(
    "Select Continent",
    df["continent"].unique()
     
)
all_options = st.sidebar.checkbox("Select all options")

if all_options:
    continent = df["continent"].unique()


st.write('You selected:', continent{index})


