import streamlit as st

st.set_page_config(page_tittle="chatbot app demo")
st.tittle("chatbot UI demo")

with st.chat_message("user"):
    st.write("Hello from the user side!")

with st.chat_message("assistant"):
    st.write("Hello from the llama3.2!")

user_message = st.chst_input("Type someting....")
if user_message:
    st.write(f"you:{user_message}")