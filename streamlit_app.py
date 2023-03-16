import openai
import streamlit as st
from streamlit_chat import message

openai.api_key = st.secrets["pass"]

def generate_response(prompt):
    
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.3
    )
    
    message = response.choices[0].text
    
    return message

st.title('Welcome to Doctor Appointment Center')

intro_message = "Hi there! I'm here to help you schedule an appointment with one of our doctors. What type of appointment would you like to schedule?"

if 'generated' not in st.session_state:
    st.session_state['generated'] = []

if 'past' not in st.session_state:
    st.session_state['past'] = []

def get_text():
    #input_text = st.text_input('You: ','Hello, How are you?', key='input')
    input_text = st.text_input('',placeholder=intro_message)
    return input_text

user_input = get_text()

if user_input:
    output = generate_response(user_input)
    st.session_state.past.append(user_input)
    st.session_state.generated.append(output)

if st.session_state['generated']:
    for i in range(len(st.session_state['generated'])-1, -1, -1):
        message(st.session_state['generated'][i], key=str(i))
        message(st.session_state['past'][i], is_user=True, key=str(i) + '_user')


