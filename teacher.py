import OpenAI
import streamlit as me

user = OpenAI(api_key= "sk-Y4t-t7IbTFyD9DFZ7J0RsPJnx9hNd1rxRiGg054hmqT3BlbkFJM5QzFW7cfD6znNWEetlnTtqVwyEj1X4EqF5kDsnXIA")
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
