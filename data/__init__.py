import streamlit as st
import pandas as pd
import glob

@st.cache_data
def get_questions():
    return pd.concat([pd.read_csv(fn, sep=';') for fn in glob.glob('./data/question*.csv')])

@st.cache_data
def get_terms():
    return pd.read_csv('terms.csv')