import streamlit as st
from data import get_questions

def main():
    qs = get_questions()
    col = st.columns(5)
    with col[2]:
        col1, col2 = st.columns(2)
        col1.button('◀️')
        col2.button('▶️')
    st.write(qs)