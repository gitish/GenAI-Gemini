
## Get started with the Gemini API
1. Go to [Google AI Studio](https://aistudio.google.com/).
2. Login with your Google account.
3. [Create](https://aistudio.google.com/app/apikey) an API key.
![KeyGen](https://github.com/gitish/GenAI-Gemini/blob/main/img/key.png?raw=true)
4. Don't forget to setup the billing. Otehrwise you may get some exception at runtime as below
![KeyGen](https://github.com/gitish/GenAI-Gemini/blob/main/img/nobilling.png?raw=true)
5. colab application (https://colab.research.google.com/drive/1mOblzC3XtLziyFugvVlOkuTU52_UHd3H)
6. References (https://github.com/google/generative-ai-docs/blob/main/site/en/tutorials/quickstart_colab.ipynb)


# Local Setup (How to run in Local)
1. In an empty folder create a python virtual environment
```
python -m venv venv
source venv/bin/activate
```
2. Now we make a requirements.txt file for installing the packages.
```
google-generativeai
streamlit
dotenv
```
Here, the google-generativeai is a package by Google to access the Gemini model and streamlit is a fast and easy way for creating web applications. 
4. Now we install these packages
```
pip install -r requirements.txt
```
If you have pip3 installed then use pip3 command instead of pip
5. Create .env file and paste your API Key  generated above
```
GOOGLE_API_KEY="<your-API-key>"
```

## Troubleshoot command
```
python -m venv venv
. venv/bin/activate
pip3 install --upgrade pip
pip3 install flask google-cloud-aiplatform
pip3 install streamlit
pip3 install google-generativeai
pip3 install dotenv
```
