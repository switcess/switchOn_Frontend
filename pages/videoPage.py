import streamlit as st

st.title('2024-06-13')


# 실시간 동영상
video_file = open('testVideo.mp4', 'rb')
video_bytes = video_file.read()

st.video(video_bytes)
st.write("2024-06-13") ######### 날짜 수정

# ## 다운로드 버튼
# with open("testVideo.mp4", "rb") as video:
#     btn = st.download_button(
#             label="Download",
#             data=video,
#             file_name="testVideo.mp4",
#             mime="video/mp4"
#           )

# col = st.columns((1.5, 4.5, 2), gap='medium')

col1,col2,col3 = st.columns([1,2,1], gap='medium')
with col1 :
  st.button('절도')
with col2 :
  st.button('이상행동')
with col3 :
  ## 다운로드 버튼
  with open("testVideo.mp4", "rb") as video:
      btn = st.download_button(
              label="Download",
              data=video,
              file_name="testVideo.mp4",
              mime="video/mp4"
            )

# def st_tags(value: list,
#             suggestions: list,
#             label: str,
#             text: str,
#             maxtags: int,
#             key=None) -> list:

#   keywords = st_tags(
#       label='# Enter Keywords:',
#       text='Press enter to add more',
#       value=['Zero', 'One', 'Two'],
#       suggestions=['five', 'six', 'seven', 
#                   'eight', 'nine', 'three', 
#                   'eleven', 'ten', 'four'],
#       maxtags = 4,
#       key='1')

# st_tags()