import streamlit as st # type: ignore
import sys, os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from pages import videoPage
import pandas as pd # type: ignore
import numpy as np # type: ignore
import datetime

st.set_page_config(layout="wide")
empty1,con1,empty2 = st.columns([0.2,0.8,0.2])

def isNotFoundVideo(date):
  if date == datetime.datetime.today().date(): # TODO : 오늘 날짜면 비디오 없다고 가정
    photo_file = open('assets/notFound.png', 'rb')
    photo_bytes = photo_file.read()
    st.markdown("> | **저장된 이상 행동 비디오가 존재하지 않습니다.** |")
    # st.write('저장된 이상 행동 비디오가 존재하지 않습니다.')
    return st.image(photo_bytes)
  else:
    video_file = open('testVideo.mp4', 'rb')
    video_bytes = video_file.read()
    return st.video(video_bytes)


# 대시보드
st.sidebar.page_link("main.py", label="실시간", icon = "🚨")
st.sidebar.page_link("pages/videoPage.py", label="과거 영상 보기", icon = "📼")
st.sidebar.page_link("pages/dashboard.py", label="대시보드", icon = "📈")


# 아이콘
image = "assets/switcessLogo.png"
st.logo(image, link="https://github.com/switcess/switchOn_Frontend")



st.title('2024-07-23')

col1, col2 = st.columns([3, 1])

with col1:
  col1_1, col1_2 = st.columns([1, 1])
  with col1_1:
    d = st.date_input("select month", )
  with col1_2:
    d = st.time_input("select date", )
with col2:
  options = st.multiselect(
    "범죄",
    ["절도", "분실", "방화", "전도"],
    ["절도", "방화"])

st.markdown(''' #### 절도 13:25:15''')
col1, col2 = st.columns([3, 1])

with col1:
  # 실시간 동영상
  isNotFoundVideo(d)

with col2:
  st.subheader('저장된 이상행동')
  st.page_link("pages/dashboard.py", label="절도 13:25:15", icon = "🚨")
  st.page_link("pages/dashboard.py", label="방화 15:27:32", icon = "🚨")
  st.page_link("pages/dashboard.py", label="절도 23:49:58", icon = "🚨")

  col3, col4 = st.columns([1, 1.5])
  ## 다운로드 버튼
  with col3:
    with open("testVideo.mp4", "rb") as video:
      btn = st.download_button(
              label="다운로드",
              data=video,
              file_name="testVideo.mp4",
              mime="video/mp4", type="primary"
            )
  with col4:
    if st.button(label="신고"):
          st.markdown(f'<meta http-equiv="refresh" content="0; url=https://www.police.go.kr/">', unsafe_allow_html=True)

