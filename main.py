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



# 실시간 동영상
st.subheader("실시간 매장 cctv")
video_file = open('testVideo.mp4', 'rb')
video_bytes = video_file.read()

st.video(video_bytes)