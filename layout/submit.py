import streamlit as st

def handle_submit(data):
    st.session_state['question'] = False
    answer = st.session_state['answer']
    correct = None
    if data.kind == '단답':
        correct = answer.lower() in data.answer.split('|')
    if correct:
        st.success('정답입니다')
        st.session_state['correct_cnt'] += 1
    else:
        st.warning('오답입니다')
        st.session_state['wrong_cnt'] += 1
    st.markdown(f'**답** : {data.answer}')
    st.button('다음으로',
        use_container_width=True,
        on_click=next_question)