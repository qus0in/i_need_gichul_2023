import streamlit as st
from data import get_questions, get_terms

def main():
    qs = get_questions()
    ts = get_terms()
    if 'page' not in st.session_state:
        st.session_state['page'] = 0
    page = st.session_state['page']
    data = qs.iloc[page]
    part = ts[(ts.part == data.part) & (ts.chapter == 0)].name
    chapter = ts[(ts.part == data.part) & (ts.chapter == data.chapter)].name
    st.markdown(f"`{part}`")
    st.markdown(f"`{chapter}`")
    st.markdown(f"> {data.title}")

    col = st.columns(5)
    with col[2]:
        col1, col2, col3 = st.columns(3)
        col1.button('◀️', on_click=prev_page)
        col2.markdown(f"{page+1} / {len(qs)}")
        col3.button('▶️', on_click=next_page)
    
def prev_page():
    if st.session_state['page'] > 0:
        st.session_state['page'] -= 1

def next_page():
    if st.session_state['page'] < len(get_questions()):
        st.session_state['page'] += 1
