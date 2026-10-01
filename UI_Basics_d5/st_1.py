import streamlit as st

st.set_page_config(page_tittle = "Streamlit Demo", page_icon=".")
st.title("streamlit Demo")

st.write("this is plain text.")

st.markdown("This is **bold**, this is *italic*,this is :blue[coloured.]")

st.write("You can also include a divider.")

st.divider()