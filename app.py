# app.py

import streamlit as st
from app_input import main as input_main
from app_questions import main as questions_main

# Set page title
# st.title('Mental Health Support Chatbot')

# Create left sidebar navigation with a list
option = st.sidebar.radio(
    'Navigation',
    ['User Inputs', 'Additional Questions']
)

# Render selected page based on user's choice
if option == 'User Inputs':
    input_main()
elif option == 'Additional Questions':
    questions_main()
