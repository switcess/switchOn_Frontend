import streamlit as st
import sys, os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from pages import videoPage
import pandas as pd
import numpy as np

st.title('SWITCH ON')

image = "assets/switcessLogo.png"
st.logo(image, link="https://github.com/switcess/switchOn_Frontend")



# 실시간 동영상
st.subheader("실시간 매장 cctv")
video_file = open('testVideo.mp4', 'rb')
video_bytes = video_file.read()

st.video(video_bytes)
st.write("2024-06-13") ######### 날짜 수정

# 월 별 이상행동 감지 그래프
st.subheader("월 별 이상행동 감지 그래프")
chart_data = pd.DataFrame(np.random.randn(10, 1))

st.line_chart(chart_data)

st.subheader('저장된 이상행동')

st.page_link("pages/videoPage.py", label="2024-07-18", icon = "🚨")
st.page_link("pages/test.py", label="2024-07-19", icon = "🚨")
st.page_link("pages/videoPage.py", label="2024-07-20", icon = "🚨")