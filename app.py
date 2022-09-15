'''
Created on 05-Sep-2022

@author: dheer
'''
import streamlit as st
import numpy as np
import pandas as pd

from login.landing_page import Login

APP_NAME = "Food 4 All"

def main():
    APP_NAME ## Displays application name
    auth_obj = Login().display_login_module()
    name, authentication_status, username = auth_obj.login('Login', 'main')
    # dataframe = pd.DataFrame(
    # np.random.randn(10, 20),
    # columns=('col %d' % i for i in range(20)))
    # st.table(dataframe)



if __name__ == '__main__':
    main()