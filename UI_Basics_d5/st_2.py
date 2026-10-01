import streamlit as st

st.set_page_config(page_tittle = "Text input Demo")
st.tittle("text Input Demo")

name = st.text_input("Enter your name:" placeholder="e.g.shanti")
st.write(f"Hello,{name}!")
passward = st.text_input("Enter your passward:",type = passward)
st.write(f"Your Passward has {len(serect)} characters.")

comments = st.text_area("Any additional comments?",height = 150)
st.write(f"Your wrote {len(comments)} charecters.") 

if st.button("submit"):
    st.write("you clicked on submit!")

show_message = st.checkbox("Do you want an extra message?")
if show_message:
    st.write("This is the message.Have a good day!")