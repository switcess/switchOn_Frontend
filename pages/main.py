# import streamlit as st
# import sys, os
# sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

# # st.set_page_config(layout="wide")
# st.set_page_config(page_title="main", layout="wide")

# if 'logged_in' not in st.session_state or not st.session_state.logged_in:
#     st.write("You need to log in first.")
#     st.markdown('<meta http-equiv="refresh" content="0; url=/app?page=login">', unsafe_allow_html=True)

# # 대시보드
# st.sidebar.page_link("main.py", label="실시간", icon = "🚨")
# st.sidebar.page_link("pages/videoPage.py", label="과거 영상 조회", icon = "📼")
# st.sidebar.page_link("pages/dashboard.py", label="월간 감지 보고서", icon = "📈")


# # 아이콘
# image = "assets/logo.png"
# st.logo(image, link="https://github.com/switcess/switchOn_Frontend")

# empty1,con1,empty2 = st.columns([0.2,0.8,0.2])

# st.title('Entry')

# # 실시간 동영상
# st.subheader("실시간 매장 cctv")
# video_file = open('mainVideo.mp4', 'rb')
# video_bytes = video_file.read()

# st.video(video_bytes, start_time=10, loop=True, autoplay=True, muted=True)

# import streamlit as st

# def render():
#     # if 'logged_in' not in st.session_state or not st.session_state.logged_in:
#     #     st.write("You need to log in first.")
#     #     st.query_params = {"page": "login"}
#     #     st.experimental_rerun()
#     #     return

#     st.title("Main Page")
#     st.write("You are logged in.")

#     # 예시 비디오 추가
#     # video_path = 'mainVideo.mp4'
#     # st.video(video_path, start_time=10, loop=True, autoplay=True, muted=True)
