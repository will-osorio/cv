import streamlit as st
import requests
from  streamlit_lottie import st_lottie



# ---- HEADER ---- 
st.set_page_config(page_title="My Webpage", page_icon=":D", layout=("wide"))
 
st.title( "Hello, my name is William Osorio! :wave: ")
st.header('Aspire financial profesional')
st.write('I am a Finance Professional with a passion for technology and data sciences.')
st.write("Seeking new challenges and opportunities to drive innovation in financial service ")

st.write('[Learn More > (www.linkedin.com/in/willosorio) ')

def load_lottieurl(url):  
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

lottie_coding = load_lottieurl("https://assets7.lottiefiles.com/packages/lf20_gzx4caln.json")

# ---- BODY ----
with st.container():
    st.write("---")
    left_column, right_column  = st.columns(2)

with right_column:
    st_lottie(lottie_coding, height="300", key = "coding" )


 
