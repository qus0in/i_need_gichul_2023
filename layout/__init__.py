import streamlit as st
from data import get_questions

def main():
    qs = get_questions()
    col = st.columns(5)
    page = st.session_state['page']
    
    if 'page' not in st.session_state:
        st.session_state['page'] = 1
    
    with col[2]:
        col1, col2, col3 = st.columns(3)
        col1.button('◀️', on_click=prev_page)
        col2.markdown(f"{page} / len(qs)")
        col3.button('▶️', on_click=next_page)
    
def prev_page():
    if st.session_state['page'] > 1:
        st.session_state['page'] -= 1

def next_page():
    if st.session_state['page'] < len(get_questions()):
        st.session_state['page'] += 1
