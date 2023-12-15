import streamlit as st
import pandas

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.jpg")

with col2:
    st.title("Eray Güler")
    content = """
    As a computer engineer, I have gained valuable experience in software development and object-oriented programming 
    (OOP) skills. I am currently pursuing my bachelor's and master's degrees in computer engineering at Manisa Celal 
    Bayar University. My goal is to apply my knowledge and skills to create innovative and impactful software solutions 
    that can enhance the lives of people and the performance of  businesses. I am passionate about learning new things,
    solving problems, and working with diverse and collaborative teams.
    """
    st.info(content)

content2 = """Below you can find some of the apps I have built in Python. Feel free to contact me!"""

st.write(content2)

col3, col4 = st.columns(2)

df = pandas.read_csv("data.csv", sep=";")

with col3:
    for index, row in df[:10].iterrows():
        st.header(row["title"])

with col4:
    for index, row in df[10:].iterrows():
        st.header(row["title"])
