import streamlit as st
import sys, os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objs as go

# st.set_page_config(layout="wide")
empty1,con1,empty2 = st.columns([0.2,0.8,0.2])

st.set_page_config(page_title="dashboard", layout="wide")


# 대시보드
st.sidebar.page_link("main.py", label="실시간", icon = "🚨")
st.sidebar.page_link("pages/videoPage.py", label="과거 영상 조회", icon = "📼")
st.sidebar.page_link("pages/dashboard.py", label="월간 감지 보고서", icon = "📈")


# 아이콘
image = "assets/logo.png"
st.logo(image, link="https://github.com/switcess/switchOn_Frontend")


# 이상행동 감지 그래프
st.title("이상행동 감지 그래프")

container = st.container(border=True)
container.markdown(
    """
    이번 달은 <span style="font-size: 18px; font-weight: bold; color: red;">도난</span>이 가장 많이 일어났으며, 
    <span style="font-size: 18px; font-weight: bold; color: red;">00:30-1:30</span> 사이에 이상 행동이 가장 많이 감지됩니다.
    """,
    unsafe_allow_html=True
)


col1, col2 = st.columns([1, 1])

crime_data = pd.DataFrame({
            'crime': ['절도', '방화', '도난', '전도'],
            'time': [1, 3, 5, 4]
        })

with col1:
    st.subheader("시간대")
    time_data = pd.DataFrame(np.random.randn(10, 1), columns=["이상행동 감지"])
    fig = go.Figure()
    fig.add_trace(go.Scatter(y=time_data["이상행동 감지"], mode='lines'))

    fig.update_layout(
        width=400,
        height=200,
        margin=dict(l=20, r=20, t=20, b=20)
    )
    st.plotly_chart(fig)



    st.subheader("월 별")
    fig = px.bar(crime_data, x='crime', y='time', text_auto=True)
    fig.update_layout(width=400, height=300)
    st.plotly_chart(fig)

with col2:
    st.subheader("파이")
    fig = px.pie(crime_data, names='crime', values='time', hole=.3)

    fig.update_traces(textposition='inside', textinfo='percent+label+value')
    fig.update_layout(width=550, height=550)
    fig.update_layout(font=dict(size=14))
    fig.update(layout_showlegend=False)

    st.plotly_chart(fig)