import openai
import streamlit as st
from streamlit_chat import message
import json

openai.api_key = st.secrets["pass"]

def generate_response(prompt):
    
    response = openai.Completion.create(
        #engine="text-davinci-003",
        engine="ada",
        prompt=prompt,
        max_tokens=100,
        n=1,
        stop=None,
        temperature=0.0
    )
    
    message = response.choices[0].text
    
    return message

st.title('Welcome to Doctor Appointment Center')

intro_message = "How Can I Help You?"

########################################
with open('data.json', 'r') as f:
  schedule_data = json.load(f)

print(schedule_data)

# line1 = f"Doctors Availability:\n\n"
# slen = 8
# space1 = " "*5
# space2 = " "*10
# line2 = f"Name{space2}Department{space2}Location{space2}Date{space2}Time\n"
# line3 = f"\n"
# header = line1+line2+line3

sch_info = header
for item in schedule_data:
  # name = item['doctor']
  # department = 'General'
  # location = 'Main Office'
  # date = item['date']
  # time = item['availability']
  sch_info = += f'{item}\n'
  # sch_info += f'{name.ljust(slen)}\t{department.ljust(slen)}\t{location.ljust(slen)}\t{date.ljust(slen)}\t{time}\n'

########################################

if 'generated' not in st.session_state:
    st.session_state['generated'] = []

if 'past' not in st.session_state:
    st.session_state['past'] = []

def get_text():
    #input_text = st.text_input('You: ','Hello, How are you?', key='input')
    input_text = st.text_input('',placeholder=intro_message)
    return input_text

user_input = get_text()

if user_input == "show doctors schedule":
  output = sch_info
  st.session_state.past.append(user_input)
  st.session_state.generated.append(output)
elif user_input:
    output = generate_response(user_input)
    st.session_state.past.append(user_input)
    st.session_state.generated.append(output)
else:
  pass

if st.session_state['generated']:
    for i in range(len(st.session_state['generated'])-1, -1, -1):
        message(st.session_state['generated'][i], key=str(i))
        message(st.session_state['past'][i], is_user=True, key=str(i) + '_user')


