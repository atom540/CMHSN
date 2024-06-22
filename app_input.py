# app_input.py

import streamlit as st
from CMHSN_evaluation import generate_ai_recommendation

def main():
    st.title('Mental Health Support Chatbot - User Inputs')

    # Collect initial user inputs for mental health support
    issue_facing = st.text_area('What mental health issue are you facing?')
    duration_issue = st.text_area('How long have you been experiencing this issue?')
    sought_help = st.radio('Have you sought professional help before?', ['Yes', 'No'])
    specific_concerns = st.text_area('Do you have any specific concerns or symptoms you would like to share?')

    user_data = {
        'issue_facing': issue_facing,
        'duration_issue': duration_issue,
        'sought_help': sought_help,
        'specific_concerns': specific_concerns
    }

    # Button to get initial mental health advice
    if st.button('Get Initial Mental Health Advice'):
        if validate_inputs(user_data):  # Validate inputs before proceeding
            initial_advice = generate_ai_recommendation(user_data)
            st.subheader('Initial Mental Health Advice:')
            st.write(initial_advice)
        else:
            st.warning('Please fill in all required fields.')

def validate_inputs(user_data):
    # Validate if required fields are filled
    if not user_data['issue_facing'] or not user_data['duration_issue'] or not user_data['sought_help'] or not user_data['specific_concerns']:
        return False
    return True

if __name__ == '__main__':
    main()
