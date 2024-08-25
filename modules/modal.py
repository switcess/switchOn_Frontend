import streamlit as st
from streamlit_modal import Modal

def show_modal():
    modal = Modal(key="Demo Key", title="저장된 이상 행동 비디오 없음")

    if 'modal_shown' not in st.session_state:
        st.session_state.modal_shown = False

    if not st.session_state.modal_shown:
        st.session_state.modal_shown = True
        with modal.container():
            st.markdown('비디오가 존재하지 않습니다.')