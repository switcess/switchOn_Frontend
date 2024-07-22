import streamlit as st
import sys, os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from pages import videoPage
import pandas as pd
import numpy as np
import plotly.express as px

st.set_page_config(layout="wide")
empty1,con1,empty2 = st.columns([0.2,0.8,0.2])

# 대시보드
st.sidebar.page_link("main.py", label="실시간", icon = "🚨")
st.sidebar.page_link("pages/videoPage.py", label="과거 영상 보기", icon = "📼")
st.sidebar.page_link("pages/dashboard.py", label="대시보드", icon = "📈")


# 아이콘
image = "assets/switcessLogo.png"
st.logo(image, link="https://github.com/switcess/switchOn_Frontend")


# 이상행동 감지 그래프
st.title("이상행동 감지 그래프")

st.subheader("시간대")
chart_data = pd.DataFrame(np.random.randn(10, 1))

st.line_chart(chart_data)


col1, col2 = st.columns([1, 1])


chart_data = pd.DataFrame({
    'crime': ['절도', '방화', '도난', '전도'],
    'time': [1, 3, 5, 4]
})

with col1:
    st.subheader("월 별")
    fig = px.bar(chart_data, x='crime', y='time',
	text_auto=True) # text_auto: 값 표시 여부
    # fig.update_layout(width=800, height=600)
    # fig.update_traces(textangle=0) # 그래프 안에 텍스트 씌우기
    st.plotly_chart(fig)


with col2:
    st.subheader("파이")
    fig = px.pie(chart_data, names='crime', values='time', hole=.3) # hole을 주면 donut 차트

    fig.update_traces(textposition='inside', textinfo='percent+label+value')
    fig.update_layout(font=dict(size=14))
    fig.update(layout_showlegend=False) # 범례표시 제거

    st.plotly_chart(fig)