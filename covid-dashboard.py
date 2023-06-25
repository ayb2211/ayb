import streamlit as st
import pandas as pd
import plotly.express as px
from streamlit_option_menu import option_menu
from numerize.numerize import numerize
import time
import altair as alt
import plotly.graph_objects as go

st.set_page_config(page_title="Dashboard",page_icon="🌍",layout="wide")
st.subheader("🔔  Analytics Dashboard")
st.markdown("##")
theme_plotly = None

with open('style.css')as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html = True)

@st.cache_data
def load_model(model_name):
    df= pd.read_excel(model_name, sheet_name='Sheet1', parse_dates=['date'])
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
st.sidebar.subheader('Line chart parameters')
plot_data = st.sidebar.multiselect('Select data', ['total_cases', 'total_deaths'], ['total_cases', 'total_deaths'])
plot_height = st.sidebar.slider('Specify plot height', 200, 500, 250)

def home() :
    s1 = int(df[(df['location'].isin(location)) & (df['continent'].isin(continent))].groupby('location').max()['total_cases'].sum())
    s2 = int(df[(df['location'].isin(location)) & (df['continent'].isin(continent))].groupby('location').max()['total_deaths'].sum())
    s3 = int(df[(df['location'].isin(location)) & (df['continent'].isin(continent))].groupby('location').max()['total_vaccinations'].sum())
    s4 = int(df[(df['location'].isin(location)) & (df['continent'].isin(continent))].groupby('location').max()['people_vaccinated'].sum())

    #1st Row
    col1, col2, col3, col4 = st.columns(4)
    col1.metric(label="Total Cases", value=f"{s1}")
    col2.metric(label="Total Deaths", value=f"{s2}")
    col3.metric(label="Total Vaccinations", value=f"{s3}")
    col4.metric(label="People Vaccinated", value=f"{s4}")
    
    #2d row
    col5, col6 = st.columns((5,3))
    num_points = 1000  # Number of data points to display
    sampled_data = df.sample(num_points)
    with col5:
        st.markdown('### Heatmap')
        chart = alt.Chart(sampled_data).mark_line().encode(
            x='date',
            y='total_cases',
        ).properties(
            width=300, height=500
        )
        
        # Render the chart using Streamlit
        st.altair_chart(chart, use_container_width=True)
    with col6:
        # Group data by continent and calculate the sum of total_deaths
        grouped_data = df_filter.groupby('continent')['new_deaths'].sum().reset_index()

        # Create a donut chart using Plotly
        fig = go.Figure(data=[go.Pie(labels=grouped_data['continent'],
                                     values=grouped_data['new_deaths'],
                                     hole=0.5)])

        # Set title
        fig.update_layout(title_text='Total Deaths by Continent')

        # Render the chart using Streamlit
        st.plotly_chart(fig)

home()
