'''
Created on 28-Sep-2022

@author: dheer
'''

import streamlit as st

class WelcomePage:
    
    def __init__(self):
        # Store the initial value of widgets in session state
        if "visibility" not in st.session_state:
            st.session_state.visibility = "visible"
            st.session_state.disabled = False
    
    def display_welcome_page(self):
        col1, col2 = st.columns(2)
        with col1:
            diet_option = st.selectbox(
                "Choose your diet",
                ("Vegan","Vegetarian","Non-Veg"),
                label_visibility=st.session_state.visibility,
                disabled=st.session_state.disabled,)
        food = self._display_and_get_food_based_on_diet(diet_option)
        self._display_receipe(food)
        
    def _display_and_get_food_based_on_diet(self, diet_option):
            if "Vegan" in diet_option:
                choice_of_food = st.selectbox(
                    "Choose your food",
                    ("phyllo dough","walnuts","cinnanmon","water","honey","melted chocolate","unsalted butter",
                     "legumes","brocolli","Tofu","hemp seeds","flax seeds","chia seeds"),
                    label_visibility=st.session_state.visibility,
                    disabled=st.session_state.disabled,)
            if diet_option == "Vegetarian":
                choice_of_food = st.selectbox(
                    "Choose your food",
                    ("white rice","brown rice","tomatoes","black beans","garlic","peppers","corn",
                     "milk","plantain","lemon","avocado","bell pepper","celery", "egg plant"),
                    label_visibility=st.session_state.visibility,
                    disabled=st.session_state.disabled,)
            if "Non-Veg" in diet_option:
                choice_of_food = st.selectbox(
                    "Choose your food",
                    ("Chicken","tomatoes","spring onion","lamb","pork","fish","prawns",
                     "rice","beef","eggs","calamari","bell pepper","celery", "onions"),
                    label_visibility=st.session_state.visibility,
                    disabled=st.session_state.disabled,)
            return choice_of_food
        
    def _display_receipe(self, food):
        if food:
            st.write("Generated receipe with food selected: {}".format("Baklava"))
                