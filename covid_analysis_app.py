import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import plotly.subplots 
from datetime import datetime
import time
import folium


@st.cache_data
def get_data():
    # Load your student performance dataset (replace with your actual data)
    covid_data = pd.read_csv(r"C:\Users\DELL\Downloads\covid_19_india.csv")
    covid_data['Active_cases']=covid_data['Confirmed']-(covid_data['Cured']+covid_data['Deaths'])
    covid_data.Date = pd.to_datetime(covid_data.Date)
    covid_data['year'] = covid_data.Date.dt.year
    return covid_data

covid_data = get_data()





# Create a Streamlit app

st.title("COVID-19 REPORT (INDIA)")
st.write("Here's a preview of the data:")
def change_label_style(header, font_size='15px', font_color='red', font_family='sans-serif'):
    html = f"""
        <style>
            p {{
                font-size: {font_size};
                color: {font_color};
                font-family: {font_family};
            }}
        </style>
    """
    return st.markdown(html, unsafe_allow_html=True)

st.markdown("<h2 style='text-align: center;'>YEAR-(2020-21)</h2>", unsafe_allow_html=True)


# Usage:
change_label_style("Here's a preview of the data:", font_size='18px')







c1, c2,c3 = st.columns(3)
# c1.dataframe(covid_data)
c1.metric("DEATHS", 73389005)
c2.metric("RECOVERED CASES",5046125452 )
c3.metric("ACTIVE CASES",332164230 )
#Top 10 States based on the Active Cases
top10_active=covid_data.groupby(by='State/UnionTerritory').max()[['Active_cases','Date']].sort_values(by=['Active_cases'],ascending=False)
top10_active.head(10)

with st.sidebar:
    

    with st.spinner("Loading..."):
        time.sleep(5)
    st.success("Succesfull!")



size = st.sidebar.slider("Select number of states With Active cases", min_value=2, max_value=50, value=10)
fig, ax=plt.subplots(figsize=(16,9))
sns.barplot(data=top10_active.iloc[:size],y='Active_cases',x='State/UnionTerritory',linewidth=2.5,edgecolor='red', ax=ax)
plt.title("Top 10 States in India with most Active COVID-19 Cases",size=25)
plt.xlabel("States/UT",color='red')
plt.ylabel("Total Active Cases",color='red')
plt.xticks(rotation=90)
st.pyplot(fig)

#top states with highest deaths
sd= st.sidebar.slider("Most Critically Death Toll States", min_value=2, max_value=10, value=5)
top10_deaths=covid_data.groupby(by='State/UnionTerritory').max()[['Deaths','Date']].sort_values(by=['Deaths'],ascending=False).reset_index()
top10_deaths.head(10)
fig=plt.figure(figsize=(15,7))
plt.title("Top 10 States in India with most Deaths Cases",size=25)
ax=sns.barplot(data=top10_deaths.iloc[:sd],y='Deaths',x='State/UnionTerritory',linewidth=4,edgecolor='black',color='red',width=0.8)
plt.xlabel("States/UT",color='red')
plt.ylabel("Total Mortality",color='red')
st.pyplot(fig)



#Growth trend
fig=plt.figure(figsize=(20,6))
ax=sns.lineplot(data=covid_data[covid_data['State/UnionTerritory'].isin(['Maharastra','Uttar Pradesh','Karnataka','Tamil Nadu','West Bengal'])],x='Deaths',y='Active_cases',hue='State/UnionTerritory')
ax.set_title("Top 5 Affected States in India",size=16)
plt.xlabel("DEATHS",color='red',size=15)
plt.ylabel("ACTIVE CASES",color='green',size=15)
# st.pyplot(fig)


#Pie-Chart
cured=covid_data['Cured'].sum()
death=covid_data['Deaths'].sum()
active=covid_data['Active_cases'].sum()
fig,px.pie(names=["Cured Cases","Death Cases","Active Cases"],values=[cured,active,death],title="COVID-19 INDIA:DEATHS/CURED/ACTIVE")
# st.pyplot(fig)
















