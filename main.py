import streamlit as st

st.title('Movie Recomendations system')

option = st.selectbox(
    'How would you like to be contacted?',
    ('Email', 'Home phone'))

