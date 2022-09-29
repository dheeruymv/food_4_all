'''
Created on 28-Sep-2022

@author: dheer
'''

import streamlit as st

class WelcomePage:
    
    def __init__(self):
        pass
    
    def display_welcome_page(self):
        col1, col2 = st.columns(2)
        with col2:
            diet_option = st.selectbox(
                "Choose your diet",
                ("Vegan","Vegetarian","Non-Vegetarain"),
                label_visibility=st.session_state.visibility,
                disabled=st.session_state.disabled,)