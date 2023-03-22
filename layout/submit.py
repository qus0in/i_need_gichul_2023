import streamlit as st
from data import get_questions

def submit(give_up=False):
    st.session_state['question'] = False
    qs = get_questions()
    answer = st.session_state['answer']
    page = st.session_state['page']
    data = qs.iloc[page]
    correct = None
    if data.kind == '단답':
        correct = answer.lower() in [a.lower() for a in data.answer.split('|')]
    if correct:
        st.success('정답입니다')
        st.session_state['correct_cnt'] += 1
    else:
        if give_up:
            st.info('아쉽습니다, 다음엔 꼭 풀어보세요!')
        else:
            st.warning('오답입니다')
        st.session_state['wrong_cnt'] += 1
    st.subheader('답')
    st.write(data.answer)
    if type(data.explain) != float:
            st.image(f'./img/{data.explain}')
    st.button('다음으로',
        use_container_width=True,
        on_click=next_question)

def next_question():
    st.session_state['page'] += 1
    st.session_state['answer'] = ''
    st.session_state['question'] = True