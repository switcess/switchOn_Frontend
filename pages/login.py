# login.py

import streamlit as st

def render():
    st.title("Login")
    # username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        # if username == "Entry" and password == "qlalfqjsgh":
            st.session_state.page = "main"
            st.experimental_rerun()  # 페이지 새로고침
        # else:
            # st.error("정보가 일치하지 않습니다. 다시 로그인 해 주세요.")
