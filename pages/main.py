import streamlit as st
import pandas as pd
import numpy as np
import altair as alt

st.title('SWITCH ON')

image = "../assets/switcessLogo.png"
st.logo(image, link="https://github.com/switcess/switchOn_Frontend")

date = st.date_input("CCTV 날짜 확인")

chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])