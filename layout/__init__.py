import streamlit as st
import streamlit.components.v1 as components
import numpy as np
from data import get_questions, get_terms

def main():
    if 'page' not in st.session_state:
        st.session_state['page'] = 0
    with st.container(): question()

def question():
    qs, ts = get_questions(), get_terms()
    page = st.session_state['page']
    data = qs.iloc[page]
    get_name = lambda x: ts.query(f'part == {data.part}').query(f'chapter == {x}').iloc[0,2]
    part = get_name(0)
    chapter = get_name(data.chapter)
    st.markdown(f"*{part} / {chapter}*")
    st.markdown(f"> {data.title}")
    if len(data.description):
        st.markdown(data.description)
    st.text_input('정답 입력', key='answer')
    answer = st.session_state['answer']
    btn = {
        'label': '제출하기',
        'disabled': len(answer)==0,
        'type': 'primary',
        'use_container_width': True,
    }
    
    if st.button(**btn):
        if answer.lower() in data.answer.split('|'):
            st.success('정답입니다')
        else:
            st.warning('오답입니다')
            st.markdown(f'**답** : {data.answer}')

        st.button('다음으로',
            use_container_width=True,
            on_click=lambda : st.session_state.update({'page': page+1}))