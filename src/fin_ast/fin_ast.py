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

# Load env variables
load_dotenv()

KEY_PATH = os.getenv('GOOGLE_APPLICATION_CREDENTIALS')
PROJECT_ID = os.getenv('PROJECT_ID')    
REGION = os.getenv('REGION')
MODEL = os.getenv('MODEL')
BUCKET_NAME = os.getenv('BUCKET_NAME')

# Allowed MIME types for image upload
allowed_mime_types = ["image/png", "image/jpeg", "image/gif", "image/webp"]

def get_service_account_credentials(key_path: str) -> Credentials:
    """
    Get service account credentials from the key file 
    """
    try:
        # with open(KEY_PATH, 'r') as key_file:
        credentials = Credentials.from_service_account_file(
                key_file, 
                scopes=["https://www.googleapis.com/auth/cloud-platform"],
                )
        return credentials
    except(IOError, FileNotFoundError) as e:
        raise IOError(f"Error in reading service account key file: {e}") from e
    except RefreshError as e:
        raise RefreshError(f"Error in refreshing access token: {e}") from e

key_file = KEY_PATH
credentials = get_service_account_credentials(KEY_PATH)

def initialize_vertexai_client(project: str, region: str, credentials: Credentials) -> vx:
    """
    Initialize Vertex AI client
    """
    try:
        client = vx.init(project=PROJECT_ID)
        return client
    except RefreshError as e:
        st.error("Internal Server Error, Please try again later.")
        raise RefreshError(f"Error in initializing Vertex AI client: {e}") from e

def upload_to_gcs(file_path, bucket_name, destination_blob_name):
    "Upload file to GCS and return the GCS URI"
    storage_client = storage.Client()
    bucket = storage_client.bucket(BUCKET_NAME)
    blob = bucket.blob(destination_blob_name)

    try:
        blob.upload_from_filename(file_path)
        gcs_uri = f"gs://{bucket_name}/{destination_blob_name}"
        return gcs_uri
    except Exception as e:
        print(f"Error in uploading file to GCS: {e}")
        st.error("Internal Server Error, Please try again later.")
        raise


vertexai_client = initialize_vertexai_client(PROJECT_ID, REGION, credentials)

def get_gemini_response(input, image, prompt):
    """
    Get response from Gemini model 
    """
    # loading the model
    model=GenerativeModel(MODEL)
    try:
        response = model.generate_content(
        [input, image, prompt,])
    except Exception as e:
        st.error("Internal Server Error, Please try again later.")
        raise Exception(f"Error in generating content: {e}") from e
    return response.text

input_prompt=""" 
You are an qualified and well experienced Financial Analyst and a strategist \
with a proven track record of delivering high quality financial analysis and \
strategic insights. You have a strong understanding of financial statements, \
financial modeling, and valuation. You have a strong analytical mindset and \
are able to think critically and solve complex problems. You are a self-starter \
and are able to work independently with minimal supervision. You are a team player \
and are able to work effectively with cross-functional teams. You have excellent \
communication skills and are able to present complex financial information in a \
clear and concise manner. You are highly organized and detail-oriented and are able \
to manage multiple projects simultaneously. You are proficient in Microsoft Excel, \

You will receive various financial data and reports from various sources and you will \
be required to analyze the data and provide accurate analysis and insights and strategic \
recommendations to based on the input files and the questions asked by the user.

Your analysis should be based on the given data and should be accurate and well-reasoned \
importantly.
"""

def load_image_from_uri(uri, mime_types=allowed_mime_types):
    for mime_type in mime_types:
        try:
            return Part.from_uri(uri, mime_type=mime_type)
        except Exception as e:
            print(f"Failed to load image with MIME type {mime_type}: {e}")
    raise Exception("Failed to load image with any of the provided MIME types")
