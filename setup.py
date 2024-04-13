from setuptools import setup, find_packages

setup(
    name='practice-gemini',
    author='PJ',
    author_email='piyankra.jayadewa@gmail.com',
    version='0.0.1',
    packages=find_packages(),
    install_requires=[
        'python-dotenv>=1.0.1',
        'streamlit>=1.33.0',
        'python-dotenv',
        'google-generativeai',
        'google-cloud-aiplatform',
        'google-api-python-client', 
        'google-auth-httplib2 ',
        'google-auth-oauthlib',
        'google-cloud-storage',
    ]

)