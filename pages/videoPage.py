import streamlit as st

st.title('2024-06-13')


# 실시간 동영상
video_file = open('testVideo.mp4', 'rb')
video_bytes = video_file.read()

st.video(video_bytes)
st.write("2024-06-13") ######### 날짜 수정

## 다운로드 버튼
with open("testVideo.mp4", "rb") as video:
    btn = st.download_button(
            label="Download",
            data=video,
            file_name="testVideo.mp4",
            mime="video/mp4"
          )