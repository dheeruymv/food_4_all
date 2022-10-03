'''
Created on 05-Sep-2022

@author: dheer
'''
import logging
import streamlit as st
from PIL import Image

from login.landing_page import Login
from utils.generalutils import GeneralUtils
from pages.welcomepage import WelcomePage

APP_NAME = "Food 4 All"


def _display_logo():
    rs_path = GeneralUtils().get_resource_path()
    logo_img = Image.open(str(rs_path)+"//food_4_all_logo.png")
    st.image(logo_img, caption="")
    

def main():
    #APP_NAME ## Displays application name
    _display_logo()
    auth_obj = Login().display_login_module()
    name, authentication_status, username = auth_obj.login('Login', 'main')
    logging.info("Name is : {}, authentication_status is : {} and username is {}".format(name, authentication_status, username))
    if st.session_state["authentication_status"]:
        auth_obj.logout('Logout', 'main')
        st.write(f'Welcome *{st.session_state["name"]}*')
        st.title('Welcome to our Food4All Service!')
        WelcomePage().display_welcome_page()
    elif st.session_state["authentication_status"] == False:
        st.error('Username/password is incorrect')
    elif st.session_state["authentication_status"] == None:
        st.warning('Please enter your username and password')


if __name__ == '__main__':
    main()