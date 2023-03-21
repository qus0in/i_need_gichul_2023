import streamlit as st
from data import get_questions

def main():
    qs = get_questions()
    col = st.columns(5)
    st.session_state['page'] = 1

    with col[2]:
        col1, col2, col3 = st.columns(3)
        col1.button('◀️', on_click=prev_page)
        col2.write(st.session_state['page'])
        col3.button('▶️', on_click=next_page)
    st.write(qs)

def prev_page():
    st.session_state['page'] -= 1
def next_page():
    st.session_state['page'] += 1
