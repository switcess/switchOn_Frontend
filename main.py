import streamlit as st
import sys, os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from pages import videoPage
import pandas as pd
import numpy as np


st.set_page_config(layout="wide")

# 대시보드
st.sidebar.page_link("main.py", label="실시간", icon = "🚨")
st.sidebar.page_link("pages/videoPage.py", label="과거 영상 보기", icon = "📼")
st.sidebar.page_link("pages/dashboard.py", label="대시보드", icon = "📈")


# 아이콘
image = "assets/switcessLogo.png"
st.logo(image, link="https://github.com/switcess/switchOn_Frontend")




empty1,con1,empty2 = st.columns([0.2,0.8,0.2])

st.title('SWITCH ON')



# page = "https://github.com/switcess/switchOn_Frontend"
# st.sidebar.title("ON")

# pages = {
#     "Page" : [
#         st.Page("pages/monthGraph.py", title="월 별 이상행동 통계")
#     ]
# }

# st.navigation(pages, position="sidebar")

# st.write(st.session_state.foo)

# 레이아웃 짜기
# col1,col2 = st.columns([6,4])
# with col1 :
#   st.title('here is column1')
# with col2 :
#   st.title('here is column2')
#   st.checkbox('this is checkbox1 in col2 ')

# 실시간 동영상
st.subheader("실시간 매장 cctv")
video_file = open('testVideo.mp4', 'rb')
video_bytes = video_file.read()

st.video(video_bytes)
st.write("2024-06-13") ######### 날짜 수정


# st.sidebar.button("Reset", type="primary")


# col1,col2 = st.columns([2,1], gap='medium')

# with col1:
#     # 월 별 이상행동 감지 그래프
#     st.subheader("월 별 이상행동 감지 그래프")
#     chart_data = pd.DataFrame(np.random.randn(10, 1))

#     st.line_chart(chart_data)

# with col2:
#     st.subheader('저장된 이상행동')

#     st.page_link("pages/videoPage.py", label="2024-07-18", icon = "🚨")
#     st.page_link("pages/test.py", label="2024-07-19", icon = "🚨")
#     # st.page_link("pages/page_2.py", label="2024-07-20", icon="2️⃣", disabled=True)
#     st.page_link("pages/videoPage.py", label="2024-07-20", icon = "🚨")