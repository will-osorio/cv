import streamlit as st
import requests
from  streamlit_lottie import st_lottie

st.set_page_config(page_title="My Webpage", page_icon=":D", layout=("wide"))


# ---- HEADER ---- 

    
st.title( "Hello, my name is William Osorio! :wave: ")
st.header ('Summary:')
st.write('I am a Finance Professional with a passion for technology, data sciences, and automation.')
st.write("I am seeking new challenges and opportunities to drive innovation in the financial service industry.")
st.write('[Learn More>](www.linkedin.com/in/willosorio) ')



def load_lottieurl(url):  
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

lottie_coding = load_lottieurl("https://assets7.lottiefiles.com/packages/lf20_gzx4caln.json")


with st.container():
    st.write('---')
    left_column, right_column  = st.columns(2)
    with left_column:
        st.header('About:')
        st.write('##')
        st.title( "Hello, my name is William Osorio! :wave: ")
        st.header ('Summary:')
        st.write('I am a Finance Professional with a passion for technology, data sciences, and automation.')
        st.write("I am seeking new challenges and opportunities to drive innovation in the financial service industry.")
        st.write('[Learn More > (www.linkedin.com/in/willosorio) ')

with right_column:
    st_lottie(lottie_coding, height="300", key = "coding" )




#  SECOND SECTION_________________

lottie_coding1 = load_lottieurl("https://assets9.lottiefiles.com/private_files/lf30_obidsi0t.json")


with st.container():
    st.write('---')
    left_column, right_column  = st.columns(2)
    with right_column:
        st.header('About:')
        st.write('##')
        st.title( "Hello, my name is William Osorio! :wave: ")
        st.header ('Summary:')
        st.write('I am a Finance Professional with a passion for technology, data sciences, and automation.')
        st.write("I am seeking new challenges and opportunities to drive innovation in the financial service industry.")
        st.write('[Learn More > (www.linkedin.com/in/willosorio) ')


with left_column:
    st_lottie(lottie_coding1, height="300", key = "coding1" )
# # ---- BODY ----
# with st.container():
#     st.write("---")
#     left_column, right_column  = st.columns(2)


# def load_lottieurl(url):  
#     r = requests.get(url)
#     if r.status_code != 200:
#         return None
#     return r.json()
# lottie_coding = load_lottieurl("https://assets7.lottiefiles.com/packages/lf20_gzx4caln.json")


with st.container():
    st.write("---")
    st.header("Shoot me an email!")
    st.write("##")

    # Documention: https://formsubmit.co/ !!! CHANGE EMAIL ADDRESS !!!
    contact_form = """
    <form action="https://formsubmit.co/willmosorio@gmail.COM" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Your name" required>
        <input type="email" name="email" placeholder="Your email" required>
        <textarea name="message" placeholder="Your message here" required></textarea>
        <button type="submit">Send</button>
    </form>
    """
    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st.empty()




















 
