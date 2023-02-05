import streamlit as st
import vertaler

st.title('Straatvertaler App')
st.subheader("Nederlands:")
message = st.text_input("Wat wil je zeggen?", key="name")
translation = vertaler.main(message)
st.subheader("Vertaling:")
# The reason for markdown is because it's plain
st.code(translation, language="markdown")
