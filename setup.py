from setuptools import setup, find_packages

setup(
    name='practice-gemini',
    author='PJ',
    author_email='piyankra.jayadewa@gmail.com',
    version='0.0.1',
    packages=find_packages(),
    install_requires=[
        'google-generativeai',
        'python-dotenv>=1.0.1',
        'streamlit>=1.33.0',
    ]

)