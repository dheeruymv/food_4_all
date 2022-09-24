'''
Created on 24-Sep-2022

@author: dheer
'''
import streamlit as st

class Register:
    
    def __init__(self, authenticator):
        self._auth_obj = authenticator
    
    def display_register_module(self):
        try:
            if self._auth_obj.register_user('Register user', preauthorization=False):
                st.success('User registered successfully')
        except Exception as e:
            st.error(e)