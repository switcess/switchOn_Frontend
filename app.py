import streamlit as st
import pages.login as login

# 페이지 설정을 앱의 시작 부분에 호출
st.set_page_config(page_title="app", layout="wide")

# 쿼리 파라미터 가져오기
# query_params = st.query_params
# page = query_params.get("page", ["login"])[0]

if 'page' not in st.session_state:
    st.session_state.page = "login"

# 페이지에 따라 콘텐츠 렌더링
if st.session_state.page == "login":
    try:
        login.render()  # login.py의 render() 함수 호출
    except ImportError:
        st.error("로그인 페이지를 찾을 수 없습니다.")
# elif page == "main":
#     try:
#         import pages.main as main  # main.py에서 import
#         # main.render()  # main.py의 render() 함수 호출
#     except ImportError:
#         st.error("메인 페이지를 찾을 수 없습니다.")
else:
    st.write("잘못된 접근입니다.")
