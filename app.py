import streamlit as st
from transformers import pipeline
# from pathlib import Path
st.title("wanneemee KHAW-RAI")
st.subheader("kummakornKHAW kuuynaijor")

text = st.text_area('KHAW nai kub', '', height=200)
# st.write('This KHAW? -->', text)

if st.button('Generate headline'):
    summarizer = pipeline("summarization", model = "pannawittt/ruanglao-wanni" )
    headline = summarizer(text, max_length=256)
    desired_text = headline[0]['summary_text']
    st.write(desired_text)
