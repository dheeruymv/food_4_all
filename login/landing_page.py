'''
Created on 05-Sep-2022

@author: dheer
'''

import streamlit as st
from streamlit_authenticator import Authenticate

import yaml
from yaml import SafeLoader

from login.register_page import Register

class Login:
    
    def __init__(self):
        pass
    
    def display_login_module(self):
        self.authenticator = ""
        col1, col2, col3 = st.columns(3)
        with open('C://Users//dheer//eclipse-workspace//food_for_all//resources//login_config.yaml') as file:
            config = yaml.load(file, Loader=SafeLoader)
            self.authenticator = Authenticate(
                                config['credentials'],
                                config['cookie']['name'],
                                config['cookie']['key'],
                                config['cookie']['expiry_days'],
                                config['preauthorized']
                            )
        print("Before clicking register button")
        register_result = st.button("Register")
        print("After clicking register buttono : {}".format(register_result))
        if register_result:
            print("Displaying register module")
            if Register(self.authenticator).display_register_module():
                #super()
                print("Existing users are : {}".format(self.authenticator.credentials))
                print("session state has : {}".format(st.session_state))
                if 'Email' not in st.session_state:
                    st.session_state['Email'] = st.text_input('Email')
                print("Session state after: {}".format(st.session_state))
        return self.authenticator