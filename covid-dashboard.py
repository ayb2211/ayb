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

@st.cache(allow_output_mutation=True)
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
all_options = st.sidebar.checkbox("Select all options", value=True)

if all_options:
    continent = df["continent"].unique()

st.write('You selected:', continent)


