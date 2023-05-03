"""Name: Haoyang Yuan
CS230: Section 6
Data: United States Cities Database
Description:
This program shows the top 5 states with most population in bar chart, top 5 populous cities by state in bar chart and the
map shows the cities.
"""
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import pydeck as pdk
from pydeck.types import String


def getdata(filepath = r"C:\Users\surface\Desktop\cs230\cs230\uscities.csv"):
   cityDf = pd.read_csv(filepath).drop(columns=['id','city_ascii','county_fips','county_name','source','density','military','incorporated','timezone','ranking'
                                            ,'zips','id'])
   stateIdDict = set(cityDf['state_id'])
   statePopDf = cityDf.groupby('state_name',as_index=False).sum(numeric_only = True).drop(columns=['lat','lon'])
   return stateIdDict, statePopDf, cityDf

def gettopfive(df,byState = False):
   if byState:
      topFiveDf = df[df.state_id == byState].sort_values('population',ascending=False).iloc[0:5]
   else:
      topFiveDf = df.sort_values('population',ascending=False).iloc[0:5]
   return topFiveDf

def topfivestate(df):
   fig = plt.figure()
   plt.bar(df.state_name,df.population)
   plt.title('Top 5 states with most population')
   plt.xlabel('state name')
   plt.ylabel('population')
   st.pyplot(fig)

def topfivecity(df):
   fig = plt.figure()
   plt.bar(df.city,df.population)
   plt.title('Top 5 most populous city by state')
   plt.xlabel('city')
   plt.ylabel('population')
   st.pyplot(fig)

def map(df):
   st.map(df)

# def tester():



def main():
   stateIdDict, statePopDf, cityDf = getdata()
   option = st.sidebar.selectbox('Choose a graph or map',('Top 5 states with most population','Top 5 most populous city by state',
                                                  'Map of Most populous city by state'))
   if option == 'Top 5 states with most population':
      topfivestate(gettopfive(statePopDf))
   elif option == 'Top 5 most populous city by state':
      stateSelected = st.sidebar.selectbox('Select a State:',stateIdDict,index=19)
      topfivecity(gettopfive(cityDf,stateSelected))
   elif option == 'Map of Most populous city by state':
      stateSelected = st.sidebar.selectbox('Select a State:', stateIdDict, index=19)
      if st.button(label='Generate Map'):
         map(gettopfive(cityDf,stateSelected))



main()
# tester()