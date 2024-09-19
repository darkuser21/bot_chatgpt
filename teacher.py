from openai import OpenAI
import streamlit as me

api = me.secrets["API_KEY"]
user = OpenAI(api_key=api)
gptmodel = "gpt-3.5-turbo"
userrole = "user"

pre_promt = "Teach me the following concept : "
response = ""

me.title("SASTA TEACHER")
me.divider()
promt=me.text_input("TUZE KYA SIKNA HAI JALDI BATA NAHI TO CHALA JAUNGA!! ")
gptbutton = me.button("ARAM SE TOUCH KAR")
me.caption("TABHI KAM KARUNGA JAB TU ESE PYAR SE TOUCH KAREGA")
me.divider()

if gptbutton:
    with me.spinner(" SABAR KAR NAHI TO NIKAL"):
        response = user.chat.completions.create(
            model = gptmodel,
            message = [
                  {"role" : userrole, "content": pre_promt + promt }
            ]
        ) 
    me.snow()
    st.write(response.choice[0]. message.content)             
