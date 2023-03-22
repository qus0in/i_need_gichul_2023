import streamlit as st

def main():
    if 'page' not in st.session_state:
        st.session_state['page'] = 0
    with st.container(): question()

def result():
    pass
