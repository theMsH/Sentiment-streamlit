import pathlib
import streamlit as st
from model import train_model

model = train_model()

# Load styles
def load_css(file_path):
    with open(file_path) as f:
        st.html(f"<style>{f.read()}</style>")

load_css(pathlib.Path("assets/styles.css"))

# State params
if 'required_message' not in st.session_state:
    st.session_state.required_message = ""
if 'sent_message' not in st.session_state:
    st.session_state.sent_message = ""
if 'result_message' not in st.session_state:
    st.session_state.result_message = "Waiting your message"
if 'result_icon' not in st.session_state:
    st.session_state.result_icon = ':material/sentiment_content:'
if 'submitted' not in st.session_state:
    st.session_state.submitted = False


st.title("Sentiment analysis Streamlit App")

# Result icon
st.write('# ' + st.session_state.result_icon)
# Result message
st.write('### '+ st.session_state.result_message)
# Sent message
if st.session_state.sent_message == "":
    st.write("")
else:
    st.write('"'+st.session_state.sent_message+'"')

# Callback fuction
def on_submit():
    if st.session_state.form_message == "":
        st.session_state.required_message = ":orange[This field is required!]"
    else: 
        st.session_state.sent_message = st.session_state.form_message
        st.session_state.form_message = ""
        st.session_state.required_message = ""

        sentiment = model.predict([st.session_state.sent_message])[0]
        st.session_state.result_message = f"Your message is {sentiment}!"
        if sentiment == "positive":
            st.session_state.result_icon = ":material/sentiment_satisfied:"
        elif sentiment == "neutral":
            st.session_state.result_icon = ":material/sentiment_neutral:"
        elif sentiment == "negative":
            st.session_state.result_icon = ":material/sentiment_dissatisfied:"

# Inputs
with st.form("my_form"):
    st.text_area(
        label="Message",
        label_visibility="collapsed",
        placeholder="Write something for me to analyze!",
        key="form_message"
    )
    st.write(st.session_state.required_message)
    st.session_state.submitted = st.form_submit_button("Get sentiment!", on_click=on_submit)
