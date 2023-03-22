from layout import main
import streamlit as st

def app():
    st.set_page_config(
        page_title='정처기 실기 CBT',
        page_icon=':crystal_ball:')
    main()

if __name__ == "__main__":
    app()