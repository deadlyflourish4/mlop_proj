import streamlit as st
from btn_dowload_model import *
# from btn_predict import classifier
from transformers import pipeline
# import

st.title("ML Deployment Here!!!")
# download_dir(local_path, s3_prefix)
btn_download = st.button("Download model")
if btn_download:
    with st.spinner("Downloading... Pls wait!"):
        download_dir(local_path, s3_prefix)

text = st.text_area("Enter your review", placeholder="Type here...")
btn_predict = st.button("Predict")
if btn_predict:
    with st.spinner("Predicting... Pls wait!"):
        classifier = pipeline('text-classification', model='tinybert-sentiment-analysis', device='cuda')

        ouput = classifier(text)
        st.write(ouput)
