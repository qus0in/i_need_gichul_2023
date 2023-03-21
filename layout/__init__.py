import streamlit as st
from data import get_questions

def main():
    qs = get_questions()
    st.button('◀️')
    st.button('▶️')
    st.write(qs)