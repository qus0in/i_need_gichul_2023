import streamlit as st
from layout.question import question

def main():
    keys = ['page', 'wrong_cnt', 'correct_cnt']
    for k in keys:
        if k not in st.session_state:
            st.session_state[k] = 0
    with st.container(): question()

def result():
    pass
