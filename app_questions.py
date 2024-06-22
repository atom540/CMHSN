# app_questions.py

import streamlit as st
from CMHSN_evaluation import generate_gpt_response

def main():
    st.title('Mental Health Support Chatbot - Additional Questions')

    # Section for additional questions to GPT-3.5-turbo
    st.markdown('### Ask Additional Questions')
    user_question = st.text_area('Ask your additional question to the AI:')
    
    # Check if AI response is already in session state
    if 'gpt_response' not in st.session_state:
        st.session_state.gpt_response = ''

    if st.button('Get AI Response'):
        if user_question.strip() != '':
            gpt_response = generate_gpt_response(user_question)
            st.session_state.gpt_response = gpt_response
        else:
            st.warning('Please enter a question.')

    if st.session_state.gpt_response:
        st.subheader('AI Response:')
        st.write(st.session_state.gpt_response)

if __name__ == '__main__':
    main()
