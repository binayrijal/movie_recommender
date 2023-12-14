import streamlit as st
import pandas as pd
import  pickle

movies_list=pickle.load(open('moviedict.pkl','rb'))
movies= pd.DataFrame(movies_list)
st.title('Movie Recomendations system')

option = st.selectbox(
    'How would you like to be contacted?',
    movies['title'].values)

