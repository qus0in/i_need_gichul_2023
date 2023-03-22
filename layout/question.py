import streamlit as st

from data import get_questions, get_terms
from layout.submit import submit

def question():
    qs, ts = get_questions(), get_terms()
    page = st.session_state['page']
    if page == len(qs):
        last_page()
        return
    if st.session_state.get('question', True):
        data = qs.iloc[page]
        get_name = lambda x: ts.query(
            f'part == {data.part}').query(f'chapter == {x}').iloc[0,2]
        part = get_name(0)
        chapter = get_name(data.chapter)
        st.markdown(f"*{part} / {chapter}*")
        st.markdown(f"> {data.title}")
        if type(data.description) != float:
            st.markdown(data.description)
        st.text_input('정답 입력', key='answer')
        btn1 = {
            'label': '✅ 제출하기',
            'type': 'primary',
            'use_container_width': True,
            'on_click': lambda : submit(data)
        }
        btn2 = {
            'label': '😖 넘기기',
            'type': 'secondary',
            'use_container_width': True,
            'on_click': lambda : submit(data)
        }
        col1, col2 = st.columns(2)
        col1.button(**btn1)
        col2.button(**btn2)
        return

def last_page():
    c_cnt = st.session_state['correct_cnt']
    w_cnt = st.session_state['wrong_cnt']
    st.write(f"> 맞힌 문제 : {c_cnt} / 전체 문제 : {c_cnt + w_cnt}")
    st.write(f"> 정답률 : {c_cnt / w_cnt * 100 : .2f}%")

def next_question():
    st.session_state['page'] += 1
    st.session_state['answer'] = ''
    st.session_state['question'] = True