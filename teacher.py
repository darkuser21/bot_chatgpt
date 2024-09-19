from openai import OpenAI
import streamlit as me

# Get API key from secrets
api = me.secrets["API_KEY"]
user = OpenAI(api_key=api)
gptmodel = "gpt-3.5-turbo-0125"
userrole = "user"

pre_prompt = "Teach me the following concept: "
response = ""

# Streamlit interface
me.title("SASTA TEACHER")
me.divider()
prompt = me.text_input("TUZE KYA SIKHNA HAI JALDI BATA, NAHI TO CHALA JAUNGA!!")
gptbutton = me.button("ARAM SE TOUCH KAR")
me.caption("TABHI KAM KARUNGA JAB TU ESE PYAR SE TOUCH KAREGA")
me.divider()

if gptbutton:
    with me.spinner("SABAR KAR NAHI TO NIKAL"):
        response = user.chat.completions.create(
            model=gptmodel,
            messages=[
                {"role": userrole, "content": pre_prompt + prompt}
            ]
        )
    
    me.snow()
    me.write(response.choices[0].message['content'])
