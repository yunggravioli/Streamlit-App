import streamlit as st
import pandas as pd
import numpy as np

st.title('Title of Application')
st.markdown('blah blah blah words words')

st.sidebar.title('Sidebar Title')

button1 = st.button('Click me >:)')
if(button1):
    st.write('Button is clicked')

agree = st.checkbox('Italic Text?')
if agree:
    st.write('Great!')
    st.markdown('*the italic text has appeared*')

side_check = st.sidebar.checkbox('Click me')
if side_check:
    st.sidebar.write('sidebar checkbox has been clicked')