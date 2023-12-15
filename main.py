import streamlit as st

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.jpg")

with col2:
    st.title("Eray Güler")
    content = """
    As a computer engineer with a Udemy certification in Java programming, I have gained valuable experience in software
     development and object-oriented programming (OOP) skills. I am currently pursuing my bachelor's and master's 
     degrees in computer engineering at Manisa Celal Bayar University, where I am learning the latest technologies 
     and methods in the field. My goal is to apply my knowledge and skills to create innovative and impactful software
      solutions that can enhance the lives of people and the performance of businesses. I am passionate about learning 
      new things, solving problems, and working with diverse and collaborative teams.
    """
    st.info(content)