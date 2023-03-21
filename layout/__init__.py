import streamlit as st
import numpy as np
from data import get_questions, get_terms

def main():
    qs = get_questions()
    ts = get_terms()
    if 'page' not in st.session_state:
        st.session_state['page'] = 0
    page = st.session_state['page']
    data = qs.iloc[page]
    part = ts[(ts.part == data.part) & (ts.chapter == 0)].iloc[0,2]
    chapter = ts[(ts.part == data.part) & (ts.chapter == data.chapter)].iloc[0,2]
    st.markdown(f"{part} / {chapter}")
    st.markdown(f"> {data.title}")
    if not np.isnan(data.description):
        st.markdown(data.description)
    st.text_input('정답 입력', key='answer')
    answer = st.session_state['answer']
    st.button('제출하기',
        disabled=answer,
        use_container_width=True)
def prev_page():
    if st.session_state['page'] > 0:
        st.session_state['page'] -= 1

def next_page():
    if st.session_state['page'] < len(get_questions()) - 1:
        st.session_state['page'] += 1
