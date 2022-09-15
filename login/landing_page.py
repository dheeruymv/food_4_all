'''
Created on 05-Sep-2022

@author: dheer
'''

import streamlit as st
import streamlit_authenticator as stauth

from streamlit_authenticator import Authenticate

import yaml
from yaml import SafeLoader

class Login:
    
    def __init__(self):
        pass
    
    def display_login_module(self):
        authenticator = ""
        with open('C://Users//dheer//eclipse-workspace//food_for_all//resources//login_config.yaml') as file:
            config = yaml.load(file, Loader=SafeLoader)
            authenticator = Authenticate(
                                config['credentials'],
                                config['cookie']['name'],
                                config['cookie']['key'],
                                config['cookie']['expiry_days'],
                                config['preauthorized']
                            )
        return authenticator