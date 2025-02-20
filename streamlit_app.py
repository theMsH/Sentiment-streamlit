import streamlit as st
from model import train_model

model = train_model()

st.header("Sentiment analysis Streamlit App")

with st.form("my_form"):
    message = st.text_input(
        "",
        placeholder="Write something for me to analyze!",
    )
    submitted = st.form_submit_button("Submit")
    if submitted:
        sentiment = model.predict([message])
        st.write("Result: ", sentiment[0])



