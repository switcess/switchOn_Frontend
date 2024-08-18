import streamlit as st # type: ignore
import sys, os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from pages import videoPage
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objs as go

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

container = st.container(border=True)
container.markdown(
    """
    이번 달은 <span style="font-size: 18px; font-weight: bold;">도난</span>이 가장 많이 일어났으며, 
    <span style="font-size: 18px; font-weight: bold;">00:30-1:30</span> 사이에 이상 행동이 가장 많이 감지됩니다.
    """,
    unsafe_allow_html=True
)


col1, col2 = st.columns([1, 1])

crime_data = pd.DataFrame({
            'crime': ['절도', '방화', '도난', '전도'],
            'time': [1, 3, 5, 4]
        })

with col1:
    # 두 번째 데이터프레임
    st.subheader("시간대")
    time_data = pd.DataFrame(np.random.randn(10, 1), columns=["이상행동 감지"])

    # Plotly를 사용하여 크기를 조절한 라인 차트 생성
    fig = go.Figure()

    # 라인 차트 추가
    fig.add_trace(go.Scatter(y=time_data["이상행동 감지"], mode='lines'))

    # 차트 레이아웃 크기 조절
    fig.update_layout(
        width=400,  # 차트의 가로 크기
        height=200,  # 차트의 세로 크기
        margin=dict(l=20, r=20, t=20, b=20)  # 마진 조절
    )

    # Streamlit에 차트 표시
    st.plotly_chart(fig)



    st.subheader("월 별")
    fig = px.bar(crime_data, x='crime', y='time', text_auto=True)
    fig.update_layout(width=400, height=300)
    st.plotly_chart(fig)

with col2:
    st.subheader("파이")
    fig = px.pie(crime_data, names='crime', values='time', hole=.3) # hole을 주면 donut 차트

    fig.update_traces(textposition='inside', textinfo='percent+label+value')
    fig.update_layout(width=550, height=550)
    fig.update_layout(font=dict(size=14))
    fig.update(layout_showlegend=False) # 범례표시 제거

    st.plotly_chart(fig)