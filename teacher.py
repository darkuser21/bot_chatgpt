from openai import OpenAI
import streamlit as me

user = OpenAI(api_key= "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")
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
                  {"role" : userrole, "content": pre_prompt + prompt }
            ]
        ) 
    me.snow()
    st.write(response.choice[0]. message.content)             
