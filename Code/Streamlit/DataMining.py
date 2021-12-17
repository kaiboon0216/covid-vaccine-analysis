import streamlit as st 
import numpy as np
import pandas as pd
import altair as alt 
from streamlit_folium import folium_static
import folium
from matplotlib import dates
import seaborn as sns
import matplotlib.pyplot as plt
import datetime
from PIL import Image 
import altair as alt 
import folium
import geopandas as gp
#EDA code
msia_cases = pd.read_csv('Clean/Clean_malaysia_cases.csv')
vax_msia = pd.read_csv('Clean/Clean_malaysia_vax.csv')
state_cases = pd.read_csv('Clean/Clean_state_cases.csv')
vax_state = pd.read_csv('Clean/Clean_state_vax.csv')
df_clusters = pd.read_csv('Clean/Clean_clusters.csv')
df_hosp = pd.read_csv('Clean/Clean_hospital.csv')
df_icu = pd.read_csv('Clean/Clean_icu.csv')
df_pkrc = pd.read_csv('Clean/Clean_pkrc.csv')
df_checkinM = pd.read_csv('Clean/Clean_checkin_malaysia.csv')
df_checkinMT = pd.read_csv('Clean/Clean_checkin_malaysia_time.csv')
df_checkinS = pd.read_csv('Clean/Clean_checkin_state.csv')
df_trace = pd.read_csv('Clean/Clean_trace.csv')
df_static = pd.read_csv('Clean/Clean_population.csv')


PahangDF= pd.read_csv('Correlation/Pahang_corr.csv')
JohorDF= pd.read_csv('Correlation/Johor_corr.csv')
KedahDF= pd.read_csv('Correlation/Kedah_corr.csv')
MelakaDF= pd.read_csv('Correlation/Melaka_corr.csv')
N9DF= pd.read_csv('Correlation/N9_corr.csv')
PulaupinangDF= pd.read_csv('Correlation/Pulaupinang_corr.csv')
PerakDF= pd.read_csv('Correlation/Perak_corr.csv')
PerlisDF= pd.read_csv('Correlation/Perlis_corr.csv')
SabahDF= pd.read_csv('Correlation/Sabah_corr.csv')
SarawakDF= pd.read_csv('Correlation/Sarawak_corr.csv')
TerengganuDF= pd.read_csv('Correlation/Terengganu_corr.csv')
KLDF= pd.read_csv('Correlation/KL_corr.csv')
LabuanDF= pd.read_csv('Correlation/Labuan_corr.csv')
PutrajayaDF= pd.read_csv('Correlation/Putrajaya_corr.csv')
SelangorDF= pd.read_csv('Correlation/Selangor_corr.csv')
KelantanDF= pd.read_csv('Correlation/Kelantan_corr.csv')
#-------------------------------------------------------------------------------------------------------------------------------------------#
st.set_page_config(layout="wide")
question1 = '<p style="font-family:Time-New-Roman; font-size: 32px;font-weight: bold;">Exploratory Data Analysis</p>' 
st.markdown(question1, unsafe_allow_html=True)

title1 = '<p style="font-family:Time-New-Roman; font-size: 24px;">Is there any correlation between vaccination and daily cases for all states of Malaysia?</p>' 
st.markdown(title1, unsafe_allow_html=True)

left_column, right_column ,text_column= st.columns(3)
with left_column:
    text = '<p style="font-family:Time-New-Roman; font-size: 18px;text-decoration: underline">Selangor</p>' 
    st.markdown(text, unsafe_allow_html=True)
    SelangorDF
with right_column:
    text = '<p style="font-family:Time-New-Roman; font-size: 18px;text-decoration: underline">Kelantan</p>' 
    st.markdown(text, unsafe_allow_html=True)
    KelantanDF
with text_column: 
    text5 = '<p style="font-family:Time-New-Roman; font-size: 15px;text-align: justify;"></p>'
    st.markdown(text5, unsafe_allow_html=True) 
    st.markdown(text5, unsafe_allow_html=True) 
    text5 = '<p style="font-family:Time-New-Roman; font-size: 15px;text-align: justify;">The highest correlation of Selangor in daily cases and vaccination columns are W.P. Kuala Lumpur.  </p>'
    st.markdown(text5, unsafe_allow_html=True)  
    text5 = '<p style="font-family:Time-New-Roman; font-size: 15px;text-align: justify;">The highest correlation of Kelantan in daily cases column is Terengganu,but vaccination column is Kedah.  </p>'
    st.markdown(text5, unsafe_allow_html=True)  

left_column, right_column ,text_column= st.columns(3)
with left_column:
    text = '<p style="font-family:Time-New-Roman; font-size: 18px;text-decoration: underline">Pahang</p>' 
    st.markdown(text, unsafe_allow_html=True)
    PahangDF
with right_column:
    text = '<p style="font-family:Time-New-Roman; font-size: 18px;text-decoration: underline">Johor</p>' 
    st.markdown(text, unsafe_allow_html=True)
    JohorDF
with text_column: 
    text5 = '<p style="font-family:Time-New-Roman; font-size: 15px;text-align: justify;"></p>'
    st.markdown(text5, unsafe_allow_html=True) 
    st.markdown(text5, unsafe_allow_html=True)
    text5 = '<p style="font-family:Time-New-Roman; font-size: 15px;text-align: justify;">The highest correlation of Pahang in daily cases column is Terengganu,but vaccination column is Perak.  </p>'
    st.markdown(text5, unsafe_allow_html=True)   
    text5 = '<p style="font-family:Time-New-Roman; font-size: 15px;text-align: justify;">The highest correlation of Johor in daily cases column is Pulau Pinang,but vaccination column is Sabah.  </p>'
    st.markdown(text5, unsafe_allow_html=True) 
    
left_column, right_column ,text_column= st.columns(3)
with left_column:
    text = '<p style="font-family:Time-New-Roman; font-size: 18px;text-decoration: underline">Kedah</p>' 
    st.markdown(text, unsafe_allow_html=True)
    KedahDF    
with right_column:
    text = '<p style="font-family:Time-New-Roman; font-size: 18px;text-decoration: underline">Melaka</p>'
    st.markdown(text, unsafe_allow_html=True)
    MelakaDF
with text_column: 
    text5 = '<p style="font-family:Time-New-Roman; font-size: 15px;text-align: justify;"></p>'
    st.markdown(text5, unsafe_allow_html=True) 
    st.markdown(text5, unsafe_allow_html=True)
    text5 = '<p style="font-family:Time-New-Roman; font-size: 15px;text-align: justify;">The highest correlation of Kedah in daily cases column is Pulau Pinang,but vaccination column is Johor.  </p>'
    st.markdown(text5, unsafe_allow_html=True)   
    text5 = '<p style="font-family:Time-New-Roman; font-size: 15px;text-align: justify;">The highest correlation of Melaka in daily cases column is Selangor,but vaccination column is Pahang.  </p>'
    st.markdown(text5, unsafe_allow_html=True)     
    
left_column, right_column ,text_column= st.columns(3)
with left_column:
    text = '<p style="font-family:Time-New-Roman; font-size: 18px;text-decoration: underline">Negeri Sembilan</p>'
    st.markdown(text, unsafe_allow_html=True)
    N9DF    
with right_column:
    text = '<p style="font-family:Time-New-Roman; font-size: 18px;text-decoration: underline">Pulau Pinang</p>'
    st.markdown(text, unsafe_allow_html=True)
    PulaupinangDF
with text_column: 
    text5 = '<p style="font-family:Time-New-Roman; font-size: 15px;text-align: justify;"></p>'
    st.markdown(text5, unsafe_allow_html=True) 
    st.markdown(text5, unsafe_allow_html=True)
    text5 = '<p style="font-family:Time-New-Roman; font-size: 15px;text-align: justify;">The highest correlation of Negeri Sembilan in daily cases column is  W.P. Kuala Lumpur,but vaccination column is Selangor.  </p>'
    st.markdown(text5, unsafe_allow_html=True)   
    text5 = '<p style="font-family:Time-New-Roman; font-size: 15px;text-align: justify;">The highest correlation of Pulau Pinang in daily cases column is Perak,but vaccination column is Johor.  </p>'
    st.markdown(text5, unsafe_allow_html=True)    
    
    
left_column, right_column ,text_column= st.columns(3)
with left_column:
    text = '<p style="font-family:Time-New-Roman; font-size: 18px;text-decoration: underline">Perak</p>'
    st.markdown(text, unsafe_allow_html=True)
    PerakDF   
with right_column:
    text = '<p style="font-family:Time-New-Roman; font-size: 18px;text-decoration: underline">Perlis</p>'
    st.markdown(text, unsafe_allow_html=True)
    PerlisDF
with text_column: 
    text5 = '<p style="font-family:Time-New-Roman; font-size: 15px;text-align: justify;"></p>'
    st.markdown(text5, unsafe_allow_html=True) 
    st.markdown(text5, unsafe_allow_html=True)
    text5 = '<p style="font-family:Time-New-Roman; font-size: 15px;text-align: justify;">The highest correlation of Perak in daily cases and vaccination columns are  Pulau Pinang.</p>'
    st.markdown(text5, unsafe_allow_html=True)   
    text5 = '<p style="font-family:Time-New-Roman; font-size: 15px;text-align: justify;">The highest correlation of Perlis in daily cases column is Terengganu,but vaccination column is Pulau Pinang.  </p>'
    st.markdown(text5, unsafe_allow_html=True)  
    
left_column, right_column ,text_column= st.columns(3)
with left_column:
    text = '<p style="font-family:Time-New-Roman; font-size: 18px;text-decoration: underline">Sabah</p>'
    st.markdown(text, unsafe_allow_html=True)
    SabahDF  
with right_column:
    text = '<p style="font-family:Time-New-Roman; font-size: 18px;text-decoration: underline">Sarawak</p>'
    st.markdown(text, unsafe_allow_html=True)
    SarawakDF
with text_column: 
    text5 = '<p style="font-family:Time-New-Roman; font-size: 15px;text-align: justify;"></p>'
    st.markdown(text5, unsafe_allow_html=True) 
    st.markdown(text5, unsafe_allow_html=True)
    text5 = '<p style="font-family:Time-New-Roman; font-size: 15px;text-align: justify;">The highest correlation of Sabah in daily cases column is Pulau Pinang,but vaccination column is Johor.  </p>'
    st.markdown(text5, unsafe_allow_html=True)   
    text5 = '<p style="font-family:Time-New-Roman; font-size: 15px;text-align: justify;">The highest correlation of Sarawak in daily cases column is Terengganu,but vaccination column is W.P. Labuan.  </p>'
    st.markdown(text5, unsafe_allow_html=True)   
    
left_column, right_column ,text_column= st.columns(3)
with left_column:
    text = '<p style="font-family:Time-New-Roman; font-size: 18px;text-decoration: underline">Terengganu</p>'
    st.markdown(text, unsafe_allow_html=True)
    TerengganuDF   
with right_column:
    text = '<p style="font-family:Time-New-Roman; font-size: 18px;text-decoration: underline">W.P. Kuala Lumpur</p>'
    st.markdown(text, unsafe_allow_html=True)
    KLDF
with text_column: 
    text5 = '<p style="font-family:Time-New-Roman; font-size: 15px;text-align: justify;"></p>'
    st.markdown(text5, unsafe_allow_html=True) 
    st.markdown(text5, unsafe_allow_html=True)
    text5 = '<p style="font-family:Time-New-Roman; font-size: 15px;text-align: justify;">The highest correlation of Terengganu in daily cases column is Kelantan,but vaccination column is Johor.  </p>'
    st.markdown(text5, unsafe_allow_html=True)   
    text5 = '<p style="font-family:Time-New-Roman; font-size: 15px;text-align: justify;">The highest correlation of W.P. Kuala Lumpur in daily cases and vaccination columns are Selangor.  </p>'
    st.markdown(text5, unsafe_allow_html=True)
    
left_column, right_column ,text_column= st.columns(3)
with left_column:
    text = '<p style="font-family:Time-New-Roman; font-size: 18px;text-decoration: underline">W.P. Labuan</p>'
    st.markdown(text, unsafe_allow_html=True)
    LabuanDF   
with right_column:
    text = '<p style="font-family:Time-New-Roman; font-size: 18px;text-decoration: underline">W.P. Putrajaya</p>'
    st.markdown(text,unsafe_allow_html=True)
    PutrajayaDF
with text_column:
    text5 = '<p style="font-family:Time-New-Roman; font-size: 15px;text-align: justify;"></p>'
    st.markdown(text5, unsafe_allow_html=True) 
    st.markdown(text5, unsafe_allow_html=True)
    text5 = '<p style="font-family:Time-New-Roman; font-size: 15px;text-align: justify;">The highest correlation of W.P. Labuan in daily cases column is Negeri Sembilan,but vaccination column is Sarawak.  </p>'
    st.markdown(text5, unsafe_allow_html=True)   
    text5 = '<p style="font-family:Time-New-Roman; font-size: 15px;text-align: justify;">The highest correlation of W.P. Putrajaya in daily cases and vaccination columns are Selangor.  </p>'
    st.markdown(text5, unsafe_allow_html=True)
#---------------------------------------------------------------------------------------------
cases =state_cases[['date','state','cases_new']]
hosp =df_hosp[['date','state','admitted_total','discharged_total']]
hosp = hosp.merge(cases,left_on=['date','state'],right_on=['date','state'],how='left')
hosp['year_month'] = pd.to_datetime(hosp["date"], format='%Y-%m-%d').apply(lambda x: x.strftime('%Y-%m'))
hosp_date =hosp[['year_month','admitted_total','discharged_total','cases_new']]
#group and sum data by month
hosp_date =hosp.groupby(['year_month'], as_index = False).sum()
#calculate admitted rate & discharged rate
hosp_date['Admitted rate'] = hosp_date['admitted_total']/hosp_date['cases_new']
hosp_date['Discharged rate'] = hosp_date['discharged_total']/hosp_date['admitted_total']
#get only admitted rate,discharged rate, and year_month column for plotting used
hosp_date = hosp_date[['year_month','Admitted rate','Discharged rate']]
hosp_date = hosp_date.melt('year_month', var_name='type',  value_name='vals')
#-------------------------------------------------------------------------------------
text5 = '<p style="font-family:Time-New-Roman; font-size: 15px;text-align: justify;"></p>'
st.markdown(text5, unsafe_allow_html=True) 
st.markdown(text5, unsafe_allow_html=True) 
title4 = '<p style="font-family:Time-New-Roman; font-size: 24px">What is the admitted and discharged rate of hospitals and pkrc in every state during this pandemic? </p>' 
st.markdown(title4, unsafe_allow_html=True)
chart=alt.Chart(hosp_date).mark_bar().encode(
    x='type:O',
    y='vals:Q',
    color='type:N',
)
text = chart.mark_text(
    align='center',
    baseline='middle',
    dy=-5  
).encode(
    text=alt.Text('vals', format='.1f')
)
g=alt.layer(chart, text, data=hosp_date).facet(column='year_month:N',title='Admitted and Discharged rate of hospital'
)
st.altair_chart(g, use_container_width=True)

text5 = '<p style="font-family:Time-New-Roman; font-size: 15px;text-align: justify;">Based on the grouped bar chart above, the first few months of the Covid-19 pandemic which is from March until September of 2020, the Admitted rate of hospital is higher than the discharged rate of hospital.After September of 2020, the Admitted rate had keep decreasing until now only have slightly increase in the early of the 2021. Besides, the discharged rate of hospital did not have a extreme up and down, its rate only in between 0.6 to 1.2. </p>'
st.markdown(text5, unsafe_allow_html=True) 

hosp_try=hosp.groupby(['year_month','state']).sum()
hosp_try[hosp_try == 0] = 1
hosp_try['admitted_rate'] = hosp_try['admitted_total']/hosp_try['cases_new']
hosp_try['discharged_rate'] = hosp_try['discharged_total']/hosp_try['admitted_total']
hosp_try = hosp_try.reset_index()
hosp_try = hosp_try[['year_month','state','admitted_rate','discharged_rate']]

text5 = '<p style="font-family:Time-New-Roman; font-size: 15px;text-align: justify;"></p>'
st.markdown(text5, unsafe_allow_html=True) 

left_column, right_column= st.columns([5,2])
with left_column:
    g=alt.Chart(hosp_try,title='Admitted rate of hospital in every state').mark_line().encode(
        x="year_month",
        y="admitted_rate",
        color = alt.Color('state', scale=alt.Scale(scheme = 'category20'))
    ).properties(
        width=1000,
        height=300
    )
    st.altair_chart(g, use_container_width=True)

with right_column:
    text6_1 = '<p style="font-family:Time-New-Roman;font-size: 15px;text-align: justify;"> Based on the line chart, we had observed that the hospital admitted rate in every state of Malaysia were very high at the beginning of the Covid-19 pandemic.Then, all the hospital admitted rate of the states were decrease rapidly in 2021 and only increase slighly during May to July of 2021 in Kelantan.</p>'
    st.markdown(text6_1 , unsafe_allow_html=True)

text5 = '<p style="font-family:Time-New-Roman; font-size: 15px;text-align: justify;"></p>'
st.markdown(text5, unsafe_allow_html=True) 
left_column, right_column= st.columns([5,2])
with left_column:
    g=alt.Chart(hosp_try,title='Discharged rate of hospital in every state').mark_line().encode(
        x="year_month",
        y="discharged_rate",
        color = alt.Color('state', scale=alt.Scale(scheme = 'category20'))
    ).properties(
        width=1000,
        height=300
    )
    st.altair_chart(g, use_container_width=True)

with right_column:
    text6_1 = '<p style="font-family:Time-New-Roman;font-size: 15px;text-align: justify;"> Based on the line chart, we had observed that the hospital discharged rate in every state of Malaysia were not so high in the whole covid-19 pandemic.Only Negeri Sembilan had a very high discharged rate which was between 8 to 9 in July of 2020 and Pahang had 5.0 of discharged rate in August of 2020. The discharged rate of 2021 did not have a very high up and down, only between 0 to 2 of discharged rate.</p>'
    st.markdown(text6_1 , unsafe_allow_html=True)
    
text5 = '<p style="font-family:Time-New-Roman; font-size: 15px;text-align: justify;"></p>'
st.markdown(text5, unsafe_allow_html=True) 
#-------------------------------------------------------------------------------------
pkrc =df_pkrc[['date','state','admitted_total','discharge_total']]
pkrc = pkrc.merge(cases,left_on=['date','state'],right_on=['date','state'],how='left')
pkrc['year_month'] = pd.to_datetime(pkrc["date"], format='%Y-%m-%d').apply(lambda x: x.strftime('%Y-%m'))
pkrc_date =pkrc[['year_month','admitted_total','discharge_total']]
pkrc_date =pkrc.groupby(['year_month'], as_index = False).sum()
pkrc_date['Admitted rate'] = pkrc_date['admitted_total']/pkrc_date['cases_new']
pkrc_date['Discharged rate'] = pkrc_date['discharge_total']/pkrc_date['admitted_total']
pkrc_date = pkrc_date[['year_month','Admitted rate','Discharged rate']]
pkrc_date = pkrc_date.melt('year_month', var_name='type',  value_name='vals')
#----------------------------------------------------------------------------------
chart=alt.Chart(pkrc_date).mark_bar().encode(
    x='type:O',
    y='vals:Q',
    color='type:N',
)
#mark the value on each bar of the chart
text = chart.mark_text(
    align='center',
    baseline='middle',
    dy=-5  # Nudges text to right so it doesn't appear on top of the bar
).encode(
    text=alt.Text('vals', format='.1f')
)
g=alt.layer(chart, text, data=pkrc_date).facet(column='year_month:N',title='Admitted and Discharged rate of pkrc'
)
st.altair_chart(g, use_container_width=True)

text6_1 = '<p style="font-family:Time-New-Roman;font-size: 15px;text-align: justify;"> Different with the hospital, the admitted rate and discharged rate of pkrc had a up and down value in 2020 espescially the discharged rate. The discharged rate of June 2020 is the highest which is 2.7 of discharged rate and the admitted rate of August 2020 had the highest Admitted rate which is 1.8. Based on the graph above, the admitted rate of pkrc in 2021 had keep decreasing until 0.1 only in September 2021,but the discharged rate in 2021 always in between 0.9 to 1.1 of discharged rate.</p>'
st.markdown(text6_1 , unsafe_allow_html=True)
text5 = '<p style="font-family:Time-New-Roman; font-size: 15px;text-align: justify;"></p>'
st.markdown(text5, unsafe_allow_html=True) 
#---------------------------------------------------------------------------------------------
pkrc_try=pkrc.groupby(['year_month','state']).sum()
pkrc_try[pkrc_try == 0] = 1
pkrc_try['Admitted rate'] = pkrc_try['admitted_total']/pkrc_try['cases_new']
pkrc_try['Discharged rate'] = pkrc_try['discharge_total']/pkrc_try['admitted_total']
pkrc_try = pkrc_try.reset_index()
pkrc_try = pkrc_try[['year_month','state','Admitted rate','Discharged rate']]
#-----------------------------------------------------------------------------------------------
left_column, right_column= st.columns([5,2])
with left_column:
    g=alt.Chart(pkrc_try,title='Admitted rate of pkrc').mark_line().encode(
        x="year_month",
        y="Admitted rate",
        color = alt.Color('state', scale=alt.Scale(scheme = 'category20'))
    ).properties(
        width=1000,
        height=300
    )
    st.altair_chart(g, use_container_width=True)

with right_column:
    text6_1 = '<p style="font-family:Time-New-Roman;font-size: 15px;text-align: justify;"> Based on the line graph, we can observed that all the admitted rate of pkrc in every state are not high which is only in between 0 to 5, but only Terrenganu has a very high admitted rate in 2020 especially April to June of 2020 where the admitted rate of Terrenganu reached in between 35 to 40. </p>'
    st.markdown(text6_1 , unsafe_allow_html=True)
text5 = '<p style="font-family:Time-New-Roman; font-size: 15px;text-align: justify;"></p>'
st.markdown(text5, unsafe_allow_html=True) 
left_column, right_column= st.columns([5,2])
with left_column:
    g=alt.Chart(pkrc_try,title='Discharged rate of pkrc').mark_line().encode(
        x="year_month",
        y="Discharged rate",
        color = alt.Color('state', scale=alt.Scale(scheme = 'category20'))
    ).properties(
        width=1000,
        height=300
    )
    st.altair_chart(g, use_container_width=True)

with right_column:
    text6_1 = '<p style="font-family:Time-New-Roman;font-size: 15px;text-align: justify;"> Based on the line graph, we can observed that all the discharged rate of pkrc in every state are not high which is only in between 0 to 5 same with the admitted rate of pkrc, Only in May of 2020, the discharged rate of Johor has increase to more than 60.</p>'
    st.markdown(text6_1 , unsafe_allow_html=True)
text5 = '<p style="font-family:Time-New-Roman; font-size: 15px;text-align: justify;"></p>'
st.markdown(text5, unsafe_allow_html=True) 
text5 = '<p style="font-family:Time-New-Roman; font-size: 15px;text-align: justify;"></p>'
st.markdown(text5, unsafe_allow_html=True) 
#------------------------------------------------------------------------------------------------        
title4 = '<p style="font-family:Time-New-Roman; font-size: 24px;">Has vaccination helped to reduce the cases? Which states have shown the effectiveness of vaccination?</p>' 
st.markdown(title4, unsafe_allow_html=True)

#--------------------------------------------------------------------------------------------
daily = msia_cases[['date','year_month','cases_new']]
vaccina = vax_msia[['date','year_month','daily']]
daily_vaccina = daily.merge(vaccina,left_on=['date','year_month'],right_on=['date','year_month'],how='left')
daily_vaccina.rename(columns = {'cases_new':'New Cases','daily':'Number of Vaccination'}, inplace = True)
daily_vaccina.fillna(0,inplace=True)
daily_vaccina=daily_vaccina.loc[daily_vaccina['date']>='2021-01-24']
daily_vaccina.drop(columns=['date'],inplace=True)
#--------------------------------------------------------------------------------------------
left_column, right_column= st.columns(2)
with left_column:
    daily_vaccina=daily_vaccina.groupby(['year_month'], as_index = False).sum()
    g=alt.Chart(daily_vaccina,title='The new cases after vaccination start?').mark_line().encode(
        x="year_month",
        y="New Cases"
    ).properties(
        width=1000,
        height=350
    )
    st.altair_chart(g, use_container_width=True)

with right_column:
    daily_vaccina=daily_vaccina.groupby(['year_month'], as_index = False).sum()
    g=alt.Chart(daily_vaccina,title='The number of vaccination in every month').mark_line().encode(
        x="year_month",
        y="Number of Vaccination"
    ).properties(
        width=1000,
        height=350
    )
    st.altair_chart(g, use_container_width=True)

text7 = '<p style="font-family:Time-New-Roman; font-size: 15px;text-align: justify;">Based on the graphs above, we can see that the vaccination has been started and increase rapidly in July and August. Besides, the cases every day also increase rapidly in August but start to decrease in September and October. Based on the observation above, we can conclude that the cases has been affected by the vaccine since received and adapt the vaccine needs about 2 months.since the vaccination has been start on July with a large amount of receive and the cases decrease rapidly in September.</p>'
st.markdown(text7, unsafe_allow_html=True)

#-----------------------------------------------------------------------------------------
case=state_cases.loc[state_cases['year']==2021]
daily = case[['year_month','state','cases_new']]
vaccina = vax_state[['date','year_month','state','daily']]
daily.fillna(0,inplace=True)
vaccina.fillna(0,inplace=True)
#-----------------------------------------------------------------------------------------
daily=daily.groupby(['year_month','state'], as_index = False).sum()
text5 = '<p style="font-family:Time-New-Roman; font-size: 15px;text-align: justify;"></p>'
st.markdown(text5, unsafe_allow_html=True) 
left_column, right_column= st.columns([5,2])
with left_column:
    
    g=alt.Chart(daily,title='New cases in every states by month').mark_line().encode(
        x="year_month",
        y='cases_new',
        color = alt.Color('state', scale=alt.Scale(scheme = 'category20'))
    ).properties(
        width=1000,
        height=300
    )
    st.altair_chart(g, use_container_width=True)

with right_column:
    text6_1 = '<p style="font-family:Time-New-Roman;font-size: 15px;text-align: justify;"> To approve the conclusion, we can observe the graph above. We can just observe one of the state with the highest number of cases in July until September which is Selangor.We can see that the cases of Selangor has been decreased rapidly in September.</p>'
    st.markdown(text6_1 , unsafe_allow_html=True)
        
left_column, right_column= st.columns([5,2])
with left_column:
    vaccina=vaccina.groupby(['year_month','state'], as_index = False).sum()
    g=alt.Chart(vaccina,title='Number of vaccination in every states by month').mark_line().encode(
        x="year_month",
        y='daily',
        color = alt.Color('state', scale=alt.Scale(scheme = 'category20'))
    ).properties(
        width=1000,
        height=300
    )
    st.altair_chart(g, use_container_width=True)

with right_column:
    text6_1 = '<p style="font-family:Time-New-Roman;font-size: 15px;text-align: justify;"> We can also see that citizens of Selangor has the highest number of receiving on vaccination.</p>'
    st.markdown(text6_1 , unsafe_allow_html=True)
text5 = '<p style="font-family:Time-New-Roman; font-size: 15px;text-align: justify;"></p>'
st.markdown(text5, unsafe_allow_html=True) 
st.markdown(text5, unsafe_allow_html=True) 
#----------------------------------------------------------------------------------
after_vacc=df_clusters.loc[df_clusters['date_announced']>='2021-03-24']
before_vacc=df_clusters.loc[df_clusters['date_announced']<'2021-03-24']
after_vacc_c = after_vacc['cluster'].count()
before_vacc_c = before_vacc['cluster'].count()
df_clusters['year_month'] = pd.to_datetime(df_clusters['date_announced'], format='%Y-%m-%d').apply(lambda x: x.strftime('%Y-%m'))
#---------------------------------------------------------------------------------------
title5 = '<p style="font-family:Time-New-Roman; font-size: 24px;">Have the clusters reduced after vaccination is started in Malaysia?</p>' 
st.markdown(title5, unsafe_allow_html=True)
left_column, right_column= st.columns([5,2])
with left_column:
    data = {'Type': ['Before Vaccination', 'After Vaccination'], 'Total': [before_vacc_c,after_vacc_c]}  
    sum_df =pd.DataFrame(data = data,columns = ['Type','Total'])
    chart=alt.Chart(sum_df,title='Number of cluster before/after vaccination start in Malaysia?').mark_bar().encode(
        x='Total',
        y='Type',
        color=alt.Color('Type', scale=alt.Scale(scheme = 'purples'))
    ).properties(
        width=900,
        height=250
    )
    text = alt.Chart(sum_df).mark_text(dx=-20, dy=1,color='white').encode(
        x=alt.X('Total', stack='zero'),
        y=alt.Y('Type'),
        text=alt.Text('Total')
    )
    g=chart + text
    st.altair_chart(g, use_container_width=True)
with right_column:
    text8 = '<p style="font-family:Time-New-Roman; font-size: 15px;text-align: justify;">Based on the bar graph, the number of cluster does not decrease when vaccination has been start after 1 month. We can observe that number of cluster has been increase about 200% of clusters before vaccination..</p>'
    st.markdown(text8, unsafe_allow_html=True)

#----------------------------------------------------------------------------------------------
count_cluster =df_clusters[['year_month','cluster']].groupby('year_month', as_index = False).count()
#----------------------------------------------------------------------------------------------
left_column, right_column= st.columns([5,2])
with left_column:
    chart=alt.Chart(count_cluster,title='Number of cluster before/after vaccination start in Malaysia').mark_bar().encode(
        x='year_month',
        y='cluster',
        color=alt.Color('cluster', scale=alt.Scale(scheme = 'viridis'))
    ).properties(
        width=900,
        height=350
    )
    text = alt.Chart(count_cluster).mark_text(dx=1, dy=-5,color='black').encode(
        x=alt.X('year_month'),
        y=alt.Y('cluster', stack='zero'),
        text=alt.Text('cluster')
    )
    g=chart + text
    st.altair_chart(g, use_container_width=True)
with right_column:
    text8 = '<p style="font-family:Time-New-Roman; font-size: 15px;text-align: justify;">The bar chart shows that number of cluster in every month. We can see that number of cluster increase rapidly especially in May 2021 until August 2021 and start decreasing in September 2021.August 2021 has the highest number of cluster which has 1052 clusters, but March 2020 has the lowest number of cluster which is 5 clusters since the pandemic just started at that time.</p>'
    st.markdown(text8, unsafe_allow_html=True)

#----------------------------------------------------------------------------------------------
a_category =after_vacc[['cluster','category']].groupby('category', as_index = False).count()
b_category=before_vacc[['cluster','category']].groupby('category', as_index = False).count()
#---------------------------------------------------------------------------------------------
left_column, right_column= st.columns(2)
with left_column:
    chart=alt.Chart(b_category,title='Number of cluster before vaccination start').mark_bar().encode(
        x='category',
        y="cluster",
        color=alt.Color('cluster', scale=alt.Scale(scheme = 'plasma'))
    ).properties(
        width=700,
        height=350
    )
    text = alt.Chart(b_category).mark_text(dx=1, dy=-5,color='black').encode(
        x=alt.X('category'),
        y=alt.Y("cluster", stack='zero'),
        text=alt.Text('cluster')
    )
    g=chart + text
    st.altair_chart(g, use_container_width=True)
    text8 = '<p style="font-family:Time-New-Roman; font-size: 15px;text-align: justify;">The graph shows the number of cluster in every category before vaccination start. We can observe that workplace and commnuity have a lot of clusters which is 769 and 287 of clusters.Other categories only have a little of clusters which is lower than 100 of clusters.</p>'
    st.markdown(text8, unsafe_allow_html=True)

with right_column:
    chart=alt.Chart(a_category,title='Number of cluster after vaccination start').mark_bar().encode(
        x='category',
        y="cluster",
        color=alt.Color('cluster', scale=alt.Scale(scheme = 'set1'))
    ).properties(
        width=700,
        height=350
    )
    #add value for each bar
    text = alt.Chart(a_category).mark_text(dx=1, dy=-5,color='black').encode(
        x=alt.X('category'),
        y=alt.Y("cluster", stack='zero'),
        text=alt.Text('cluster')
    )
    g=chart + text
    st.altair_chart(g, use_container_width=True)
    text8 = '<p style="font-family:Time-New-Roman; font-size: 15px;text-align: justify;">The bar graph shows the number of cluster in every category before vaccination start. We can observe that workplace and commnuity also have a lot of clusters which is 2388 and 1367 of clusters.But clusters in other categories has been increases to 230 and lower of clusters which is different before vaccination start. However, workplace and commnunity still has the highest number of clusters which is the same during the before vaccination start.</p>'
    st.markdown(text8, unsafe_allow_html=True)

#------------------------------------------------------------------------------------------
after_vacc_end=after_vacc['cluster'].loc[after_vacc['status']=='ended'].count()
after_vacc_active=after_vacc['cluster'].loc[after_vacc['status']=='active'].count()
before_vacc_end=before_vacc['cluster'].loc[before_vacc['status']=='ended'].count()
before_vacc_active=before_vacc['cluster'].loc[before_vacc['status']=='active'].count()
data = {'Vaccination':['Before Vaccination','After Vaccination'],'Ended Cluster':[before_vacc_end,after_vacc_end],'Active Cluster': [before_vacc_active,after_vacc_active]}  
df =pd.DataFrame(data = data,columns = ['Vaccination','Ended Cluster','Active Cluster'])
df=df.groupby('Vaccination', as_index = False).sum()
df = df.melt("Vaccination", var_name='type',  value_name='vals')
df  =df[df!=0]
#-------------------------------------------------------------------------------------------
text5 = '<p style="font-family:Time-New-Roman; font-size: 15px;text-align: justify;"></p>'
st.markdown(text5, unsafe_allow_html=True) 
left_column, right_column= st.columns([5,2])
with left_column:
    chart=alt.Chart(df,title='Status of cluster').mark_bar().encode(
        x='vals',
        y='Vaccination',
        color= alt.Color('type', scale=alt.Scale(scheme = 'purples')),
        order=alt.Order(
          # Sort the segments of the bars by this field
          'type',
          sort='ascending'
        )
    ).properties(
        width=900,
        height=200
    )
    #add value for each bar
    text = alt.Chart(df).mark_text(dx=-15, dy=1,color='black').encode(
        x=alt.X('vals'),
        y=alt.Y('Vaccination'),
        text=alt.Text('vals')
    )
    g=chart + text
    st.altair_chart(g, use_container_width=True)
with right_column:
    text8 = '<p style="font-family:Time-New-Roman; font-size: 15px;text-align: justify;">The graph shows the status of cluster before and after the vaccination start. Although there are a lot of cluster after vaccination start, only 506 of clusters still active until now, other 3919 of clusters which is more than 70% of clusters have been ended.</p>'
    st.markdown(text8, unsafe_allow_html=True)
#------------------------------------------------------------------------------------------------
daily = msia_cases[['date','year_month','cases_recovered','deaths_new','deaths_new_dod','deaths_pvax','deaths_fvax']]
vaccina = vax_msia[['date','year_month','daily']]
recover_dealth_vaccina = daily.merge(vaccina,left_on=['date','year_month'],right_on=['date','year_month'],how='left')
recover_dealth_vaccina.rename(columns = {'deaths_new': 'Death cases', 'cases_recovered': 'Recovered cases','deaths_pvax':'Death people with partial vaccination','deaths_fvax':'Death people with full vaccination'}, inplace = True)
after_vacc=recover_dealth_vaccina.loc[recover_dealth_vaccina['date']>='2021-02-24']
#-----------------------------------------------------------------------------------------------
text5 = '<p style="font-family:Time-New-Roman; font-size: 15px;text-align: justify;"></p>'
st.markdown(text5, unsafe_allow_html=True) 
text5 = '<p style="font-family:Time-New-Roman; font-size: 15px;text-align: justify;"></p>'
st.markdown(text5, unsafe_allow_html=True) 
title6 = '<p style="font-family:Time-New-Roman; font-size: 24px;">Does the vaccination affect the recovery and death cases?</p>' 
st.markdown(title6, unsafe_allow_html=True)

left_column, mid_column,right_column= st.columns(3)
with left_column:
    after_vacc_r=after_vacc.groupby(['year_month'], as_index = False).sum()
    #create a line graph
    g=alt.Chart(after_vacc_r,title='The death cases cases after vaccination progress start?').mark_line().encode(
        x="year_month",
        y="Death cases"
    ).properties(
        width=700,
        height=350
    )
    st.altair_chart(g, use_container_width=True)
with mid_column:
    after_vacc_r=after_vacc.groupby(['year_month'], as_index = False).sum()
    g=alt.Chart(after_vacc_r,title='The recovered cases after vaccination progress start?').mark_line().encode(
        x="year_month",
        y="Recovered cases"
    ).properties(
        width=700,
        height=350
    )
    st.altair_chart(g, use_container_width=True)
with right_column:
    after_vacc_r=after_vacc.groupby(['year_month'], as_index = False).sum()
    #create a line graph
    g=alt.Chart(after_vacc_r,title='The vaccination by month').mark_line().encode(
        x="year_month",
        y="daily"
    ).properties(
        width=700,
        height=350
    )
    st.altair_chart(g, use_container_width=True)
    
text13 = '<p style="font-family:Time-New-Roman;font-size: 15px;text-align: justify;">Based on the graphs above shows the trend of the death cases, vaccination, and recovered cases. We can observe that the vaccination had been start since February and increase rapidly from June until August.Besides, the cases of death and recovered had been increased in July until September. Based on the trend above, we can conclude that the vaccination can affect the cases of death and recovered.It is because a complete injection of vaccine needs about 2 months. So, when the we can see that the cases start to decrease in October since two months before: August has the highest number of receiving vaccination. </p>'
st.markdown(text13, unsafe_allow_html=True)

#------------------------------------------------------------------------------------------
test=after_vacc[['year_month','deaths_new_dod','Death people with partial vaccination','Death people with full vaccination']]
test=test.groupby(['year_month'], as_index = False).sum()
test['death in partial(%)'] =test ['Death people with partial vaccination']/test ['deaths_new_dod']*100
test ['death in full(%)'] =test ['Death people with full vaccination']/test ['deaths_new_dod']*100
test ['death(%)'] =test ['deaths_new_dod']/test ['deaths_new_dod']*100
test ['death(%)'] =test ['death(%)']-test ['death in full(%)']-test ['death in partial(%)']
test = test[['year_month','death in full(%)','death in partial(%)','death(%)']]
test =test[test!=0]
test = test.melt("year_month", var_name='type',  value_name='vals')
#-------------------------------------------------------------------------------------------

chart = alt.Chart(test,title='The percentage of death cases with vaccination').mark_bar().encode(
    x='year_month',
    y='vals',
    color= alt.Color('type', scale=alt.Scale(scheme = 'greenblue')),
    order=alt.Order(
      'type',
      sort='ascending'
    )
).properties(
    width=1250,
    height=350
)

text = alt.Chart(test).mark_text(dx=1, dy=5,color='black').encode(
    x=alt.X('year_month'),
    y=alt.Y('vals', stack='zero'),
    text=alt.Text('vals', format='.1f'),
    order=alt.Order(
      'type',
      sort='ascending'
    )
)
g=chart + text
st.altair_chart(g, use_container_width=True)

text13 = '<p style="font-family:Time-New-Roman;font-size: 15px;text-align: justify;">Based on the graph, we can know that the death cases of citizen with vaccination start increasing in May 2021. In addition, the highest percentage of death cases of citizen with partial vaccination is August 2021 with 29% of death cases.However, October has the highest percentage of citizens with full vaccination death cases which is 44.3% of death cases. </p>'
st.markdown(text13, unsafe_allow_html=True)
text5 = '<p style="font-family:Time-New-Roman; font-size: 15px;text-align: justify;"></p>'
st.markdown(text5, unsafe_allow_html=True) 
text5 = '<p style="font-family:Time-New-Roman; font-size: 15px;text-align: justify;"></p>'
st.markdown(text5, unsafe_allow_html=True) 
#------------------------------------------------------------------------------------------------
reg_type =vax_msia[['date','year_month','mysj','call','web']]
reg_type=reg_type.loc[reg_type['date']>='2021-06-24']
reg_type.drop(columns=['date'],inplace=True)
reg_type =reg_type.groupby('year_month').diff()
reg_type['year_month'] =vax_msia['year_month']
reg_type=reg_type.groupby(['year_month']).sum()
reg_type[reg_type < 0] = 0
reg_type = reg_type.reset_index()
reg_type= reg_type.melt('year_month', var_name='type',  value_name='vals')
#-----------------------------------------------------------------------------------------------
text5 = '<p style="font-family:Time-New-Roman; font-size: 15px;text-align: justify;"></p>'
st.markdown(text5, unsafe_allow_html=True) 
text5 = '<p style="font-family:Time-New-Roman; font-size: 15px;text-align: justify;"></p>'
st.markdown(text5, unsafe_allow_html=True) 
title6 = '<p style="font-family:Time-New-Roman; font-size: 24px;">How do the citizens of Malaysia register for the vaccination and which has the highest number of registration?</p>' 
st.markdown(title6, unsafe_allow_html=True)
left_column, right_column= st.columns([5,2])
with left_column:
    g=alt.Chart(reg_type,title='Number of registration in every register type').mark_bar().encode(
        x='vals',
        y='year_month',
        color= alt.Color('type', scale=alt.Scale(scheme = 'set2'))
    ).properties(
        width=900,
        height=250
    )
    st.altair_chart(g, use_container_width=True)
with right_column:
    text14 = '<p style="font-family:Time-New-Roman;font-size: 15px;text-align: justify;">Based on the stacked bar graph, we found that most of the citizen in Malaysia register their vaccine through MySejahtera, only a few Malaysia citizen register through web and calling.</p>'
    st.markdown(text14, unsafe_allow_html=True)

#------------------------------------------------------------------------------------------------
reg_state_type =vax_state[['date','state','mysj','call','web']]
reg_state_type =reg_state_type.loc[reg_state_type ['date']>='2021-06-24']
reg_state_type .drop(columns=['date'],inplace=True)
reg_state_type =reg_state_type.groupby('state').diff()
reg_state_type['state'] =vax_state['state']
reg_state_type['year_month'] =vax_state['year_month']
reg_state_type=reg_state_type.groupby(['year_month','state']).sum()
reg_state_type[reg_state_type < 0] = 0
reg_state_type= reg_state_type.reset_index()
#------------------------------------------------------------------------------------------------
left_column, mid_column,right_column= st.columns(3)
with left_column:
    g=alt.Chart(reg_state_type,title=' MySejahtera ').mark_line().encode(
        x="year_month",
        y="mysj",
        color = alt.Color('state', scale=alt.Scale(scheme = 'category20'))
    ).properties(
        width=500,
        height=300
    )
    st.altair_chart(g, use_container_width=True)
    text15 = '<p style="font-family:Time-New-Roman;font-size: 15px;text-align: justify;">We can observe that most of the registration are in July and August, especially in Selangor and Johor. Besides, the registration of vaccination is decreasing.</p>'
    st.markdown(text15, unsafe_allow_html=True)
with mid_column:
    g=alt.Chart(reg_state_type,title=' Web ').mark_line().encode(
        x="year_month",
        y="web",
        color = alt.Color('state', scale=alt.Scale(scheme = 'category20'))
    ).properties(
        width=500,
        height=300
    )
    st.altair_chart(g, use_container_width=True)
    text15 = '<p style="font-family:Time-New-Roman;font-size: 15px;text-align: justify;">Based on the graph, we know that only June and July have vaccine registration through website. Then, Perak and Johor has the highest number of registration using website.</p>'
    st.markdown(text15, unsafe_allow_html=True)
with right_column:
    g=alt.Chart(reg_state_type,title=' Calling ').mark_line().encode(
        x="year_month",
        y="call",
        color = alt.Color('state', scale=alt.Scale(scheme = 'category20'))
    ).properties(
        width=500,
        height=300
    )
    st.altair_chart(g, use_container_width=True)
    text15 = '<p style="font-family:Time-New-Roman;font-size: 15px;text-align: justify;">Based on the graph, we can know that vaccine registration through calling is very not popular in Malaysia. The highest number of registration is only 170 of registration per month which is from Selangor.Besides, the registration through calling has been decrease after August 2021.</p>'
    st.markdown(text15, unsafe_allow_html=True)
text5 = '<p style="font-family:Time-New-Roman; font-size: 15px;text-align: justify;"></p>'
st.markdown(text5, unsafe_allow_html=True) 
#----------------------------------------------------------------------------------------------
reg_type =vax_msia[['mysj','call','web']].tail(2)
pd.set_option('display.float_format', '{:.1f}'.format)
reg_type=reg_type.sum()
data = {'Type': ['MySejahtera', 'Call','Web'], 'Total': [reg_type.mysj,reg_type.call,reg_type.web]}  
sum_df =pd.DataFrame(data = data,columns = ['Type','Total'])
sum_df = sum_df.melt('Type', var_name='type',  value_name='vals')
#----------------------------------------------------------------------------------------------
left_column, right_column= st.columns([5,2])
with left_column:
    chart = alt.Chart(sum_df,title='Total number of Vaccine Registration in every registration method').mark_bar().encode(
        x='vals',
        y='Type',
        color= alt.Color('Type', scale=alt.Scale(scheme = 'reds')),
    ).properties(
        width=900,
        height=300
    )

    text = alt.Chart(sum_df).mark_text(dx=25, dy=1,color='black').encode(
        x=alt.X('vals', stack='zero'),
        y=alt.Y('Type'),
        text=alt.Text('vals', format='.0f')
    )

    g=chart + text
    st.altair_chart(g, use_container_width=True)
    
with right_column:
    text15 = '<p style="font-family:Time-New-Roman;font-size: 15px;text-align: justify;">Above shown the total number of vaccine registration from every types of registration. We can observe that Calling only have 22096 of registration and Web only have 2281697 of registrations,but MySejahtera has a very high number of registration which is 2000K number of registrations.</p>'
    st.markdown(text15, unsafe_allow_html=True)
#--------------------------------------------------------------------------------------------
total_vac=vax_state.loc[vax_state['date']>='2021-06-24']
total_vac = total_vac[['state','daily_partial']]
total_vac=total_vac.groupby(['state']).sum()
total_reg = vax_state[['state','total']].tail(16)
progress = total_vac.merge(total_reg,left_on=['state'],right_on=['state'],how='left')
progress['sucess rate(%)'] = (progress['daily_partial']/progress['total'])*100
progress['no sucess rate(%)'] =100- progress['sucess rate(%)'] 
progress=progress.groupby('state').sum()
progress[progress < 0] = 0
progress[progress > 100] = 100
progress = progress.reset_index()
progress = progress[['state','sucess rate(%)','no sucess rate(%)']]
progress=progress[progress!=0]
progress = progress.melt('state', var_name='type',  value_name='vals')
#-------------------------------------------------------------------------------------------
text5 = '<p style="font-family:Time-New-Roman; font-size: 15px;text-align: justify;"></p>'
st.markdown(text5, unsafe_allow_html=True) 
text5 = '<p style="font-family:Time-New-Roman; font-size: 15px;text-align: justify;"></p>'
st.markdown(text5, unsafe_allow_html=True) 
title6 = '<p style="font-family:Time-New-Roman; font-size: 24px;">What is the sucessful rate of vaccination in every state?</p>' 
st.markdown(title6, unsafe_allow_html=True)

left_column, right_column= st.columns([5,2])
with left_column:
    chart=alt.Chart(progress,title='Sucessful rate of vaccination in every states').mark_bar().encode(
        x='vals',
        y='state',
        color= alt.Color('type', scale=alt.Scale(scheme = 'set1'))
    ).properties(
        width=900,
        height=300
    )
    #add data value on each bar
    text = alt.Chart(progress).mark_text(dx=-15, dy=1,color='black').encode(
        x=alt.X('vals', stack='center'),
        y=alt.Y('state'),
        text=alt.Text('vals', format='.1f')
    )
    g=chart + text
    st.altair_chart(g, use_container_width=True)

with right_column:
    text18 = '<p style="font-family:Time-New-Roman; font-size: 15px;text-align: justify;">Based on the stacked bar chart, most of the sucess rate in every state are near to 80%. Only few states is near to 70% and below which are Perlis, Sarawak, Selangor, and Labuan.But Sabah, Kuala Lumpur and Putrajaya have high sucess rate which is 99.3% in Sabah and 100% in Kuala Lumpur and Putrajaya.</p>'
    st.markdown(text18, unsafe_allow_html=True)
#----------------------------------------------------------------------------------------------
total_vac =vax_state[['state','cumul_partial','cumul_full']].tail(16)
state =df_static.drop(0)
state =state[['state','pop']]
progress = state.merge(total_vac,left_on=['state'],right_on=['state'],how='left')
progress['progress partial(%)'] = (progress['cumul_partial']/progress['pop'])*100
progress['progress full(%)'] = (progress['cumul_full']/progress['pop'])*100
progress['progress full/partial(%)'] = (progress['cumul_full']/progress['cumul_partial'])*100
progress_fp =progress[['state','progress partial(%)','progress full(%)']]
progress_fp=progress_fp.groupby('state', as_index = False).sum()
progress_fp = progress_fp.melt('state', var_name='type',  value_name='vals')
#-----------------------------------------------------------------------------------------------
text5 = '<p style="font-family:Time-New-Roman; font-size: 15px;text-align: justify;"></p>'
st.markdown(text5, unsafe_allow_html=True) 
text5 = '<p style="font-family:Time-New-Roman; font-size: 15px;text-align: justify;"></p>'
st.markdown(text5, unsafe_allow_html=True) 
title6 = '<p style="font-family:Time-New-Roman; font-size: 24px;">What is the vaccination progress in every state?</p>' 
st.markdown(title6, unsafe_allow_html=True)

chart=alt.Chart(progress_fp).mark_bar().encode(
    x='type:O',
    y='vals:Q',
    color='type:N',
    
)
#add value for each bar
text = chart.mark_text(
    align='center',
    baseline='middle',
    dy=-5  
).encode(
    text=alt.Text('vals:Q', format='.1f')
)
g=alt.layer(chart, text, data=progress_fp).facet(column='state:N',title='Partial/Full Vaccination progress in every state'
)
st.altair_chart(g, use_container_width=True)

text17 = '<p style="font-family:Time-New-Roman; font-size: 15px;text-align: justify;">The graph shows the percentage of vaccination progress in every state. Based on the graph above, only Kuala Lumpur and Putrajaya has more than 100% of people has been received vaccination.Other states are only 85% and below of people has been received vaccination, especially Sabah has the lowest percentage of vaccination progress which is 56.7% of full vaccination and 60.7% of partial vaccination.</p>'
st.markdown(text17, unsafe_allow_html=True)

#--------------------------------------------------------------------------------------------
progress['No Full people'] = progress['pop']-progress['cumul_full']
progress_fnf=progress.groupby('state').sum()
progress_fnf[progress_fnf < 0] = 0
progress_fnf = progress_fnf.reset_index()
progress_fnf=progress_fnf[progress_fnf!=0]
progress_fnf =progress_fnf[['state','cumul_full','No Full people']]
progress['No partial people'] = progress['pop']-progress['cumul_partial']
progress_pnf=progress.groupby('state').sum()
progress_pnf[progress_pnf < 0] = 0
progress_pnf = progress_pnf.reset_index()
progress_pnf =progress_pnf[['state','cumul_partial','No partial people']]
progress_pnf=progress_pnf[progress_pnf!=0]
progress_pnf = progress_pnf .melt('state', var_name='type',  value_name='vals')
progress_fnf = progress_fnf .melt('state', var_name='type',  value_name='vals')
#--------------------------------------------------------------------------------------------

left_column, right_column= st.columns(2)
with left_column:
    chart=alt.Chart(progress_fnf,title='Progress of fully vaccination in every states').mark_bar().encode(
        x='state',
        y='vals',
        color= alt.Color('type', scale=alt.Scale(scheme = 'set1'))
    ).properties(
        width=700,
        height=1000
    )
    #add value for each stacked bar
    text = alt.Chart(progress_fnf).mark_text(dx=1, dy=-5,color='black').encode(
        x=alt.X('state'),
        y=alt.Y('vals', stack='zero'),
        text=alt.Text('vals', format='.0f')
    )
    g=chart + text
    st.altair_chart(g, use_container_width=True)

with right_column:
    chart=alt.Chart(progress_pnf,title='Progress of partial vaccination in every states').mark_bar().encode(
        x='state',
        y='vals',
        color= alt.Color('type', scale=alt.Scale(scheme = 'set2'))
    ).properties(
        width=700,
        height=1000
    )
    #add value for each stacked bar
    text = alt.Chart(progress_pnf).mark_text(dx=1, dy=-5,color='black').encode(
        x=alt.X('state'),
        y=alt.Y('vals', stack='zero'),
        text=alt.Text('vals', format='.0f')
    )
    g=chart + text
    st.altair_chart(g, use_container_width=True)
text18 = '<p style="font-family:Time-New-Roman; font-size: 18px;text-align: justify;">Based on the graph, some states like Selangor, Sabah, and Johor will have a slow vaccination progress because there are a lot of people in these states, so it will takes a long time to complete the vaccination.</p>'
st.markdown(text18, unsafe_allow_html=True)

#------------------------------------------------------------------------------------------------
totalpop =df_static['pop'].head(1).values[0]
seconddose =vax_msia['cumul_full'].tail(1).values[0]/totalpop*100
firstdose = vax_msia['cumul_partial'].tail(1).values[0]/totalpop*100 -seconddose
total =(totalpop/totalpop)*100-firstdose-seconddose
data = {'Type': [ 'Second Dose','First Dose','Unvaccinated'], 'Total': [seconddose,firstdose,total]}  
sum_df =pd.DataFrame(data = data,columns = ['Type','Total'])
sum_df = sum_df.melt('Type', var_name='type',  value_name='vals')
#------------------------------------------------------------------------------
text5 = '<p style="font-family:Time-New-Roman; font-size: 15px;text-align: justify;"></p>'
st.markdown(text5, unsafe_allow_html=True) 
text5 = '<p style="font-family:Time-New-Roman; font-size: 15px;text-align: justify;"></p>'
st.markdown(text5, unsafe_allow_html=True) 
title6 = '<p style="font-family:Time-New-Roman; font-size: 24px">How many citizens of Malaysia have the first dose of vaccine and how many of them have completed the vaccination?</p>' 
st.markdown(title6, unsafe_allow_html=True)
left_column, right_column= st.columns([5,2])
with left_column:
    chart = alt.Chart(sum_df,title='Total number of receiving by every types of vaccine').mark_bar().encode(
        x='vals',
        y='type',
        color= alt.Color('Type', scale=alt.Scale(scheme = 'blues')),
        order=alt.Order(
          'type',
          sort='ascending'
        )
    ).properties(
        width=900,
        height=150
    )
    text = alt.Chart(sum_df).mark_text(dx=-15, dy=1,color='black').encode(
        x=alt.X('vals', stack='zero'),
        y=alt.Y('type'),
        text=alt.Text('vals', format='.2f'),
        order=alt.Order(
          'type',
          sort='ascending'
        )
    )

    g=chart + text
    st.altair_chart(g, use_container_width=True)
with right_column:
    text19 = '<p style="font-family:Time-New-Roman; font-size: 15px;text-align: justify;">Based on the stacked bar chart, we can observed that there are near to 80% of population in Malaysia have been start their vaccination which is at least taking the first dose of the vaccine.Besides, there are  73.62% of population in Malaysia had been took the second dose of vaccine. </p>'
    st.markdown(text19, unsafe_allow_html=True)

Dose = vax_msia[['year_month','daily_partial','daily_full']]
Dose=Dose.groupby(['year_month'], as_index = False).sum()
Dose.rename(columns = {'daily_partial':'Partial Vaccination','daily_full':'Full Vaccination'}, inplace = True)
Dose = Dose.melt('year_month', var_name='type',  value_name='vals')
left_column, right_column= st.columns([5,2])
with left_column:
    chart=alt.Chart(Dose).mark_bar().encode(
        x='type:O',
        y='vals:Q',
        color='type:N'
    )
    text = chart.mark_text(
        align='center',
        baseline='middle',
        dy=-5  
    ).encode(
        text=alt.Text('vals', format='.0f')
    )
    g=alt.layer(chart, text, data=Dose).facet(column='year_month:N',title='Vaccination progress in Malaysia by month'
    )
    st.altair_chart(g, use_container_width=True)
with right_column:
    text19 = '<p style="font-family:Time-New-Roman; font-size: 15px;text-align: justify;">Based on the bar chart, the vaccination given to the citizen of Malaysia had been increase rapidly start from June 2021, but it starts decreasing in September until now.The highest number of received partial vaccination is about 8200K in July and 8300K of citizen Malaysia complete their vaccination in August. </p>'
    st.markdown(text19, unsafe_allow_html=True)

#--------------------------------------------------------------------------------------
type_vax= vax_msia[['pfizer1','sinovac1','astra1','cansino']]
type_vax=type_vax.sum()
data = {'Type': ['Pfizer', 'Sinovac','AZ','Cansino'], 'Total': [type_vax.pfizer1,type_vax.sinovac1,type_vax.astra1,type_vax.cansino]}  
sum_df =pd.DataFrame(data = data,columns = ['Type','Total'])
sum_df = sum_df.melt('Type', var_name='type',  value_name='vals')
#----------------------------------------------------------------------------------------------
text5 = '<p style="font-family:Time-New-Roman; font-size: 15px;text-align: justify;"></p>'
st.markdown(text5, unsafe_allow_html=True) 
text5 = '<p style="font-family:Time-New-Roman; font-size: 15px;text-align: justify;"></p>'
st.markdown(text5, unsafe_allow_html=True) 
title6 = '<p style="font-family:Time-New-Roman; font-size: 24px">Which type of vaccine has mostly been received by citizens of Malaysia?</p>' 

st.markdown(title6, unsafe_allow_html=True)
left_column, right_column= st.columns([4,3])
with left_column:
    chart = alt.Chart(sum_df,title='Number of citizens with First Dose/ Second Dose vaccine').mark_bar().encode(
        x='vals',
        y='Type',
        color= alt.Color('Type', scale=alt.Scale(scheme = 'blues')),
    ).properties(
        width=750,
        height=150
    )
    #add value to each bar
    text = alt.Chart(sum_df).mark_text(dx=25, dy=1,color='black').encode(
        x=alt.X('vals', stack='zero'),
        y=alt.Y('Type'),
        text=alt.Text('vals', format='.0f')
    )

    g=chart + text
    st.altair_chart(g, use_container_width=True)
with right_column:
    text19 = '<p style="font-family:Time-New-Roman; font-size: 15px;text-align: justify;">The graph shows the total number of vaccination received in every types of vaccine. We can observe that Pfizer and Sinovac has a large amount of receive compare to the AZ and Cansino. Especially Cansino only has 160K of receive.</p>'
    st.markdown(text19, unsafe_allow_html=True)

#------------------------------------------------------------------------------------------
vax_type =vax_msia[['year_month','pfizer1','sinovac1','astra1','cansino']]
vax_type.rename(columns = {'pfizer1':'Pfizer','sinovac1':'Sinovac','astra1':'AZ','cansino':'Cansino'}, inplace = True)
#------------------------------------------------------------------------------------------

left_column, right_column= st.columns(2)
with left_column:
    month_type = vax_type.melt('year_month', var_name='type',  value_name='vals')
    month_type=month_type.groupby(['year_month','type'], as_index = False).sum()
    g=alt.Chart(month_type,title='Vaccine reception of every types of vaccine in every month').mark_line().encode(
        x="year_month",
        y="vals",
        color = alt.Color('type', scale=alt.Scale(scheme = 'category20'))
    ).properties(
        width=1000,
        height=300
    )
    st.altair_chart(g, use_container_width=True)
#-----------------------------------------------------------------------------------------------
vax_type.rename(columns = {'pfizer1':'Pfizer','sinovac1':'Sinovac','astra1':'AZ','cansino':'Cansino'}, inplace = True)
vax_type=vax_type.groupby(['year_month'], as_index = False).sum()
vax_type['Total(%)']= vax_type['Cansino']+vax_type['AZ']+vax_type['Sinovac']+vax_type['Pfizer']
vax_type['Cansino(%)'] =vax_type['Cansino']/vax_type['Total(%)']*100
vax_type['AZ(%)'] =vax_type['AZ']/vax_type['Total(%)']*100
vax_type['Sinovac(%)'] =vax_type['Sinovac']/vax_type['Total(%)']*100
vax_type['Pfizer(%)'] =vax_type['Pfizer']/vax_type['Total(%)']*100
vax_type =vax_type[['year_month','Cansino(%)','AZ(%)','Sinovac(%)','Pfizer(%)']]
vax_type = vax_type.melt('year_month', var_name='type',  value_name='vals')
vax_type =vax_type[vax_type!=0]
#------------------------------------------------------------------------------------------------

with right_column:
    g=alt.Chart(vax_type,title='Percentage of Vaccine reception in every types of vaccine').mark_bar().encode(
        x='year_month',
        y='vals',
        color= alt.Color('type', scale=alt.Scale(scheme = 'set2')),
        order=alt.Order(
      'vals',
      sort='ascending'
    )
    ).properties(
        width=800,
        height=300
    )
    st.altair_chart(g, use_container_width=True)


text19 = '<p style="font-family:Time-New-Roman; font-size: 15px;text-align: justify;">Based on the graph, Pfizer has been kept receiving by the Malaysia citizen from the beginning of vaccination start until now. Sinovac has start provide from April 2021 and has the highest amount of receive in July which is about 4500K of receive, but decrease extremely in September 2021.AZ also almost same with the Sinovac which is start in May and keep decreasing until September 2021. Only the Cansino has been started recently which is August 2021.</p>'
st.markdown(text19, unsafe_allow_html=True)

#=================================================================================================
boruta_ad_30= pd.read_csv('Feature Selection/boruta_admitted_30.csv')
boruta_ad_50= pd.read_csv('Feature Selection/boruta_admitted_50.csv')
boruta_ad_100= pd.read_csv('Feature Selection/boruta_admitted_100.csv')
boruta_new_30= pd.read_csv('Feature Selection/boruta_casesNew_30.csv')
boruta_new_50= pd.read_csv('Feature Selection/boruta_casesNew_50.csv')
boruta_new_100= pd.read_csv('Feature Selection/boruta_casesNew_100.csv')
boruta_icu_30= pd.read_csv('Feature Selection/boruta_ICU_30.csv')
boruta_icu_50= pd.read_csv('Feature Selection/boruta_ICU_50.csv')
boruta_icu_100= pd.read_csv('Feature Selection/boruta_ICU_100.csv')

rfe_ad_30= pd.read_csv('Feature Selection/RFE_admitted_30.csv')
rfe_ad_50= pd.read_csv('Feature Selection/RFE_admitted_50.csv')
rfe_ad_100= pd.read_csv('Feature Selection/RFE_admitted_100.csv')
rfe_new_30= pd.read_csv('Feature Selection/RFE_casesNew_30.csv')
rfe_new_50= pd.read_csv('Feature Selection/RFE_casesNew_50.csv')
rfe_new_100= pd.read_csv('Feature Selection/RFE_casesNew_100.csv')
rfe_icu_30= pd.read_csv('Feature Selection/RFE_ICU_30.csv')
rfe_icu_50= pd.read_csv('Feature Selection/RFE_ICU_50.csv')
rfe_icu_100= pd.read_csv('Feature Selection/RFE_ICU_100.csv')


boruta_ad_30.drop('Unnamed: 0',axis=1,inplace=True)
boruta_ad_50.drop('Unnamed: 0',axis=1,inplace=True)
boruta_ad_100.drop('Unnamed: 0',axis=1,inplace=True)
boruta_new_30.drop('Unnamed: 0',axis=1,inplace=True)
boruta_new_50.drop('Unnamed: 0',axis=1,inplace=True)
boruta_new_100.drop('Unnamed: 0',axis=1,inplace=True)
boruta_icu_30.drop('Unnamed: 0',axis=1,inplace=True)
boruta_icu_50.drop('Unnamed: 0',axis=1,inplace=True)
boruta_icu_100.drop('Unnamed: 0',axis=1,inplace=True)

rfe_ad_30.drop('Unnamed: 0',axis=1,inplace=True)
rfe_ad_50.drop('Unnamed: 0',axis=1,inplace=True)
rfe_ad_100.drop('Unnamed: 0',axis=1,inplace=True)
rfe_new_30.drop('Unnamed: 0',axis=1,inplace=True)
rfe_new_50.drop('Unnamed: 0',axis=1,inplace=True)
rfe_new_100.drop('Unnamed: 0',axis=1,inplace=True)
rfe_icu_30.drop('Unnamed: 0',axis=1,inplace=True)
rfe_icu_50.drop('Unnamed: 0',axis=1,inplace=True)
rfe_icu_100.drop('Unnamed: 0',axis=1,inplace=True)
#=================================================================================================
text5 = '<p style="font-family:Time-New-Roman; font-size: 15px;text-align: justify;"></p>'
st.markdown(text5, unsafe_allow_html=True) 
text5 = '<p style="font-family:Time-New-Roman; font-size: 15px;text-align: justify;"></p>'
st.markdown(text5, unsafe_allow_html=True) 
title6 = '<p style="font-family:Time-New-Roman; font-size: 32px;font-weight: bold">Feature Selection</p>' 
st.markdown(title6, unsafe_allow_html=True)
title6 = '<p style="font-family:Time-New-Roman; font-size: 24px">BORUTA</p>' 
st.markdown(title6, unsafe_allow_html=True)

text19 = '<p style="font-family:Time-New-Roman; font-size: 15px;text-align: justify;">In this project, we are going to predict 3 scenarios using various machine learning techniques and study their performances. The 3 scenarios are: </p>'
st.markdown(text19, unsafe_allow_html=True)
text19 = '<p style="font-family:Time-New-Roman; font-size: 15px;text-align: justify;"> i) daily covid cases of Malaysia </p>'
st.markdown(text19, unsafe_allow_html=True)
text19 = '<p style="font-family:Time-New-Roman; font-size: 15px;text-align: justify;">ii) daily admitted covid cases to hospital across Malaysia  </p>'
st.markdown(text19, unsafe_allow_html=True)
text19 = '<p style="font-family:Time-New-Roman; font-size: 15px;text-align: justify;">iii) daily ICU cases across Malaysia </p>'
st.markdown(text19, unsafe_allow_html=True)

text19 = '<p style="font-family:Time-New-Roman; font-size: 15px;text-align: justify;">In order to predict the scenarios, we have to combine the datasets and perform some pre-processing to get the variable we needed. For example, to predict the daily covid cases of Malaysia, we combine the data of daily Malaysia’s cases, daily states‘ cases, daily vaccine, daily death cases, and perform data preprocessing to calculate the covid cases before one day to two weeks.Our aim here to is create as many features as we could, and in the next step perform feature extraction to find the insight and filter out unimportant features.</p>'
st.markdown(text19, unsafe_allow_html=True)
text19 = '<p style="font-family:Time-New-Roman; font-size: 15px;text-align: justify;">Next, we are going to extract the features (independent variables) that strongly contribute to our scenarios. We have decided to use Boruta algorithm and Recursive Feature Elimination (RFE) as our feature selector. For each scenario, we will select the top 30, top 50 and top 100 features separately.By doing this, we can reduce the features number from 200-300++ to 30,50 and 100. The expander below shows the details of each selected feature for each scenario with Boruta and RFE respectively.   </p>'
st.markdown(text19, unsafe_allow_html=True)
text19 = '<p style="font-family:Time-New-Roman; font-size: 15px;text-align: justify;"> </p>'
st.markdown(text19, unsafe_allow_html=True)
with st.expander("Admitted cases"):
    left_column,mid, right_column= st.columns(3)
    with left_column:
        boruta_ad_30
        text19 = '<p style="font-family:Time-New-Roman; font-size: 15px;text-align: center;">Top 30 features</p>'
        st.markdown(text19, unsafe_allow_html=True)
    with mid:
        boruta_ad_50
        text19 = '<p style="font-family:Time-New-Roman; font-size: 15px;text-align: center;">Top 50 features</p>'
        st.markdown(text19, unsafe_allow_html=True)
    with right_column:
        boruta_ad_100
        text19 = '<p style="font-family:Time-New-Roman; font-size: 15px;text-align: center;">Top 100 features</p>'
        st.markdown(text19, unsafe_allow_html=True)
with st.expander("New Cases"):
    left_column,mid, right_column= st.columns(3)
    with left_column:
        boruta_new_30
        text19 = '<p style="font-family:Time-New-Roman; font-size: 15px;text-align: center;">Top 30 features</p>'
        st.markdown(text19, unsafe_allow_html=True)
    with mid:
        boruta_new_50
        text19 = '<p style="font-family:Time-New-Roman; font-size: 15px;text-align: center;">Top 50 features</p>'
        st.markdown(text19, unsafe_allow_html=True)
    with right_column:
        boruta_new_100
        text19 = '<p style="font-family:Time-New-Roman; font-size: 15px;text-align: center;">Top 100 features</p>'
        st.markdown(text19, unsafe_allow_html=True)
with st.expander("ICU"):
    left_column,mid, right_column= st.columns(3)
    with left_column:
        boruta_icu_30
        text19 = '<p style="font-family:Time-New-Roman; font-size: 15px;text-align: center;">Top 30 features</p>'
        st.markdown(text19, unsafe_allow_html=True)
    with mid:
        boruta_icu_50
        text19 = '<p style="font-family:Time-New-Roman; font-size: 15px;text-align: center;">Top 50 features</p>'
        st.markdown(text19, unsafe_allow_html=True)
    with right_column:
        boruta_icu_100
        text19 = '<p style="font-family:Time-New-Roman; font-size: 15px;text-align: center;">Top 100 features</p>'
        st.markdown(text19, unsafe_allow_html=True)
text19 = '<p style="font-family:Time-New-Roman; font-size: 15px;text-align: justify;">From the table above, we can see that covid cases 2 days before in Selangor, daily vaccine given in Sarawak and covid cases 4 days before in Selangor are the top 3 features that contribute to the scenario of daily covid cases of Malaysia. Besides, admitted cases one week before in Sarawak, admitted cases 5 days before in kedah and daily new cases in Selangor are the top 3 features contributing to the scenario of daily admitted covid cases to hospital across Malaysia. Moreover, admitted cases 5 days before in Negeri Sembilan, admitted cases 3 days before in Johor and admitted cases 4 days before in Kelantan are the top 3 features that contribute to the scenario of daily ICU cases across Malaysia </p>'
st.markdown(text19, unsafe_allow_html=True)

title6 = '<p style="font-family:Time-New-Roman; font-size: 24px">RFE</p>'
st.markdown(title6, unsafe_allow_html=True)

with st.expander("Admitted cases"):
    left_column,mid, right_column= st.columns(3)
    with left_column:
        rfe_ad_30
        text19 = '<p style="font-family:Time-New-Roman; font-size: 15px;text-align: center;">Top 30 features</p>'
        st.markdown(text19, unsafe_allow_html=True)
    with mid:
        rfe_ad_50
        text19 = '<p style="font-family:Time-New-Roman; font-size: 15px;text-align: center;">Top 50 features</p>'
        st.markdown(text19, unsafe_allow_html=True)
    with right_column:
        rfe_ad_100
        text19 = '<p style="font-family:Time-New-Roman; font-size: 15px;text-align: center;">Top 100 features</p>'
        st.markdown(text19, unsafe_allow_html=True)
with st.expander("New Cases"):
    left_column,mid, right_column= st.columns(3)
    with left_column:
        rfe_new_30
        text19 = '<p style="font-family:Time-New-Roman; font-size: 15px;text-align: center;">Top 30 features</p>'
        st.markdown(text19, unsafe_allow_html=True)
    with mid:
        rfe_new_50
        text19 = '<p style="font-family:Time-New-Roman; font-size: 15px;text-align: center;">Top 50 features</p>'
        st.markdown(text19, unsafe_allow_html=True)
    with right_column:
        rfe_new_100
        text19 = '<p style="font-family:Time-New-Roman; font-size: 15px;text-align: center;">Top 100 features</p>'
        st.markdown(text19, unsafe_allow_html=True)
with st.expander("ICU"):
    left_column,mid ,right_column= st.columns(3)
    with left_column:
        rfe_icu_30
        text19 = '<p style="font-family:Time-New-Roman; font-size: 15px;text-align: center;">Top 30 features</p>'
        st.markdown(text19, unsafe_allow_html=True)
    with mid:
        rfe_icu_50
        text19 = '<p style="font-family:Time-New-Roman; font-size: 15px;text-align: center;">Top 50 features</p>'
        st.markdown(text19, unsafe_allow_html=True)
    with right_column:
        rfe_icu_100
        text19 = '<p style="font-family:Time-New-Roman; font-size: 15px;text-align: center;">Top 100 features</p>'
        st.markdown(text19, unsafe_allow_html=True)
        
text19 = '<p style="font-family:Time-New-Roman; font-size: 15px;text-align: justify;">From the table above, we can see that the pcr, covid cases 3 days before in Sarawak and cluster workplace are the top 3 features that contribute to the scenario of daily covid cases of Malaysia. However, for the scenario of daily admitted covid cases to hospital across Malaysia and daily ICU cases across Malaysia, the RFE model seems to be overfitted and generate a lot of features with ranking of 1, thus we are not able to differentiate the top 3 features from the others. </p>'
st.markdown(text19, unsafe_allow_html=True)

text19 = '<p style="font-family:Time-New-Roman; font-size: 15px;text-align: justify;">As we compare the output generated by Boruta and RFE algorithms, we can conclude that RFE is more likely to be overfitted as it produces a lot of features which have the same ranking of 1. This results in a situation where we cannot clearly differentiate which features are more important than others. Thus, we decided to use the top 30, 50 and 100 features generated by Boruta as it can differentiate the features better. These features will be used to feed into our machine learning model to predict the scenarios.  </p>'
st.markdown(text19, unsafe_allow_html=True)
#=================================================================================================

title6 = '<p style="font-family:Time-New-Roman; font-size: 32px;font-weight: bold">Classfication & Regression model</p>' 
st.markdown(title6, unsafe_allow_html=True)
text31 = '<p style="font-family:Time-New-Roman;font-size: 28px;">Machine Learning  </p>'
st.markdown(text31, unsafe_allow_html=True)

text19 = '<p style="font-family:Time-New-Roman; font-size: 15px;text-align: justify;">In this section, we are going to compare the regression model and classification model to see which model performs better in predicting our 3 scenarios. </p>'
st.markdown(text19, unsafe_allow_html=True)
#=================================================================================================
text31 = '<p style="font-family:Time-New-Roman;font-size: 28px;">Regression model </p>'
st.markdown(text31, unsafe_allow_html=True)
text19 = '<p style="font-family:Time-New-Roman; font-size: 15px;text-align: justify;">We decided to use 5 regression model which are Linear Regression, Decision Tree Regression, Random Forest Regression, Bayesian Linear Regression and Support Vector Regression to predict the daily covid cases of Malaysia, daily admitted covid cases to hospital across Malaysia and daily ICU cases across Malaysia. The performance of each regression model is shown at the table x. R-squared(R2) and Mean Absolute Error(MAE) are selected as evaluation metrics. </p>'
st.markdown(text19, unsafe_allow_html=True)

text31 = '<p style="font-family:Time-New-Roman;font-size: 24px;font-weight: bold;text-align: center;">New Cases </p>'
st.markdown(text31, unsafe_allow_html=True)
im = Image.open("Regression/caseNew.png")
st.image(im, width=1500)
text19 = '<p style="font-family:Time-New-Roman; font-size: 15px;text-align: justify;">From the table above, we can see that the best performing model for predicting daily covid cases of Malaysia is the linear regression model with R2 of 0.999 and MAE of 132.5. Next, it is followed by the Bayesian linear regression model with R2 of 0.999 and MAE of 133.67. Both of the results are obtained using the dataset of top 50 features. The worst performing model is the Support Vector Regression model with R2 of 0.539 and MAE of 3453 using the dataset of top 30 features.  </p>'
st.markdown(text19, unsafe_allow_html=True)

text31 = '<p style="font-family:Time-New-Roman;font-size: 24px;font-weight: bold;text-align: center;">Admitted Cases  </p>'
st.markdown(text31, unsafe_allow_html=True)
im = Image.open("Regression/admitted.png")
st.image(im, width=1500)
text19 = '<p style="font-family:Time-New-Roman; font-size: 15px;text-align: justify;">Moreover, we can see that the best performing model for predicting daily admitted covid cases to hospital across Malaysia is Bayesian linear regression model with R2 of 0.984 and MAE of 48.531 using the dataset of top 100 features, followed by the same model with R2 of 0.981 and MAE of 51.046 using the dataset that do not undergo any feature selection.The worst performing model is the Decision Tree Regression model with R2 of 0.744 and MAE of 188.65 using the dataset of top 30 features.</p>'
st.markdown(text19, unsafe_allow_html=True)


text31 = '<p style="font-family:Time-New-Roman;font-size: 24px;font-weight: bold;text-align: center;">ICU </p>'
st.markdown(text31, unsafe_allow_html=True)
im = Image.open("Regression/ICU.png")
st.image(im, width=1500)
text19 = '<p style="font-family:Time-New-Roman; font-size: 15px;text-align: justify;"> Furthermore, the table shows us that the best performing model for predicting daily ICU cases across Malaysia is the Linear Regression and Bayesian Linear Regression model. Both of them have the same R2 and MAE which are 0.989 and 18.8 respectively using the dataset that does not undergo any feature selection.The worst performing model is the Decision Tree Regression model with R2 of 0.852 and MAE of 61.65 using the dataset of top 100 features.</p>'
st.markdown(text19, unsafe_allow_html=True)
text19 = '<p style="font-family:Time-New-Roman; font-size: 15px;text-align: justify;">In general, we can conclude that for the regression model, Linear Regression and Bayesian Linear Regression outperforms other models. Dataset with top 30 features seems to lower down the performance of the model in 3 scenarios.</p>'
st.markdown(text19, unsafe_allow_html=True)


text31 = '<p style="font-family:Time-New-Roman;font-size: 28px;">Classification model </p>'
st.markdown(text31, unsafe_allow_html=True)
text19 = '<p style="font-family:Time-New-Roman; font-size: 15px;text-align: justify;">Before we fit our data into the classification model, we need to discretize the dependent variable and group it into categorical data as its original data type is integer. The following steps show the steps to set the severity level of each scenario:</p>'
st.markdown(text19, unsafe_allow_html=True)

left_column,mid, right_column= st.columns(3)
with left_column:

    text19 = '<p style="font-family:Time-New-Roman; font-size: 15px;text-align: justify;">1. daily covid cases of Malaysia</p>'
    st.markdown(text19, unsafe_allow_html=True)
    text19 = '<p style="font-family:Time-New-Roman; font-size: 15px;text-align: justify;">--a. Let X = No. daily covid cases of Malaysia</p>'
    st.markdown(text19, unsafe_allow_html=True)
    text19 = '<p style="font-family:Time-New-Roman; font-size: 15px;text-align: justify;">----i) If X <= 1000,severity score class = 1</p>'
    st.markdown(text19, unsafe_allow_html=True)
    text19 = '<p style="font-family:Time-New-Roman; font-size: 15px;text-align: justify;">----ii) If 1000 < X <= 3000, severity score class = 2</p>'
    st.markdown(text19, unsafe_allow_html=True)
    text19 = '<p style="font-family:Time-New-Roman; font-size: 15px;text-align: justify;">----iii) If 3000 < X <= 6000, severity score class = 3</p>'
    st.markdown(text19, unsafe_allow_html=True)
    text19 = '<p style="font-family:Time-New-Roman; font-size: 15px;text-align: justify;">----iv) If 6000 < X <= 9000, severity score class = 4</p>'
    st.markdown(text19, unsafe_allow_html=True)
    text19 = '<p style="font-family:Time-New-Roman; font-size: 15px;text-align: justify;">----v) If X > 9000 severity score class = 5</p>'
    st.markdown(text19, unsafe_allow_html=True)
with mid:
    text19 = '<p style="font-family:Time-New-Roman; font-size: 15px;text-align: justify;">2. daily admitted covid cases to hospital across Malaysia</p>'
    st.markdown(text19, unsafe_allow_html=True)
    text19 = '<p style="font-family:Time-New-Roman; font-size: 15px;text-align: justify;">--a. Let X = No. daily admitted covid cases</p>'
    st.markdown(text19, unsafe_allow_html=True)
    text19 = '<p style="font-family:Time-New-Roman; font-size: 15px;text-align: justify;">----i) If X <= 600,severity score class = 1</p>'
    st.markdown(text19, unsafe_allow_html=True)
    text19 = '<p style="font-family:Time-New-Roman; font-size: 15px;text-align: justify;">----ii) If 600 < X <= 1200, severity score class = 2</p>'
    st.markdown(text19, unsafe_allow_html=True)
    text19 = '<p style="font-family:Time-New-Roman; font-size: 15px;text-align: justify;">----iii) If 1200 < X<= 1800, severity score class = 3</p>'
    st.markdown(text19, unsafe_allow_html=True)
    text19 = '<p style="font-family:Time-New-Roman; font-size: 15px;text-align: justify;">----iv) If 1800 < X<= 2400, severity score class 4</p>'
    st.markdown(text19, unsafe_allow_html=True)
    text19 = '<p style="font-family:Time-New-Roman; font-size: 15px;text-align: justify;">----v) If X > 2400 severity score class = 5</p>'
    st.markdown(text19, unsafe_allow_html=True)
with right_column:
    text19 = '<p style="font-family:Time-New-Roman; font-size: 15px;text-align: justify;">3. daily ICU cases across Malaysia</p>'
    st.markdown(text19, unsafe_allow_html=True)
    text19 = '<p style="font-family:Time-New-Roman; font-size: 15px;text-align: justify;">--a. Let X = No. ICU cases</p>'
    st.markdown(text19, unsafe_allow_html=True)
    text19 = '<p style="font-family:Time-New-Roman; font-size: 15px;text-align: justify;">----i) If x <= 500,severity score class = 1</p>'
    st.markdown(text19, unsafe_allow_html=True)
    text19 = '<p style="font-family:Time-New-Roman; font-size: 15px;text-align: justify;">----ii) If 500 < x <= 750, severity score class = 2</p>'
    st.markdown(text19, unsafe_allow_html=True)
    text19 = '<p style="font-family:Time-New-Roman; font-size: 15px;text-align: justify;">----iii) If 750 < x <= 1000, severity score class = 3</p>'
    st.markdown(text19, unsafe_allow_html=True)
    text19 = '<p style="font-family:Time-New-Roman; font-size: 15px;text-align: justify;">----iv) If 1000 < x <= 1250, severity score class 4</p>'
    st.markdown(text19, unsafe_allow_html=True)
    text19 = '<p style="font-family:Time-New-Roman; font-size: 15px;text-align: justify;">----v) If x > 1250 severity score class = 5</p>'
    st.markdown(text19, unsafe_allow_html=True)
text19 = '<p style="font-family:Time-New-Roman; font-size: 15px;text-align: justify;">We decided to use 5 classification models which are Decision Tree Classifier, Random Forest Classifier, Support Vector Machine, Naive Bayes and KNN to predict the daily covid cases of Malaysia, daily admitted covid cases to hospital across Malaysia and daily ICU cases across Malaysia. SMOTE technique is used to balance the dataset. The performance of each regression model is shown at the table x. Accuracy and F1 score are selected as evaluation metrics. </p>'
st.markdown(text19, unsafe_allow_html=True)
text31 = '<p style="font-family:Time-New-Roman;font-size: 24px;font-weight: bold;text-align: center;">Admitted Cases  </p>'
st.markdown(text31, unsafe_allow_html=True)
im = Image.open("CM Classification/admitted.png")
st.image(im, width=1500)

text31 = '<p style="font-family:Time-New-Roman;font-size: 24px;font-weight: bold;text-align: center;">New Cases </p>'
st.markdown(text31, unsafe_allow_html=True)
im = Image.open("CM Classification/caseNew.png")
st.image(im, width=1500)
text19 = '<p style="font-family:Time-New-Roman; font-size: 15px;text-align: justify;">From the table above, we can observe that for the case to predict daily covid cases severity , decision tree classifier model outperforms other models with the accuracy and F1-score of 0.89 and 0.88 respectively testing on the dataset of top 50 features, top 100 features, not undergoing feature selection and SMOTE is applied to the dataset. Next, it is followed by a Support vector machine model with the accuracy and F1-score of 0.89 and 0.88 using the dataset of 100 top features but SMOTE is not applied.   </p>'
st.markdown(text19, unsafe_allow_html=True)

text31 = '<p style="font-family:Time-New-Roman;font-size: 24px;font-weight: bold;text-align: center;">ICU </p>'
st.markdown(text31, unsafe_allow_html=True)
text19 = '<p style="font-family:Time-New-Roman; font-size: 15px;text-align: justify;">On the other hand, the best performing model for predicting daily admitted covid cases to hospital severity are decision tree classifier and support vector machine model with the accuracy and F1-score of 0.91 and 0.91 respectively, testing on the dataset of top 30 and top 50 features which SMOTE is applied to the dataset.</p>'
st.markdown(text19, unsafe_allow_html=True)

im = Image.open("CM Classification/ICU.png")
st.image(im, width=1500)
text19 = '<p style="font-family:Time-New-Roman; font-size: 15px;text-align: justify;">Last but not least, the best performing model for predicting the daily ICU cases severity is decision tree classifier with the accuracy and F1-score of 0.95 respectively testing on the dataset which is not undergoing feature selection but SMOTE is applied.It followed by Random Forest Classifier, Support Vector Machine and KNN model which achieve the accuracy and F1-score of 0.93 respectively testing on dataset of top 100 feature with and without SMOTE.</p>'
st.markdown(text19, unsafe_allow_html=True)
text19 = '<p style="font-family:Time-New-Roman; font-size: 15px;text-align: justify;">Below shows the confusion matrix of some good performing models for each scenario:</p>'
st.markdown(text19, unsafe_allow_html=True)

with st.expander("Confusion matrics of Admitted cases"):
    left_column,left_mid,mid,right_mid= st.columns(4)
    with left_column:
        im = Image.open("CM Classification/admitted_T30_SMOTE_DTC.png")
        st.image(im, width=250)
        text31 = '<p style="font-family:Time-New-Roman;font-size: 15px;">TOP 30 Features Selection-SMOTE (Decision Tree Classifier)  </p>'
        st.markdown(text31, unsafe_allow_html=True)
    with left_mid:
        im = Image.open("CM Classification/admitted_T50_SMOTE_DTC.png")
        st.image(im, width=250)
        text31 = '<p style="font-family:Time-New-Roman;font-size: 15px;">TOP 50 Features Selection-SMOTE (Decision Tree Classifier) </p>'
        st.markdown(text31, unsafe_allow_html=True)
    with mid:
        im = Image.open("CM Classification/admitted_T50_SMOTE_SVC.png")
        st.image(im, width=250)
        text31 = '<p style="font-family:Time-New-Roman;font-size: 15px;t">TOP 50 Features Selection-SMOTE (Support Vector Classifier) </p>'
        st.markdown(text31, unsafe_allow_html=True)
    with right_mid:
        im = Image.open("CM Classification/admitted_T100_SMOTE_SVC.png")
        st.image(im, width=250)
        text31 = '<p style="font-family:Time-New-Roman;font-size: 15px;">TOP 100 Features Selection-SMOTE (Support Vector Classifier) </p>'
        st.markdown(text31, unsafe_allow_html=True)
        
with st.expander("Confusion matrics of New cases"):
    left_column,left_mid,mid,right_mid= st.columns(4)
    with left_column:
        im = Image.open("CM Classification/casesNew_NFS_SMOTE_DTC.png")
        st.image(im, width=250)
        text31 = '<p style="font-family:Time-New-Roman;font-size: 15px;">No Features Selection-SMOTE (Decision Tree Classifier) </p>'
        st.markdown(text31, unsafe_allow_html=True)
    with left_mid:
        im = Image.open("CM Classification/casesNew_T50_SMOTE_DTC.png")
        st.image(im, width=250)
        text31 = '<p style="font-family:Time-New-Roman;font-size: 15px;">Top 50 Features Selection-SMOTE (Decision Tree Classifier) </p>'
        st.markdown(text31, unsafe_allow_html=True)
    with mid:
        im = Image.open("CM Classification/casesNew_T100_NSMO_SVC.png")
        st.image(im, width=250)
        text31 = '<p style="font-family:Time-New-Roman;font-size: 15px;t">Top 100 Features Selection-No SMOTE (Support Vectpr Classifier)</p>'
        st.markdown(text31, unsafe_allow_html=True)
    with right_mid:
        im = Image.open("CM Classification/casesNew_T100_SMOTE_DTC.png")
        st.image(im, width=250)
        text31 = '<p style="font-family:Time-New-Roman;font-size: 15px;">Top 100 Features Selection-SMOTE (Decision Tree Classifier) </p>'
        st.markdown(text31, unsafe_allow_html=True)
        
with st.expander("Confusion matrics of ICU"):
    left_column,left_mid,mid,right_mid= st.columns(4)
    with left_column:
        im = Image.open("CM Classification/ICU_NFS_SMOTE_DTC.png")
        st.image(im, width=250)
        text31 = '<p style="font-family:Time-New-Roman;font-size: 15px;">No Features Selection-SMOTE (Decision Tree Classifier)   </p>'
        st.markdown(text31, unsafe_allow_html=True)
    with left_mid:
        im = Image.open("CM Classification/ICU_T100_NSMO_KNN.png")
        st.image(im, width=250)
        text31 = '<p style="font-family:Time-New-Roman;font-size: 15px;">Top 100 Features Selection-No SMOTE (K nearest neighbor) </p>'
        st.markdown(text31, unsafe_allow_html=True)
    with mid:
        im = Image.open("CM Classification/ICU_T100_NSMO_RFC.png")
        st.image(im, width=250)
        text31 = '<p style="font-family:Time-New-Roman;font-size: 15px;t">Top 100 Features Selection-No SMOTE (Random Forest Classifier) </p>'
        st.markdown(text31, unsafe_allow_html=True)
    with right_mid:
        im = Image.open("CM Classification/ICU_T100_SMOTE_SVC.png")
        st.image(im, width=250)
        text31 = '<p style="font-family:Time-New-Roman;font-size: 15px;">Top 100 Features Selection-SMOTE (Support Vectpr Classifier)  </p>'
        st.markdown(text31, unsafe_allow_html=True)
        

text19 = '<p style="font-family:Time-New-Roman; font-size: 15px;text-align: justify;">In conclusion, we cannot compare the performance of classification and regression models directly because the output of two models are different. Classification model produces a categorical output, while the regression model produces a numerical output. For the regression part, Linear Regression and Bayesian Linear Regression performed the best among other regression models while Decision Tree Classifier and Support Vector Machine performed the best among other classification models in 3 scenarios. For both regression and classification models, they seem to perform badly on the dataset with top 30 features. This means selecting the top 30 features might not be a good idea. However, selecting top 50 and 100 can still proceed. Based on our works, we highly encourage you to apply SMOTE on your dataset for classification problems as it has been proved to increase the performance of the model. </p>'
st.markdown(text19, unsafe_allow_html=True)
#=================================================================================================
arima1_forecast= pd.read_csv('Herd Immunity/arima1_forecast.csv')
arima1_predict=pd.read_csv('Herd Immunity/arima1_predictions.csv')
arima1_test= pd.read_csv('Herd Immunity/arima1_test.csv')
arima2_forecast= pd.read_csv('Herd Immunity/arima2_forecast.csv')
arima2_full= pd.read_csv('Herd Immunity/arima2_full.csv')
arima2_test= pd.read_csv('Herd Immunity/arima2_test.csv')
lstm_forecast= pd.read_csv('Herd Immunity/lstm_forecast.csv')
lstm_test= pd.read_csv('Herd Immunity/lstm_test.csv')

arima1_forecast.rename(columns = {'Unnamed: 0':'index','0':'value'}, inplace = True)
arima1_predict.rename(columns = {'Unnamed: 0':'index','0':'predict'}, inplace = True)
arima1_test.rename(columns = {'Unnamed: 0':'index','0':'test'}, inplace = True)
lstm_forecast.rename(columns = {'Unnamed: 0':'index','0':'value'}, inplace = True)
lstm_test.rename(columns = {'Unnamed: 0':'index'}, inplace = True)


arima1= arima1_predict.merge(arima1_test,left_on=['index'],right_on=['index'],how='left')
arima1 = arima1.melt('index', var_name='type',  value_name='vals')
arima2 = arima2_test.melt('date', var_name='type',  value_name='vals')
lstm = lstm_test.melt('index', var_name='type',  value_name='vals')
#=================================================================================================
title6 = '<p style="font-family:Time-New-Roman; font-size: 32px;font-weight: bold">Herd Immunity</p>' 
st.markdown(title6, unsafe_allow_html=True)

text19 = '<p style="font-family:Time-New-Roman; font-size: 15px;text-align: justify;">In this section, we are going to predict the vaccine given daily for the coming month and conclude whether Malaysia can reach herd immunity(80% of fully vaccinated) by 30/11/2021. We have tried 4 different approaches to perform the prediction.</p>'
st.markdown(text19, unsafe_allow_html=True)
title6 = '<p style="font-family:Time-New-Roman; font-size: 24px;;font-weight: bold">Basics Mathematics </p>' 
st.markdown(title6, unsafe_allow_html=True)
text19 = '<p style="font-family:Time-New-Roman; font-size: 15px;text-align: justify;">In this method, we are grouping the vaccination data into a weekly manner. After that, we calculate the change of vaccine per week to obtain the weekly rate.From the current weekly rate, we predict the total vaccine given for next week until 30/11/2021. Since we are predicting in a weekly manner, the data we use is until 26/10/2021, which is 5 weeks before 30/11/2021.</p>'
st.markdown(text19, unsafe_allow_html=True)
text19 = '<p style="font-family:Time-New-Roman; font-size: 15px;text-align: justify;">For the weekly change rate, we take the average of 4 weeks.For example, to predict next week, we take the average of this week, last week, last 2 week and last 3 week; to predict next next week, we take last week, last 2 week, last 3 week and last 4 week. For the algorithm, we use back the basics mathematics, which are:</p>'
st.markdown(text19, unsafe_allow_html=True)
text19 = '<p style="font-family:Time-New-Roman; font-size: 15px;text-align: justify;"> i) next_week = this_week * average_rate </p>'
st.markdown(text19, unsafe_allow_html=True)
text19 = '<p style="font-family:Time-New-Roman; font-size: 15px;text-align: justify;"> ii) next_2week = next_week * average_rate and so on..</p>'
st.markdown(text19, unsafe_allow_html=True)

im = Image.open("Heldimmunity.jpg")
st.image(im)

text19 = '<p style="font-family:Time-New-Roman; font-size: 15px;text-align: justify;"> From the result, we can see that the total predicted number of vaccines for the next 5 weeks is 4013075. With this amount of vaccine, we are able to reach 85.9% of herd immunity by the end of November 2021. </p>'
st.markdown(text19, unsafe_allow_html=True)
title6 = '<p style="font-family:Time-New-Roman; font-size: 24px;;font-weight: bold">ARIMA </p>' 
st.markdown(title6, unsafe_allow_html=True)
g=alt.Chart(arima2).mark_line().encode(
      x='date',
      y='vals',
      color = alt.Color('type', scale=alt.Scale(scheme = 'set1'))
  ).properties(
      width=700,
      height=300
  )
st.altair_chart(g, use_container_width=True)
left_column,left_mid= st.columns([4,3])
with left_column:
    g=alt.Chart(arima2_forecast).mark_line().encode(
           x='date',
           y="Forecast",
       ).properties(
           width=700,
           height=300
       )

    st.altair_chart(g, use_container_width=False)
with left_mid:
    text19 = '<p style="font-family:Time-New-Roman; font-size: 15px;text-align: justify;"> ARIMA stands for AutoRegression Integrated Moving Average. In order to use the ARIMA model, we need to specify the order in terms of (p,d,q). We have decided to use the auto-arima package to help us loop through a range of values and decide the best value for (p,d,q). By running through the auto-arima function with the vaccination data, the model suggested a SARIMAX model with order of (2,0,1) and seasonal order of (0,1,1,12). By using the suggested model and parameters, our SARIMAX model obtains a RMSE of 37344 as shown in the picture. By using the trained model for forecasting, the model predicts that the total predicted number of vaccines for the next 5 weeks is 4980740. With this amount of vaccine, we are able to reach 88.8% of herd immunity by the end of November 2021.  </p>'
    st.markdown(text19, unsafe_allow_html=True)
    text19 = '<p style="font-family:Time-New-Roman; font-size: 15px;text-align: justify;"> However, If we look at the predicted value produced by the model, we can notice that the predicted value has a periodic pattern. This condition is different from the previous approach (basic mathematics) where the number of vaccines is decreasing over the timeline. </p>'
    st.markdown(text19, unsafe_allow_html=True)

title6 = '<p style="font-family:Time-New-Roman; font-size: 24px;;font-weight: bold">LSTM </p>' 
st.markdown(title6, unsafe_allow_html=True)

g=alt.Chart(lstm).mark_line().encode(
      x='index',
      y='vals',
      color = alt.Color('type', scale=alt.Scale(scheme ='set1'))
  ).properties(
      width=700,
      height=300
  )
st.altair_chart(g, use_container_width=True)
left_column,left_mid= st.columns([4,3])
with left_column:
    g=alt.Chart(lstm_forecast).mark_line().encode(
           x='index',
           y="value",
       ).properties(
           width=700,
           height=400
       )
    st.altair_chart(g, use_container_width=False)
with left_mid:
    text19 = '<p style="font-family:Time-New-Roman; font-size: 15px;text-align: justify;"> LSTM stands for Long Short Term Memory, which is a type of Recurrent Neural Network (RNN) used in sequence prediction problems and we decide to use it to predict our vaccine for the coming month. The process can be divided into 2 parts: In the first part, we split the vaccine dataset into a train and test set to build the model. In the second part, with the trained model, we pass in the whole dataset as input to forecast the number of vaccines for the coming month. We set the lookup variable to 7, meaning we will use the last 7 days’s data to predict the next day value. The reason we choose 7 for lookup is due to after trial and error we found out that with 7 lookups, the model performs the best.</p>'
    st.markdown(text19, unsafe_allow_html=True)
    text19 = '<p style="font-family:Time-New-Roman; font-size: 15px;text-align: justify;"> Image x shows the predicted value and real value on the test set. We can see that the predicted value is still following the trend of the real value. Besides, the model obtained the RMSE of 37396. Next, we fed the whole dataset into this model and used it to forecast the vaccine number given for the coming month. From the result, we can see that the total predicted number of vaccines for the next 5 weeks is 4493483. With this amount of vaccine, we are able to reach 87.38% of herd immunity by the end of November 2021. If we look at the predicted value produced by the model, we can notice that the predicted value is decreasing slowly. This condition is similar to the previous approach (basic mathematics) where the number of vaccines is decreasing over the timeline.</p>'
    st.markdown(text19, unsafe_allow_html=True)
text19 = '<p style="font-family:Time-New-Roman; font-size: 15px;text-align: justify;">In conclusion, based on the three of the approaches we have tried, all three approaches have predicted that we can reach 80% of herd immunity by 30 November 2021. </p>'
st.markdown(text19, unsafe_allow_html=True)
#====================================================================================================================
title6 = '<p style="font-family:Time-New-Roman; font-size: 32px;font-weight: bold">Clustering</p>' 
st.markdown(title6, unsafe_allow_html=True)
st.markdown(text19, unsafe_allow_html=True)
text19 = '<p style="font-family:Time-New-Roman; font-size: 15px;text-align: justify;">Clustering is a task of dividing the data points into a number of groups so that the data points in the same group are more similar to each other than those in the other group. This technique is particularly useful if our data points are messy and we want to group them into a few clusters. In this section, we are going to cluster 2 scenarios, they are: daily covid cases and admitted to hospital cases in each state and daily covid cases and daily death cases in each state. Three clustering techniques(KMeans, DBSCAN and agglomerative clustering) are selected to be used in this section.  </p>'
st.markdown(text19, unsafe_allow_html=True)

        
title6 = '<p style="font-family:Time-New-Roman; font-size: 24px;">1. Daily covid cases and admitted to hospital cases in each state</p>' 
st.markdown(title6, unsafe_allow_html=True)
left_column,left_mid= st.columns([3,4])
with left_column:
    im = Image.open("Clustering/new_admitted_ori.png")
    st.image(im, width=500)
with left_mid:
    text31 = '<p style="font-family:Time-New-Roman;font-size: 15px;;text-align: justify;">Image on the left shows the original scatter plot of the daily covid cases and admitted to hospital cases in each state. From the original plot, we can see that the data points are overlapping and quite messy. It is hard to differentiate each other clearly. Thus, we decided to cluster the data points with 3 algorithms: KMeans,DBSCAN and Agglomerative clustering.</p>'
    st.markdown(text31, unsafe_allow_html=True)
    text31 = '<p style="font-family:Time-New-Roman;font-size: 15px;;text-align: justify;">Images in the expander below show the result after clustering. From the images, we can see that the data points have been grouped into 3 groups with clear borders, except for DBSCAN technique which still produced a hardly differentiable output. After applying clustering, a new column named [‘y’] will be generated and we can use that variable to define the risk. For example, at the output of KMeans clustering, the data points are grouped into cluster 0, 1 and 2 while cluster 0 starts from the left bottom corner, followed by cluster 2 and cluster 1. For this situation, cluster 1 has higher risk than cluster 0 and 2 as it appears at the right corner of the graph, where the x and y variables (cases_new and admitted_total) are high. Thus, any data points that are categorized into cluster 1 have a higher risk compared to cluster 2 and 0. In addition, we also can use the [‘y’] variable generated to be the target variable and apply it to a classification problem to predict whether the new data fall in which level of risk.</p>'
    st.markdown(text31, unsafe_allow_html=True)
with st.expander("Scatter plot of  Daily covid cases and admitted to hospital cases in each state"):
    left_column,left_mid,mid= st.columns(3)
    with left_column:
        im = Image.open("Clustering/new_admitted_kmeans.png")
        st.image(im, width=450)
        text31 = '<p style="font-family:Time-New-Roman;font-size: 15px;text-align: center;">Kmeans</p>'
        st.markdown(text31, unsafe_allow_html=True)
    with left_mid:
        im = Image.open("Clustering/new_admitted_dbscan.png")
        st.image(im, width=450)
        text31 = '<p style="font-family:Time-New-Roman;font-size: 15px;text-align: center;">DBSCAN</p>'
        st.markdown(text31, unsafe_allow_html=True)
    with mid:
        im = Image.open("Clustering/new_admitted_agglo.png")
        st.image(im, width=450)
        text31 = '<p style="font-family:Time-New-Roman;font-size: 15px;text-align: center;">Agglomerative Clustering</p>'
        st.markdown(text31, unsafe_allow_html=True)
        
title6 = '<p style="font-family:Time-New-Roman; font-size: 24px;">2. daily covid cases and daily death cases in each state</p>' 
st.markdown(title6, unsafe_allow_html=True)
left_column,left_mid= st.columns([3,4])
with left_column:
    im = Image.open("Clustering/new_death_ori.png")
    st.image(im, width=500)
with left_mid:
    text31 = '<p style="font-family:Time-New-Roman;font-size: 15px;;text-align: justify;">Image on the left shows the original scatter plot of the daily covid cases and daily death cases in each state. Same as the previous scenario, we cluster the data points with 3 algorithms: KMeans, DBSCAN and Agglomerative clustering. </p>'
    st.markdown(text31, unsafe_allow_html=True)
    text31 = '<p style="font-family:Time-New-Roman;font-size: 15px;;text-align: justify;">Images in the expander below show the result after clustering. From the images, we can see that the data points have been grouped into 3 groups with clear borders, except for DBSCAN technique which still produced a hardly differentiable output. After applying clustering, a new column named [‘y’] will be generated and we can use that variable to define the risk. For example, at the output of Agglomerative clustering, the data points are grouped into cluster 0, 1 and 2 while cluster 0 starts from the left bottom corner, followed by cluster 2 and cluster 1. For this situation, cluster 1 has higher risk than cluster 0 and 2 as it appears at the top left corner of the graph, where the y variables (cases_new) are high. Thus, any data points that are categorized into cluster 1 have a higher risk compared to cluster 2 and 0. In addition, we also can use the [‘y’] variable generated to be the target variable and apply it to a classification problem to predict whether the new data fall in which level of risk. </p>'
    st.markdown(text31, unsafe_allow_html=True)
with st.expander("Scatter plot of daily covid cases and daily death cases in each state"):
    left_column,left_mid,mid= st.columns(3)
    with left_column:
        im = Image.open("Clustering/new_death_kmeans.png")
        st.image(im, width=450)
        text31 = '<p style="font-family:Time-New-Roman;font-size: 15px;text-align: center;">Kmeans</p>'
        st.markdown(text31, unsafe_allow_html=True)
    with left_mid:
        im = Image.open("Clustering/new_death_dbscan.png")
        st.image(im, width=450)
        text31 = '<p style="font-family:Time-New-Roman;font-size: 15px;text-align: center;">DBSCAN</p>'
        st.markdown(text31, unsafe_allow_html=True)
    with mid:
        im = Image.open("Clustering/new_death_agglo.png")
        st.image(im, width=450)
        text31 = '<p style="font-family:Time-New-Roman;font-size: 15px;text-align: center;">Agglomerative Clustering</p>'
        st.markdown(text31, unsafe_allow_html=True)
#=================================================================================================

title6 = '<p style="font-family:Time-New-Roman; font-size: 18px;font-weight: bold">End of content.</p>' 
st.markdown(title6, unsafe_allow_html=True)
title6 = '<p style="font-family:Time-New-Roman; font-size: 15px;font-weight: bold">Prepared by Chang Kai Boon(1181101282) and Soe Zhao Hong(1181101614)</p>' 
st.markdown(title6, unsafe_allow_html=True)