# Sentiment-streamlit
School exercise with streamlit

You need sentiment dataset for the model to work. [Download train.csv](https://www.kaggle.com/datasets/abhi8923shriv/sentiment-analysis-dataset?resource=download&select=train.csv)

## Setup
- clone with https
- open project in VSCode
- run commands below
```
python -m venv venv
```
```
venv\Scripts\activate
```
```
python -m pip install -r requirements.txt
```
- Insert [train.csv](https://www.kaggle.com/datasets/abhi8923shriv/sentiment-analysis-dataset?resource=download&select=train.csv) into projects root folder
    - Adjust df path in model.py if using own dataset
- run streamlit locally with command below
```
streamlit run streamlit_app.py
```
