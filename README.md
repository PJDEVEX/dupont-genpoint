# Dupont GenPoint

![Dupont GenPoint](https://res.cloudinary.com/pjdevex/image/upload/v1713107004/Screenshot_2024-04-14_170232_hdhegb.png)

[Click here view the Demo...](https://drive.google.com/file/d/1Vj0Qv3x4yj6P39U_Zxsk2wD5sv1f312r/view?usp=sharing)

<h2>DuPont GenPoint: A Powerful Financial Analysis Tool</h2>

<strong>DuPont GenPoint</strong> is a powerful financial analysis application designed to empower financial professionals with the capabilities to extract strategic insights from complex financial data from image based sources.

## Key Features:

- <strong>Automated Data Analysis:</strong> Leverage the power of Vertext AI's generative AI framework and Gemini-1.0-Pro-Vision models to automate data analysis from various financial sources.
- <strong>Strategic Recommendations:</strong> Gain actionable insights and strategic recommendations derived from a deep understanding of financial statements, valuation, and financial modeling.
- <strong>Streamlined User Experience:</strong> The intuitive web app interface allows you to effortlessly upload files, receive analysis, and explore results.

## Benefits:

- <strong>Improved Efficiency:</strong> Automate time-consuming data analysis tasks, freeing up valuable time for strategic decision-making.
- <strong>Data-Driven Decisions:</strong> Make informed choices based on accurate and well-reasoned analysis.
- <strong>Enhanced Accuracy:</strong> Mitigate human error with AI-powered data processing and analysis.
- <strong>Simplified Collaboration:</strong> Share insights and recommendations seamlessly with colleagues through the web app interface.

## Future development:
- Financial professional, please feel free to share your challenges that you face on your daily routine. We are here to develop the ultimate system for you...

## Special Credit
Special thanks are due to my better half, [Ruvini](https://www.linkedin.com/in/ruvini-perera/), for her unwavering support. I also extend my gratitude to [Code Institute](https://codeinstitute.net/) for laying the foundation of my coding career and helping me discover my passion.


This README provides a comprehensive guide to installing, configuring, using DuPont GenPoint to unlock the power of <strong>AI-driven financial analysis</strong> while presenting the process flow of the project and core tech stack used for the development.

## How to set up the project

<details>
  <summary>Click here...</summary>

### Step 1: Clone the repo
```bash
Project repo: https://github.com/PJDEVEX/dupont-genpoint
```
### Step 2: Create Virtual Environment
- Activate virtual environment
```bash
source ~/anaconda3/bin/activate
```
```bash
conda create -n p-gemini python=3.10 -y
```
```bash
conda activate p-gemini
```

### Step3: Install project dependencies
```bash
pip3 install -r requirements.txt
```

### Step4: Define Env variables
- create `.env`

```ini
import os

GOOGLE_APPLICATION_CREDENTIALS="xxxxxxxxxxxxxxxxxxxxxxxxxx"
PROJECT_ID=xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
REGION=xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
MODEL=xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
BUCKET_NAME=xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

```

### Step5: Google Cloud 

- Create a new project
- Create a new credentials - Service Account (Grant the permission so that account can have admin permission to both `Vertextai` as well as `Google Cloud Storage` )
- Add a new api key and download the json
- Optionally, the above can be done using the google cloud cli
- move the json file to credentials folder

### Step6: Google Google Cloud Storage
- Create a google bucket
- update the ENV var

### Step7. Update Vartextai variables
- Project_ID can be found in the .json file downloaded earlier.
- Select a region at your [choice](https://cloud.google.com/compute/docs/regions-zones).
- Select a LLM model of your [choice](https://ai.google.dev/models/gemini) that support text image and text compatibility. 

### Step6: Install local Variables
  - run `pip3 install requirements.txt`


### Step8: Execute locally
- use the command `streamlit run app.py`.

</details>

## The project flow

<details>
  <summary>Click here...</summary>
  <img src="https://res.cloudinary.com/pjdevex/image/upload/v1712767814/practice_gemini_process_flow_pqlrsv.webp" alt="The process flow">
</details>


### Tech Stack
- DuPont GenPoint is built using:

<details>
<summary>Click here...</summary>

|#|Component|Dependency/Library|version|Badge|Purpose|Ref|
|---|:---|:---|:---|:---|:---|:---|
|1|Programming Language| Python|3.10|![Python](https://img.shields.io/badge/Python-3.10-blue.svg)|Interpriter|[Python](https://www.python.org/)|
|2|Generative AI Framework|VertextAI|1.47.0|[![VertextAI](https://img.shields.io/badge/vertextai-1.47.0-blue)](https://pypi.org/project/vertextai/1.47.0/)|fully-managed, unified AI development platform for building and using generative AI|[Vertex AI ](https://cloud.google.com/vertex-ai?hl=en#innovate-faster-with-enterprise-ready-ai-enhanced-by-gemini-models)
|3|Multimodel Generative AI Model|Gemini-1.0-Pro-Vision|1.0|[![Gemini-Pro-1.0-Vision](https://img.shields.io/badge/Gemini_pro_vision-1.0-blue.svg)]()|Multimodal models in the Google Cloud console|[Gemini-1.0-Pro-Vision](https://console.cloud.google.com/vertex-ai/publishers/google/model-garden/gemini-pro-vision?project=practice-gemini)
|4| Web APP|Streamlit|1.33.0|[![Streamlit](https://img.shields.io/badge/Streamlit-1.33.0-red)](https://pypi.org/project/streamlit/)|A faster way to build and share data apps|[Streamlit](https://pypi.org/project/streamlit/)

</details>