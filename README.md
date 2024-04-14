# Dupont GenPoint

![Dupont GenPoint]()

<h2>Introducing FpBot: Trusted Companion for Financial Professionals</h2>

FpBot is your go-to assistant for navigating the intricate world of accounting and auditing standards, as well as tax regulations in Sri Lanka. Whether you're a seasoned financial expert or just starting out in the industry, FpBot is here to provide you with timely and accurate information to help you stay compliant and informed. With FpBot by your side, you can tackle complex financial challenges with confidence and ease. Let FpBot be your guide as you navigate the dynamic landscape of finance in Sri Lanka.

## How to set up the project

<details>
  <summary>Click here...</summary>
### Step 1: Clone the repo
```bash
Project repo: https://github.com/PJDEVEX/fpbot
```
### Step 2: Create Virtual Environment
- Activate virtual environment
```bash
source ~/anaconda3/bin/activate
```
```bash
conda create -n fpbot python=3.10 -y
```
```bash
conda activate fbbot
```

### Step3: Install project dependencies
```bash
pip3 install -r requirements.txt
```

### Step4: Define Env variables
- create `.env`

```ini
import os

PINECONE_API_KEY=xxxxxxxxxxxxxxxxxxxxxx
PINECONE_INDEX_NAME=xxx-xxxxxxxxxxxxxxx
PINECONE_ENV=xxxxxxxxxxxxxxxxxxxxxxxxxx

EMBEDDING_MODEL_NAME=xxxxxxxxxxxxxxxxxx
HOST=0.0.0.0
PORT=5000

```

### Step5: Chat Model

Download the quantized model from `huggingface` :hugs:, create a model folder and keep the model in the folder, 
  - The chat model used is [llama-2-7b-chat.ggmlv3.q4_0.bin](https://huggingface.co/TheBloke/Llama-2-7B-Chat-GGML/blob/main/llama-2-7b-chat.ggmlv3.q4_0.bin) 
  - Downloaded from [here...](https://huggingface.co/TheBloke/Llama-2-7B-Chat-GGML/resolve/main/llama-2-7b-chat.ggmlv3.q4_0.bin?download=true)
  - Create a `model` file in `root` directory
  - Paste the model to `model` directory

### Step6: Embedding Model
  - The embedding model used is [sentence-transformers/all-MiniLM-L6-v2](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2). 
  - Please copy ```bash sentence-transformers/all-MiniLM-L6-v2``` and past in .env file.
  - It uses 384 dimensions.

### Step7: Create a Pinecone Index
- Visit [Pinecone.io](https://docs.pinecone.io/home), create an API and Index
- Dimension shall be `384` or depend on the embedding model being used
- Update .env accordingly

### Step8: Execute locally
- use the command `python3 app.py`.

</details>

## The process flow

<details>
  <summary>Click here...</summary>
  <img src="https://res.cloudinary.com/pjdevex/image/upload/v1712767814/practice_gemini_process_flow_pqlrsv.webp" alt="The process flow">
</details>


### Tech Stack

<details>
<summary>Click here...</summary>

|#|Component|Dependency/Library|version|Badge|Purpose|Ref|
|---|:---|:---|:---|:---|:---|:---|
|1|Programming Language| Python|3.10|![Python](https://img.shields.io/badge/Python-3.10-blue.svg)|Interpriter|[Python](https://www.python.org/)|
|2|Generative AI Framework(s)|LangChain|0.1.14|[![langchain](https://img.shields.io/badge/langchain-0.0.225-orange)](https://pypi.org/project/langchain/0.1.14/)|Framework for building the application with LLMs through composability|[Langchain](https://python.langchain.com/docs/get_started/introduction)
|3|"|LLamaIndex||[![LLama Index](https://img.shields.io/badge/LLama_Index-G.%20Framework-<COLOR>.svg)](https://your-link-url)|data framework for building LLM applications|[lamaIndex](https://www.llamaindex.ai/)
|4| Frontend-webapp|Flask|3.0.2|[![Flask](https://img.shields.io/badge/Flask-3.0.2-green)](https://flask.palletsprojects.com/)|||
|5|LLM|Meta Llama2||[![Meta LLama2](https://img.shields.io/badge/Meta_LLama2-LLM-blueviolet)](https://example.com)||[Meta Llama2](https://llama.meta.com/llama2/)|
|6|VectorDB|Pinecone-client|3.2.2|[![Pinecone Client](https://img.shields.io/badge/Pinecone_Client-orange?style=for-the-badge&logo=python)](https://pypi.org/project/pinecone-client/)|VectorDB|[Pinecone-client](https://pypi.org/project/pinecone-client/)|
|7|Transformer|ctransformers|0.2.27|[![ctransformers](https://img.shields.io/badge/ctransformers-v0.2.5-orange)](https://pypi.org/project/ctransformers/0.2.27/)|Python bindings for the Transformer models implemented in C/C++ using GGML library.|[C Transformers](https://python.langchain.com/docs/integrations/llms/ctransformers)|
|8|Embedding tool|sentence-transformers|2.6.1|[![Sentence Transformers](https://img.shields.io/pypi/v/sentence-transformers.svg?color=orange)](https://pypi.org/project/sentence-transformers/)| Multilingual Sentence, Paragraph, and Image Embeddings using BERT & Co.|[Sentence Transformers on Hugging Face](https://python.langchain.com/docs/integrations/text_embedding/sentence_transformers)|

</details>