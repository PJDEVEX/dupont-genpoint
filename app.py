import os
import tempfile
from dotenv import load_dotenv

import streamlit as st 
from google.auth.transport.requests import Request
from google.oauth2.service_account import Credentials
from google.auth.exceptions import RefreshError
import vertexai as vx
from vertexai.generative_models import GenerativeModel, Part
from PIL import Image
from google.cloud import storage
from src.fin_ast.fin_ast import upload_to_gcs, get_gemini_response, load_image_from_uri, input_prompt

load_dotenv()

BUCKET_NAME = os.getenv('BUCKET_NAME')

# Streamlit app
st.set_page_config(page_title="Financial Assistant", page_icon=":robot:")

st.header("Dupont GenPoint")
input = st.text_input("Input Prompt: ", key="input")

uploaded_file=st.file_uploader("Choose a file...", type=["jpg", "jpeg", "png", "webp"])
image_gcs_uri=""
if uploaded_file is not None:
    image=Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_column_width=True)

    # Upload the image to GCS
    if BUCKET_NAME:
        file_path = tempfile.NamedTemporaryFile(delete=False).name
        uploaded_file.seek(0)
        with open(file_path, "wb") as f:
            f.write(uploaded_file.read())
        image_gcs_uri = upload_to_gcs(file_path, BUCKET_NAME, uploaded_file.name)

submit=st.button(":rocket: Generate")

if submit:
    if BUCKET_NAME:
        image_part = load_image_from_uri(image_gcs_uri)
        response=get_gemini_response(input_prompt, image_part, input)

    st.subheader("Answer:")
    st.write(response)