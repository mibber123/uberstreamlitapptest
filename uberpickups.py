import streamlit as st
import pandas as pd
import numpy as np

st.title('streamlit uber test')

date = 'date/time'

dataurl = ('https://s3-us-west-2.amazonaws.com/streamlit-demo-data/uber-raw-data-sep14.csv.gz')

def loaddata(nrows):
    data = pd.read_csv(dataurl, nrows)
    lowercase = lambda x: str(x).tolower()
    data.rename(lowercase, axis = 'columns', inplace = True)
    data[date] = pd.to_datetime(data[date])
    return data
    
dataloadstate = st.text('loading data...')

rows = 10000
data = loaddata(rows)

dataloadstate = st.text("Loading Data...done!")