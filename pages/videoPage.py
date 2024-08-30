import streamlit as st
import sys, os
from datetime import datetime
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
import modules.modal as modal
from modules.findAllVideo import findAllVideo

st.set_page_config(layout="wide")
empty1, con1, empty2 = st.columns([0.2, 0.8, 0.2])

def openVideo():
    video_file = open('testVideo.mp4', 'rb')
    video_bytes = video_file.read()
    start_time = st.session_state.get('video_start_time', 0)
    return st.video(video_bytes, start_time=start_time, loop=True, autoplay=True, muted=True)

# Sidebar
st.sidebar.page_link("main.py", label="실시간", icon="🚨")
st.sidebar.page_link("pages/videoPage.py", label="과거 영상 조회", icon="📼")
st.sidebar.page_link("pages/dashboard.py", label="월간 통계 보고서", icon="📈")

# Logo
image = "assets/switcessLogo.png"
st.logo(image, link="https://github.com/switcess/switchOn_Frontend")

st.title(str(datetime.now().strftime('%Y-%m-%d')))

col1, col2 = st.columns([3, 1])

with col1:
    col1_1, col1_2 = st.columns([1, 1])
    with col1_1:
        selected_date = st.date_input("select month")
        resultList = findAllVideo(selected_date)
    with col1_2:
        selected_time = st.time_input("select date")
with col2:
    options = st.multiselect(
        "범죄",
        ["절도", "분실", "방화", "전도"],
        ["절도", "전도"]
    )

st.markdown(''' #### 절도 13:25:15''')
col1, col2 = st.columns([3, 1])

with col1:
    openVideo()

with col2:
    st.subheader('저장된 이상행동')
    time_offsets = [10, 20, 30, 40]
    
    for i, result in enumerate(resultList):
        button_label = f"🚨 {result['actions']} {result['time']}"
        if st.button(label=button_label, key=f"button_{i}"):
            st.session_state.video_start_time = time_offsets[i]

    col3, col4 = st.columns([1, 1.5])
    ## Download button
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
