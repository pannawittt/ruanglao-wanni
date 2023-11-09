import streamlit as st
from transformers import pipeline
from pathlib import Path
st.title("wanneemee KHAW-RAI")
st.subheader("kummakornKHAW kuuynaijor")

text = st.text_area('KHAW nai kub', '', height=200)
st.write('This KHAW? -->', text)
cloud_model_location = "1Vek2BMm-i0WCp6kbBBG42APE3Vp9iLK9"

def load_model():

    save_dest = Path('model')
    save_dest.mkdir(exist_ok=True)
    
    f_checkpoint = Path("model/skyAR_coord_resnet50.pt")

    if not f_checkpoint.exists():
        with st.spinner("Downloading model... this may take awhile! \n Don't stop it!"):
            from GD_download import download_file_from_google_drive
            download_file_from_google_drive(cloud_model_location, f_checkpoint)
    
    model = "checkpoint-4500"
    return model


if st.button('Generate headline'):
    summarizer = pipeline("summarization", model= load_model())
    headline = summarizer(text, max_length=256)
    desired_text = headline[0]['summary_text']
    st.write(desired_text)