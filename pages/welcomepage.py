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
        receipe_rest = st.button("Get Receipe!!")
        if receipe_rest:
            self._display_receipe(food)
        
    def _display_and_get_food_based_on_diet(self, diet_option):
            if "Vegan" in diet_option:
                choice_of_food = st.multiselect(
                    "Choose your food",
                    ["phyllo dough","walnuts","cinnanmon","water","honey","melted chocolate","unsalted butter",
                     "legumes","brocolli","Tofu","hemp seeds","flax seeds","chia seeds"])
            if diet_option == "Vegetarian":
                choice_of_food = st.multiselect(
                    "Choose your food",
                    ["white rice","brown rice","tomatoes","black beans","garlic","peppers","corn",
                     "milk","plantain","lemon","avocado","bell pepper","celery", "egg plant"])
            if "Non-Veg" in diet_option:
                choice_of_food = st.multiselect(
                    "Choose your food",
                    ["Chicken","tomatoes","spring onion","lamb","pork","fish","prawns",
                     "rice","beef","eggs","calamari","bell pepper","celery", "onions"])
            return choice_of_food
        
    def _display_receipe(self, food):
        st.markdown("""
                <style>
                .big-font {
                font-size:100px !important;
                        }
                </style>
            """, unsafe_allow_html=True)
        if food:  ### Integrate with Anju's receipe preparation python script
            st.markdown("**Generated receipe with food selected: {}** :smile:".format("Baklava"))
            #st.write("Do you want to order food!?")
            order_food = st.radio("Do you want to order food!?",('Yes','No'))
            #order_food_no = st.checkbox('No')
            #st.write(order_food_yes)
            #st.write(order_food_no)
            if order_food == "Yes":
                self._order_food_based_on_user_selection(order_food)
            elif order_food == "No":
                self._order_food_based_on_user_selection(order_food)
            
    def _order_food_based_on_user_selection(self, order_food):
        if order_food == "Yes":
            zip_code = st.number_input("Zip Code", max_value=99999)
            address = st.text_area("Address")
            order_placed = st.button("Order food!")
            if order_placed:
                st.write("List of restaurants to be displayed")
        elif order_food == "No":
            st.write("Get receipe to your mailbox!")
            email = st.text_input("Email")
            if email:
                send_email = st.button("Get mail")
                if send_email:
                    st.write("Email sent successfully! Enjoy your cooking & food! :smile:")
            
                